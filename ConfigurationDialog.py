"""Python Plugin Reloader for QGIS: Configuration Dialog.

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
from qgis.PyQt import uic
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QDialog, QWidget
import qgis.utils
from pyplugin_installer import installer as plugin_installer

from .Settings import Settings


FORM_CLASS = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), 'ConfigurationDialogBase.ui'))[0]


class ConfigurationDialog(QDialog, FORM_CLASS):
    """Plugin Reloader Configuration Window."""

    def __init__(self, parent: QWidget):
        """Pseudoconstructor."""
        super().__init__(parent)
        self.setupUi(self)
        self.cbToolButtonText.setChecked(Settings.toolButtonTextEnabled())
        self.cbNotifications.setChecked(Settings.notificationsEnabled())
        self.cbExtraCommands.setChecked(Settings.extraCommandsEnabled())
        self.pteExtraCommands.setPlainText(Settings.getExtraCommands())
        if rpc := Settings.recentPluginsCount():
            self.sbRecentPluginsCount.setValue(rpc)

        # DEPRECATED The plugin selector is deprecated and disabled.
        # Keep it for some time and remove completely!
        #
        # Update the plugin list first! The plugin could be removed
        # from the list if was temporarily broken.
        # Still doesn't work in every case. TODO?: try to load from scratch
        # the plugin saved in QSettings if doesn't exist
        if len(plugin_installer.plugins.all()) == 0:
            plugin_installer.plugins.rebuild()
        qgis.utils.updateAvailablePlugins()
        plugins_list = sorted(qgis.utils.plugins.keys())
        for plugin in plugins_list:
            try:
                icon = QIcon(plugin_installer.plugins.all()[plugin]['icon'])
            except KeyError:
                icon = QIcon()
            self.comboPlugin.addItem(icon, plugin)
        if recentPlugins := Settings.recentPlugins():
            plugin = recentPlugins[0]
            if plugin in qgis.utils.plugins:
                self.comboPlugin.setCurrentIndex(plugins_list.index(plugin))

    def accept(self):
        """Accept."""
        Settings.setToolButtonTextEnabled(self.cbToolButtonText.isChecked())
        Settings.setNotificationsEnabled(self.cbNotifications.isChecked())
        Settings.setExtraCommandsEnabled(self.cbExtraCommands.isChecked())
        Settings.setExtraCommands(self.pteExtraCommands.toPlainText())
        Settings.setRecentPluginsCount(self.sbRecentPluginsCount.value())
        super().accept()
