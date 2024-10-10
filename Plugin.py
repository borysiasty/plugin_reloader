"""Python Plugin Reloader for QGIS: The plugin class.

    begin                : 2010-01-24
    copyright            : (C) 2010 by Borys Jurgiel
    email                : qgis at borysjurgiel dot pl
    The "Reload" icon copyright by Matt Ball http://www.mattballdesign.com

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
"""

import os
import sys
import subprocess
from functools import partial
from pathlib import Path
from time import time
from typing import Optional
from qgis.PyQt.QtCore import QCoreApplication, QLocale, QObject, \
    QSettings, QTranslator
from qgis.PyQt.QtGui import QColor, QIcon, QPainter, QPixmap
from qgis.PyQt.QtWidgets import QAction, QMenu, QToolButton

from qgis.core import Qgis, QgsMessageLog
from qgis.gui import QgisInterface
import qgis.utils
from pyplugin_installer import installer as plugin_installer

from .ConfigurationDialog import ConfigurationDialog
from .PluginSelectionDialog import PluginSelectionDialog
from .Settings import Settings


class Plugin:
    """The plugin class."""

    actionForPlugin: dict[Optional[str], QAction] = {}
    """Dictionary of plugin reloading actions {plugin_name: action}

    The 'configure new plugin' action is stored under a <None> key
    """

    def __init__(self, iface: QgisInterface):
        """Pseudoconstructor."""
        self.iface = iface

        self.menu = None

        if QSettings().value('locale/overrideFlag', type=bool):
            locale = QSettings().value('locale/userLocale')
        else:
            locale = QLocale.system().name()

        locale_path = os.path.join(
            os.path.dirname(__file__),
            'i18n',
            f'plugin_reloader_{locale[:2]}.qm')

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

    def tr(self, message: str) -> str:
        """Translate a string."""
        return QCoreApplication.translate('Plugin', message)

    def initGui(self):
        """Add actions to the QGIS menu and toolbar."""
        icon = QIcon(str(Path(__file__).parent / "reload.png"))
        iconConf = QIcon(str(Path(__file__).parent / "reload-conf.png"))

        self.menu = self.iface.pluginMenu().addMenu(icon, self.tr(
            "&Plugin Reloader"))

        self.toolButton = QToolButton()
        self.toolButton.setMenu(QMenu())
        self.toolButton.setToolButtonStyle(Settings.toolButtonStyle())
        self.toolButton.setPopupMode(
            QToolButton.ToolButtonPopupMode.MenuButtonPopup)
        toolButtonMenu = self.toolButton.menu()

        # Create default action for the tool button
        # NOTE The action text must be constant due to the assigned
        # keybord shortcut. However, the button text and action tooltip
        # will be later updated according to the current plugin name.
        self.actionReloadRecentPlugin = QAction(
            icon, self.tr("Reload recent plugin"))
        self.actionReloadRecentPlugin.setObjectName(
            "PluginReloader_ReloadRecentPlugin")
        self.iface.registerMainWindowAction(
            self.actionReloadRecentPlugin, "Ctrl+F5")

        # Create actions for recently processed plugins
        self.actionForPlugin = {}
        for plugin in Settings.recentPlugins():
            self.actionForPlugin[plugin] = self.createActionForPlugin(plugin)

        # Create action for adding a new plugin
        self.actionAddNewPlugin = QAction(icon, self.tr("Reload a plugin..."))
        run = partial(self.run, None)
        self.actionAddNewPlugin.triggered.connect(run)
        # Append it to the acions dictionary under a NULL key
        self.actionForPlugin[None] = self.actionAddNewPlugin

        # Create action for opening the settings window
        self.actionSettings = QAction(iconConf, self.tr("Configure"))
        self.actionSettings.triggered.connect(self.openConfigWindow)

        # Add the actionReloadRecentPlugin to menu (to present its shortcut)
        # and set it to the tool buttton as the default action
        self.toolButton.setDefaultAction(self.actionReloadRecentPlugin)
        self.menu.addAction(self.actionReloadRecentPlugin)
        self.menu.addSeparator()

        # Update the default action's icon and tooltip and the tool button
        # text to the most recent plugin. The action text stays constant.
        recentPlugin = list(self.actionForPlugin.keys())[0]
        # NOTE Updating the button text must be done after setting the button's
        # default action!
        self.updateDefaultAction(recentPlugin)

        # Add all the rest of the actions to the menu and the toolbar
        for action in self.actionForPlugin.values():
            toolButtonMenu.addAction(action)
            self.menu.addAction(action)

        toolButtonMenu.addSeparator()
        self.menu.addSeparator()

        toolButtonMenu.addAction(self.actionSettings)
        self.menu.addAction(self.actionSettings)

        self.iface.addToolBarWidget(self.toolButton)

        self.iface.initializationCompleted.connect(self.updatePluginIcons)

    def unload(self):
        """Remove the plugin's actions from the QGIS menu and toolbars."""
        if not self.menu:
            # The initGui() method was never called
            return

        self.iface.unregisterMainWindowAction(self.actionReloadRecentPlugin)
        self.iface.pluginMenu().removeAction(self.menu.menuAction())
        self.toolButton.deleteLater()

    def createActionForPlugin(self, plugin: str) -> QAction:
        """Create reloading action for a given plugin."""
        icon = self.iconForPlugin(plugin)
        actionName = self.tr("Reload plugin: {}").format(plugin)
        action = QAction(icon, actionName)
        action.setToolTip(actionName)
        run = partial(self.run, plugin)
        action.triggered.connect(run)
        return action

    def actionsForRecentPlugins(self) -> list[QAction]:
        """Return list of actions for recently reloaded plugins."""
        actions = [a for a in self.actionForPlugin.values()
                   if a != self.actionAddNewPlugin]
        return actions

    def updateDefaultAction(self, plugin: str):
        """Update the tool button's icon, tooltip, signal and displayed text, \
        while keeping the action name constant due to registered shortuct.

        NOTE: Since QGIS 3.32 keyboard shortcuts are registered by objectName
        and not the action text, so it can be simplified some day.
        """
        self.actionReloadRecentPlugin.setIcon(
            self.iconForPlugin(plugin, withOverlay=True))

        text = self.actionForPlugin[plugin].text()
        toolTipText = text
        shortcutText = self.actionReloadRecentPlugin.shortcut().toString()
        if shortcutText and shortcutText not in toolTipText:
            toolTipText = f"{toolTipText} ({shortcutText})"
        self.actionReloadRecentPlugin.setToolTip(toolTipText)
        run = partial(self.run, plugin)
        self.actionReloadRecentPlugin.disconnect()
        self.actionReloadRecentPlugin.triggered.connect(run)
        self.toolButton.setText(text)

    def iconForPlugin(self, plugin: str, withOverlay: bool = False) -> QIcon:
        """Return plugin icon.

        If no plugin icon is availabie, falls back to the reloader icon.

        :param withOverlay: whether to add the reloader arrow overlay
        """
        reloaderIcon = QIcon(str(Path(__file__).parent / "reload.png"))
        if plugin == 'plugin_reloader':
            return reloaderIcon
        if plugin not in plugin_installer.plugins.all():
            return reloaderIcon
        if 'icon' not in plugin_installer.plugins.all()[plugin]:
            return reloaderIcon

        icon = QIcon(plugin_installer.plugins.all()[plugin]['icon'])

        if withOverlay:
            srcPm = icon.pixmap(64, 64)
            ovrPm = reloaderIcon.pixmap(64, 64)

            pixmap = QPixmap(64, 64)
            pixmap.fill(QColor(0, 0, 0, 0))
            painter = QPainter(pixmap)
            painter.drawPixmap(0, 0, 64, 64, srcPm)
            painter.drawPixmap(20, 20, 48, 48, ovrPm)
            painter.end()
            icon = QIcon(pixmap)

        return icon

    def updatePluginIcons(self):
        """Update plugin icons when QGIS initialization is completed \
        and plugin registry is filled."""
        for plugin, action in self.actionForPlugin.items():
            if plugin in plugin_installer.plugins.all():
                icon = self.iconForPlugin(plugin)
                action.setIcon(icon)

        recentPlugin = list(self.actionForPlugin.keys())[0]
        self.updateDefaultAction(recentPlugin)

    def choosePluginToReload(self) -> Optional[str]:
        """Open the plugin selection dialog and return choosen plugin."""
        dlg = PluginSelectionDialog(self.iface.mainWindow())
        dlg.exec()
        if dlg.result():
            plugin = dlg.comboPlugin.currentText()
        else:
            plugin = None
        return plugin

    def openConfigWindow(self):
        """Open the configuration dialog."""
        recentPluginsCount = len(self.actionsForRecentPlugins())
        dlg = ConfigurationDialog(self.iface.mainWindow())
        dlg.exec()
        if dlg.result():
            if self.toolButton.toolButtonStyle() != Settings.toolButtonStyle():
                self.toolButton.setToolButtonStyle(Settings.toolButtonStyle())
            if recentPluginsCount > Settings.recentPluginsCount():
                # The max. number of recent plugins is below the current one.
                allRecentPlugins = Settings.recentPlugins(listAll=True)
                toRemove = allRecentPlugins[Settings.recentPluginsCount():]
                for plugin in toRemove:
                    toolButtonMenu = self.toolButton.menu()
                    for menu in (toolButtonMenu, self.menu):
                        menu.removeAction(self.actionForPlugin[plugin])

    def run(self, plugin: Optional[str] = None):
        """Reload a plugin."""
        # Udate the plugin list first! The plugin could be removed
        # from the list if was temporarily broken.
        qgis.utils.updateAvailablePlugins()

        # Select another plugin if the old one is unavailable
        if plugin is not None and plugin not in qgis.utils.available_plugins:
            self.iface.messageBar().pushMessage(
                self.tr('Plugin <b>{}</b> not found.').format(plugin),
                Qgis.Warning, 1)
            plugin = None

        if plugin is None:
            # Open plugin selection window
            plugin = self.choosePluginToReload()

            if plugin is None:
                # User cancelled
                return

        self.updateRecentPluginsOrder(plugin)

        # Run extra commands before reloading
        if Settings.extraCommandsEnabled():
            successExtraCommands = self.handleExtraCommands()
            if not successExtraCommands:
                return

        self.reloadPlugin(plugin)

    def updateRecentPluginsOrder(self, recentPlugin: str):
        """Update menus and settings by putting the recent plugin on top."""
        oldTopAction = self.toolButton.menu().actions()[0]

        if recentPlugin in self.actionForPlugin:
            # Move the reloaded plugin to the top of the list
            newTopAction = self.actionForPlugin[recentPlugin]
            if newTopAction != oldTopAction:
                self.toolButton.menu().insertAction(
                    self.toolButton.menu().actions()[0], newTopAction)
                self.menu.insertAction(self.menu.actions()[2], newTopAction)
        else:
            # Add the new action on top...
            newTopAction = self.createActionForPlugin(recentPlugin)
            self.actionForPlugin[recentPlugin] = newTopAction
            self.toolButton.menu().insertAction(
                self.toolButton.menu().actions()[0], newTopAction)
            self.menu.insertAction(self.menu.actions()[2], newTopAction)
            # ...and remove the oldest one if necessary.
            recentPluginsCount = len(self.actionForPlugin) - 1
            if recentPluginsCount > Settings.recentPluginsCount():
                oldestPlugin = Settings.recentPlugins()[-1]
                oldestPluginAction = self.actionForPlugin.pop(oldestPlugin)
                for menu in (self.toolButton.menu(), self.menu):
                    menu.removeAction(oldestPluginAction)

        if newTopAction != oldTopAction:
            # Update the button's default action
            self.updateDefaultAction(recentPlugin)
            # Set the plugin as the most recent
            Settings.updateRecentPlugins(recentPlugin)

    def reloadPlugin(self, plugin: str):
        """Reload plugin with submodules and check if it was successful."""
        windowState = self.iface.mainWindow().saveState()
        startTime = time()

        # Try to initially load the selected plugin if not loaded yet
        if plugin not in qgis.utils.plugins:
            qgis.utils.loadPlugin(plugin)
            qgis.utils.startPlugin(plugin)
            qgis.utils.updateAvailablePlugins()

        qgis.utils.unloadPlugin(plugin)

        # Remove submodules left by qgis.utils.unloadPlugin
        # NOTE Since QGIS 3.4.8, imported submodules are unloaded automagically
        # by qgis.utils.unloadPlugin. However, parent packages that weren't
        # directly imported, are not handled.
        for key in list(sys.modules.keys()):
            if plugin in key:
                if hasattr(sys.modules[key], 'qCleanupResources'):
                    sys.modules[key].qCleanupResources()
                del sys.modules[key]

        qgis.utils.loadPlugin(plugin)
        pluginStarted = qgis.utils.startPlugin(plugin)

        endTime = time()
        self.iface.mainWindow().restoreState(windowState)

        if pluginStarted and Settings.notificationsEnabled():
            duration = int(round((endTime - startTime) * 1000))
            msg = self.tr('<b>{}</b> reloaded in {} ms.').format(plugin,
                                                                 duration)
            self.iface.messageBar().pushMessage(msg, Qgis.Success)
            # Actual name of the "Plugins" tab in the message log panel
            # is localized, so we need to find it in QGIS' translations.
            # Don't pass the string value directly to QObject().tr()
            # to prevent local pylupdate from catching it.
            pluginsLogTabSourceName = "Plugins"
            pluginsLogTabName = QObject().tr(pluginsLogTabSourceName)
            QgsMessageLog.logMessage(msg, pluginsLogTabName, level=Qgis.Info)

    def handleExtraCommands(self) -> bool:
        """Execute extra CLI commands prior to the plugin reload."""
        recentPlugins = Settings.recentPlugins()
        if recentPlugins:
            plugin = recentPlugins[0]
        else:
            return False

        try:
            extraCommands = Settings.getExtraCommands()
            if extraCommands.strip():  # Prevent an empty command to be run
                path = plugin_installer.plugins.all()[plugin]['library']
                extraCommands = extraCommands.replace('%PluginName%', plugin)
                extraCommands = extraCommands.replace('%PluginPath%', path)

                completed_process = subprocess.run(
                    extraCommands,
                    shell=True,
                    capture_output=True,
                    check=True,
                )

                message = completed_process.stdout.decode('utf-8', 'replace')
                if message:
                    self.iface.messageBar().pushMessage(message, Qgis.Info)

            successExtraCommands = True

        except subprocess.CalledProcessError as exc:
            self.iface.messageBar().pushMessage(
                self.tr('Could not execute extra commands: {}').format(
                    exc.stderr.decode('utf-8', 'replace')),
                Qgis.Warning
            )
            successExtraCommands = False

        return successExtraCommands
