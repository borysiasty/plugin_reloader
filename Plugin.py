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
from time import time
from qgis.PyQt.QtCore import QCoreApplication, QLocale, QSettings, QTranslator
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QMenu, QToolButton

from qgis.core import Qgis
from qgis.gui import QgisInterface
import qgis.utils
from pyplugin_installer import installer as plugin_installer

from .ConfigurationDialog import ConfigurationDialog
from .Settings import Settings


class Plugin:
    """The plugin class."""

    def __init__(self, iface: QgisInterface):
        """Pseudoconstructor."""
        self.iface = iface
        self.toolButton = QToolButton()
        self.toolButton.setMenu(QMenu())
        self.toolButton.setPopupMode(
            QToolButton.ToolButtonPopupMode.MenuButtonPopup)
        self.toolBtnAction = self.iface.addToolBarWidget(self.toolButton)

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
        return QCoreApplication.translate('ReloaderPlugin', message)

    def theBestShortcutForPluginReload(self):
        """Try to find the best saved setting.

        NOTE *the action name is variable*, so the "Keyboard Shortcuts" window
        tends to save concurrent shortcuts:
              .../shortcuts/Reload plugin: plugin Foo=F5
              .../shortcuts/Reload plugin: plugin Bar=Ctrl+F5
              .../shortcuts/Reload plugin: plugin HelloWorld=Ctrl+Alt+Del
        so we should find the recent one (not always possible)
        and remove the rest.
        """
        DEFAULT = "Ctrl+F5"
        settings = QSettings()
        settings.beginGroup('shortcuts')
        # Find all saved shortcuts:
        keys = [key for key in settings.childKeys()
                if key.startswith(self.tr('Reload plugin: '))]
        if settings.contains(self.tr('Reload chosen plugin')):
            keys.append(self.tr('Reload chosen plugin'))
        if not keys:
            # Nothing found in settings - fallback to default:
            key = None
            shortcut = DEFAULT
        elif len(keys) == 1:
            # Just one setting found, take that!
            shortcut = settings.value(keys[0])
        else:
            # More then one old setting found.
            # Take the best one and remove the rest.
            if self.actionRun.text() in keys:
                # The current action text found.
                # Let's hope it's the recent one...
                key = self.actionRun.text()
                shortcut = settings.value(key)
            else:
                # Otherwise take the first one
                key = keys[0]
                shortcut = settings.value(key)
            # Remove redundant settings
            for i in keys:
                if i != key:
                    settings.remove(i)
        return shortcut

    def initGui(self):
        """Add the plugin's actions to the QGIS menu and toolbars."""
        self.actionRun = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), "reload.png")),
            self.tr('Reload chosen plugin'),
            self.iface.mainWindow()
        )
        self.actionRun.setToolTip(self.tr('Reload chosen plugin'))
        plugin = Settings.currentPlugin()
        if plugin:
            self.actionRun.setToolTip(
                self.tr('Reload plugin: {}').format(plugin))
            self.actionRun.setText(
                self.tr('Reload plugin: {}').format(plugin))
        self.iface.addPluginToMenu(self.tr('&Plugin Reloader'), self.actionRun)
        self.iface.registerMainWindowAction(
            self.actionRun, self.theBestShortcutForPluginReload())
        m = self.toolButton.menu()
        m.addAction(self.actionRun)
        self.toolButton.setDefaultAction(self.actionRun)
        self.actionRun.triggered.connect(self.run)
        self.actionConfigure = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), "reload-conf.png")),
            self.tr('Configure'),
            self.iface.mainWindow()
        )
        self.iface.registerMainWindowAction(self.actionConfigure, "Shift+F5")
        self.actionConfigure.setToolTip(
            self.tr('Choose a plugin to be reloaded'))
        m.addAction(self.actionConfigure)
        self.iface.addPluginToMenu(self.tr('&Plugin Reloader'),
                                   self.actionConfigure)
        self.actionConfigure.triggered.connect(self.openConfigWindow)

    def unload(self):
        """Remove the plugin's actions from the QGIS menu and toolbars."""
        for action in [self.actionRun, self.actionConfigure]:
            self.iface.removePluginMenu(self.tr('&Plugin Reloader'), action)
            self.iface.removeToolBarIcon(action)
            self.iface.unregisterMainWindowAction(action)

        self.iface.removeToolBarIcon(self.toolBtnAction)

    def handleExtraCommands(self) -> bool:
        """Execute extra CLI commands prior to the plugin reload."""
        try:
            extraCommands = Settings.getExtraCommands()
            if extraCommands.strip():  # Prevent an empty command to be run
                plugin = Settings.currentPlugin()
                path = plugin_installer.plugins.all()[plugin]['library']
                extraCommands = extraCommands.replace('%PluginName%', plugin)
                extraCommands = extraCommands.replace('%PluginPath%', path)

                completed_process = subprocess.run(
                    extraCommands,
                    shell=True,
                    capture_output=True,
                    check=True,
                )

                self.iface.messageBar().pushMessage(
                    completed_process.stdout.decode('utf-8', 'replace'),
                    Qgis.Info
                )

            successExtraCommands = True

        except subprocess.CalledProcessError as exc:
            self.iface.messageBar().pushMessage(
                self.tr('Could not execute extra commands: {}').format(
                    exc.stderr.decode('utf-8', 'replace')),
                Qgis.Warning
            )
            successExtraCommands = False

        return successExtraCommands

    def run(self):
        """Reload the selected plugin."""
        if len(plugin_installer.plugins.all()) == 0:
            plugin_installer.plugins.rebuild()

        if Settings.extraCommandsEnabled():
            successExtraCommands = self.handleExtraCommands()
            if not successExtraCommands:
                return

        plugin = Settings.currentPlugin()

        # Udate the plugin list first! The plugin could be removed
        # from the list if was temporarily broken.
        qgis.utils.updateAvailablePlugins()

        # Try to load from scratch the plugin saved in QSettings if not loaded
        if plugin not in qgis.utils.plugins and plugin != "":
            qgis.utils.loadPlugin(plugin)
            qgis.utils.startPlugin(plugin)
            qgis.utils.updateAvailablePlugins()

        # Give one chance for correct (not a loop)
        if plugin not in qgis.utils.plugins:
            self.iface.messageBar().pushMessage(
                self.tr('Plugin <b>{}</b> not found.').format(plugin),
                Qgis.Warning, 0)
            self.openConfigWindow()
            self.iface.messageBar().currentItem().dismiss()
            plugin = Settings.currentPlugin()

        if plugin in qgis.utils.plugins:
            state = self.iface.mainWindow().saveState()

            # Unload submodules
            for key in list(sys.modules.keys()):
                if plugin in key:
                    if hasattr(sys.modules[key], 'qCleanupResources'):
                        sys.modules[key].qCleanupResources()
                    del sys.modules[key]

            # Reload plugin and check if it was successful.
            # Starting with QGIS 3.22, qgis.utils.reloadPlugin() returns bool
            # but it returns nothing in prior versions. The function is
            # thus replicated for compatibility.
            startTime = time()
            qgis.utils.unloadPlugin(plugin)
            qgis.utils.loadPlugin(plugin)
            pluginStarted = qgis.utils.startPlugin(plugin)
            endTime = time()

            self.iface.mainWindow().restoreState(state)
            if Settings.notificationsEnabled() and pluginStarted:
                # Not sure if we're more interested in the total time
                # (a developer's business) or just qgis.utils.reloadPlugin
                # (to see how much a huge plugin slows down the QGIS start).
                duration = int(round((endTime - startTime) * 1000))
                self.iface.messageBar().pushMessage(
                    self.tr('<b>{}</b> reloaded in {} ms.').format(plugin,
                                                                   duration),
                    Qgis.Success
                )

    def openConfigWindow(self):
        """Open the configuration dialog."""
        if len(plugin_installer.plugins.all()) == 0:
            plugin_installer.plugins.rebuild()

        dlg = ConfigurationDialog(self.iface)
        dlg.exec()
        if dlg.result():
            plugin = dlg.comboPlugin.currentText()
            self.actionRun.setToolTip(
                self.tr('Reload plugin: {}').format(plugin))
            self.actionRun.setText(
                self.tr('Reload plugin: {}').format(plugin))
            Settings.setCurrentPlugin(plugin)
            Settings.setNotificationsEnabled(dlg.cbNotifications.isChecked())
            Settings.setExtraCommandsEnabled(dlg.cbExtraCommands.isChecked())
            Settings.setExtraCommands(dlg.pteExtraCommands.toPlainText())
