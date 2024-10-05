"""Python Plugin Reloader for QGIS: Plugin Selection Dialog.

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
    os.path.join(os.path.dirname(__file__), 'PluginSelectionDialogBase.ui'))[0]


class PluginSelectionDialog(QDialog, FORM_CLASS):
    """Plugin Selection Window."""

    def __init__(self, parent: QWidget):
        """Pseudoconstructor."""
        super().__init__(parent)
        self.setupUi(self)

        # Update the plugin list first! The plugin could be removed
        # from the list if was temporarily broken.
        # Still doesn't work in every case. TODO?: try to load from scratch
        # the plugin saved in QSettings if doesn't exist
        if not plugin_installer.plugins.all():
            plugin_installer.plugins.rebuild()
        qgis.utils.updateAvailablePlugins()
        plugins_list = list(qgis.utils.plugins.keys())
        plugins_list.sort()
        for plugin in plugins_list:
            try:
                icon = plugin_installer.plugins.all()[plugin]['icon']
                icon = QIcon(icon)
            except KeyError:
                icon = QIcon()
            self.comboPlugin.addItem(icon, plugin)
        recentPlugins = Settings.recentPlugins()
        if recentPlugins:
            plugin = recentPlugins[0]
            if plugin in qgis.utils.plugins:
                self.comboPlugin.setCurrentIndex(plugins_list.index(plugin))
