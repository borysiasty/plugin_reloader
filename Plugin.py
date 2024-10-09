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
from qgis.PyQt.QtGui import QIcon, QPixmap
from qgis.PyQt.QtWidgets import QAction, QLabel, QMenu, QToolButton

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

        self.iface.initializationCompleted.connect(self.updatePluginIcons)

    def tr(self, message: str) -> str:
        """Translate a string."""
        return QCoreApplication.translate('Plugin', message)

    def shortcut(self):
        """Try to find the best saved keyboard shortcut for recent reload.

        NOTE The action text is variable, so QGIS might save
        concurrent shortcuts:
              .../shortcuts/Reload plugin: plugin Foo=F5
              .../shortcuts/Reload plugin: plugin Bar=Ctrl+F5
              .../shortcuts/Reload plugin: plugin HelloWorld=Ctrl+Alt+Del
        """
        # Start from default value
        shortcut = "Ctrl+F5"

        # Look for a saved one
        settings = QSettings()
        settings.beginGroup('shortcuts')
        actionTextPrefix = self.tr('Reload plugin: ')
        for key in settings.childKeys():
            if key.startswith(actionTextPrefix) and settings.value(key):
                # Take the first one in case there could be more
                shortcut = settings.value(key)
                break

        return shortcut

    def saveShortcut(self, plugin: str, shortcut: str):
        """Save the current keyboard shortcut to settings.

        This is neccessary
            # Store the current keyboard shortcut (it's necessary to keep
            # the shortcut associated with the changing actions)

        """
        actionTextPrefix = self.tr('Reload plugin: ')

        settings = QSettings()
        settings.beginGroup('shortcuts')

        # Remove old entries
        for key in settings.childKeys():
            if key.startswith(actionTextPrefix):
                settings.remove(key)

        # Add the current one
        key = actionTextPrefix + plugin
        settings.setValue(key, shortcut)

    def actionsForRecentPlugins(self) -> list[QAction]:
        """Return list of actions for recently reloaded plugins."""
        actions = [a for a in self.actionForPlugin.values()
                   if a != self.actionAddNewPlugin]
        return actions

    def setTopAction(self, topAction: QAction):
        """Set the fist action as the default of the tool button \
        and (re)assign the keyboard shortcut to it."""
        self.toolButton.setDefaultAction(topAction)

        for action in self.actionsForRecentPlugins():
            if action == topAction:
                # Always assign the default/saved shortcut to the first action.
                self.iface.registerMainWindowAction(action, self.shortcut())
            else:
                # Unset shortcut from the previous action
                if action.shortcut().toString():
                    self.iface.unregisterMainWindowAction(action)
                    action.setShortcut('')

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

        # Create actions for recently processed plugins + a configurable one.
        self.actionForPlugin = {}
        for plugin in Settings.recentPlugins():
            self.actionForPlugin[plugin] = self.createActionForPlugin(plugin)

        self.actionAddNewPlugin = QAction(icon, self.tr("Reload a plugin..."))
        run = partial(self.run, None)
        self.actionAddNewPlugin.triggered.connect(run)

        self.actionForPlugin[None] = self.actionAddNewPlugin

        self.setTopAction(list(self.actionForPlugin.values())[0])

        self.actionSettings = QAction(iconConf, self.tr("Configure"))
        self.actionSettings.triggered.connect(self.openConfigWindow)

        toolButtonMenu = self.toolButton.menu()

        for action in self.actionForPlugin.values():
            toolButtonMenu.addAction(action)
            self.menu.addAction(action)

        toolButtonMenu.addSeparator()
        self.menu.addSeparator()

        toolButtonMenu.addAction(self.actionSettings)
        self.menu.addAction(self.actionSettings)

        self.iconLabel = QLabel()
        self.iconLabel.setPixmap(QPixmap(
            str(Path(__file__).parent / 'reload.png')))

        self.iface.addToolBarWidget(self.iconLabel)
        self.iface.addToolBarWidget(self.toolButton)

    def updatePluginIcons(self):
        """Update plugin icons when QGIS initialization is completed \
        and plugin registry is filled."""
        for plugin, action in self.actionForPlugin.items():
            if plugin in plugin_installer.plugins.all():
                icon = QIcon(plugin_installer.plugins.all()[plugin]['icon'])
                action.setIcon(icon)

    def unload(self):
        """Remove the plugin's actions from the QGIS menu and toolbars."""
        if not self.menu:
            # The initGui() method was never called
            return

        for action in self.actionsForRecentPlugins():
            self.iface.unregisterMainWindowAction(action)

        self.iface.pluginMenu().removeAction(self.menu.menuAction())
        self.toolButton.deleteLater()
        self.iconLabel.deleteLater()

    def createActionForPlugin(self, plugin: str) -> QAction:
        """Create reloading action for a given plugin."""
        try:
            icon = QIcon(plugin_installer.plugins.all()[plugin]['icon'])
        except KeyError:
            icon = QIcon(str(Path(__file__).parent / "reload.png"))
        actionName = self.tr("Reload plugin: {}").format(plugin)
        action = QAction(icon, actionName)
        action.setToolTip(actionName)
        run = partial(self.run, plugin)
        action.triggered.connect(run)
        return action

    def selectPlugin(self) -> Optional[str]:
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
            plugin = self.selectPlugin()

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
        menus = (self.toolButton.menu(), self.menu)

        oldTopAction = self.menu.actions()[0]

        if recentPlugin in self.actionForPlugin:
            # Move the reloaded plugin to the top of the list
            newTopAction = self.actionForPlugin[recentPlugin]
            if newTopAction != oldTopAction:
                for menu in menus:
                    menu.insertAction(menu.actions()[0], newTopAction)
        else:
            # Add the new action on top...
            newTopAction = self.createActionForPlugin(recentPlugin)
            self.actionForPlugin[recentPlugin] = newTopAction
            for menu in menus:
                menu.insertAction(menu.actions()[0], newTopAction)
            # ...and remove the oldest one if necessary.
            recentPluginsCount = len(self.actionForPlugin) - 1
            if recentPluginsCount > Settings.recentPluginsCount():
                oldestPlugin = Settings.recentPlugins()[-1]
                oldestPluginAction = self.actionForPlugin.pop(oldestPlugin)
                for menu in menus:
                    menu.removeAction(oldestPluginAction)

        if newTopAction != oldTopAction:
            if oldTopAction != self.actionAddNewPlugin:
                # Preserve the current keyboard shortcut when the aassociated
                # action change
                shortcut = oldTopAction.shortcut().toString()
                self.saveShortcut(recentPlugin, shortcut)

            # Move the new action to top
            self.setTopAction(newTopAction)
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
