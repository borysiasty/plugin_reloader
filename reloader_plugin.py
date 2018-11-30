# -*- coding: utf-8 -*-
# ***************************************************************************
# reloader_plugin.py  -  A Python Plugin Reloader for QGIS
# ---------------------
#     begin                : 2010-01-24
#     copyright            : (C) 2010 by Borys Jurgiel
#     email                : info at borysjurgiel dot pl
#     The "Reload" icon copyright by Matt Ball http://www.mattballdesign.com
# ***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************

import os
import sys
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt import uic
from qgis.core import Qgis as QGis
from qgis.utils import plugins, reloadPlugin, updateAvailablePlugins, loadPlugin, startPlugin
from pyplugin_installer import installer as plugin_installer

Ui_ConfigureReloaderDialogBase = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'configurereloaderbase.ui'))[0]

def currentPlugin():
    settings = QSettings()
    return unicode(settings.value('/PluginReloader/plugin', '', type=str))


class ConfigureReloaderDialog (QDialog, Ui_ConfigureReloaderDialogBase):
  def __init__(self, parent):
    super().__init__()
    self.iface = parent
    self.setupUi(self)
    #update the plugin list first! The plugin could be removed from the list if was temporarily broken.
    #Still doesn't work in every case. TODO?: try to load from scratch the plugin saved in QSettings if doesn't exist
    plugin = currentPlugin()
    updateAvailablePlugins()
    #if plugin not in plugins:
      #try:
        #loadPlugin(plugin)
        #startPlugin(plugin)
      #except:
        #pass
    #updateAvailablePlugins()

    plugins_list = sorted(plugins.keys())
    for plugin in plugins_list:
      try:
        icon = QIcon(plugin_installer.plugins.all()[plugin]['icon'])
      except KeyError:
        icon = QIcon()
      self.comboPlugin.addItem(icon, plugin)
    plugin = currentPlugin()
    if plugin in plugins:
      self.comboPlugin.setCurrentIndex(plugins_list.index(plugin))


class ReloaderPlugin():
  def __init__(self, iface):
    self.iface = iface
    self.toolButton = QToolButton()
    self.toolButton.setMenu(QMenu())
    self.toolButton.setPopupMode(QToolButton.MenuButtonPopup)
    self.toolBtnAction = self.iface.addToolBarWidget(self.toolButton)

  def theBestShortcutForPluginReload(self):
    ''' Try to find the best saved setting.
        Note **the action name is variable**, so the "Keyboard Shortcuts" window
        tends to save concurrent shortcuts:
              .../shortcuts/Reload plugin: plugin Foo=F5
              .../shortcuts/Reload plugin: plugin Bar=Ctrl+F5
              .../shortcuts/Reload plugin: plugin HelloWorld=Ctrl+Alt+Del
        so we should find the recent one (not always possible) and remove the rest.
    '''
    DEFAULT = "Ctrl+F5"
    settings = QSettings()
    settings.beginGroup('shortcuts')
    # Find all saved shortcuts:
    keys = [key for key in settings.childKeys() if key.startswith('Reload plugin: ')]
    if settings.contains('Reload chosen plugin'):
        keys.append('Reload chosen plugin')
    if not len(keys):
        # Nothing found in settings - fallback to default:
        key = None
        shortcut = DEFAULT
    elif len(keys) == 1:
        # Just one setting found, take that!
        shortcut = settings.value(keys[0])
    else:
        # More then one old setting found. Take the best one and remove the rest.
        if self.actionRun.text() in keys:
            # The current action text found - let's hope it's the recent one...
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
    self.actionRun = QAction(
      QIcon(os.path.join(os.path.dirname(__file__), "reload.png")),
      "Reload chosen plugin",
      self.iface.mainWindow()
    )
    self.actionRun.setToolTip("Reload chosen plugin")
    plugin = currentPlugin()
    if plugin:
      self.actionRun.setToolTip("Reload plugin: {}".format(plugin))
      self.actionRun.setText("Reload plugin: {}".format(plugin))
    self.iface.addPluginToMenu("&Plugin Reloader", self.actionRun)
    self.iface.registerMainWindowAction(self.actionRun, self.theBestShortcutForPluginReload())
    m = self.toolButton.menu()
    m.addAction(self.actionRun)
    self.toolButton.setDefaultAction(self.actionRun)
    self.actionRun.triggered.connect(self.run)
    self.actionConfigure = QAction(
      QIcon(os.path.join(os.path.dirname(__file__), "reload-conf.png")),
      "Configure",
      self.iface.mainWindow()
    )
    self.iface.registerMainWindowAction(self.actionConfigure, "Shift+F5")
    self.actionConfigure.setToolTip("Choose a plugin to be reloaded")
    m.addAction(self.actionConfigure)
    self.iface.addPluginToMenu("&Plugin Reloader", self.actionConfigure)
    self.actionConfigure.triggered.connect(self.configure)

  def unload(self):
    self.iface.removePluginMenu("&Plugin Reloader",self.actionRun)
    self.iface.removePluginMenu("&Plugin Reloader",self.actionConfigure)
    self.iface.removeToolBarIcon(self.actionRun)
    self.iface.removeToolBarIcon(self.actionConfigure)
    self.iface.unregisterMainWindowAction(self.actionRun)
    self.iface.unregisterMainWindowAction(self.actionConfigure)
    self.iface.removeToolBarIcon(self.toolBtnAction)

  def run(self):
    plugin = currentPlugin()
    #update the plugin list first! The plugin could be removed from the list if was temporarily broken.
    updateAvailablePlugins()
    #try to load from scratch the plugin saved in QSettings if not loaded
    if plugin not in plugins:
      try:
        loadPlugin(plugin)
        startPlugin(plugin)
      except:
        pass
    updateAvailablePlugins()
    #give one chance for correct (not a loop)
    if plugin not in plugins:
      self.configure()
      plugin = currentPlugin()
    if plugin in plugins:
      state = self.iface.mainWindow().saveState()

      # Unload submodules
      for key in [key for key in sys.modules.keys()]:
        if '{}.'.format(plugin) in key:
          if hasattr(sys.modules[key], 'qCleanupResources'):
            sys.modules[key].qCleanupResources()
          del sys.modules[key]

      reloadPlugin(plugin)
      self.iface.mainWindow().restoreState(state)
      self.iface.messageBar().pushMessage("<b>{}</b> reloaded.".format(plugin), QGis.Info)

  def configure(self):
    dlg = ConfigureReloaderDialog(self.iface)
    dlg.exec_()
    if dlg.result():
      plugin = dlg.comboPlugin.currentText()
      settings = QSettings()
      self.actionRun.setToolTip("Reload plugin: {}".format(plugin))
      self.actionRun.setText("Reload plugin: {}".format(plugin))
      settings.setValue('/PluginReloader/plugin', plugin)
