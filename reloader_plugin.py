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
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt import uic
from qgis.core import Qgis as QGis
from qgis.utils import plugins, reloadPlugin, updateAvailablePlugins, loadPlugin, startPlugin

Ui_ConfigureReloaderDialogBase = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'configurereloaderbase.ui'))[0]

def currentPlugin():
    settings = QSettings()
    return unicode(settings.value('/PluginReloader/plugin', '', type=str))


class ConfigureReloaderDialog (QDialog, Ui_ConfigureReloaderDialogBase):
  def __init__(self, parent):
    QDialog.__init__(self)
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
      self.comboPlugin.addItem(plugin)
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

  def initGui(self):
    self.actionRun = QAction(
      QIcon(os.path.join(os.path.dirname(__file__), "reload.png")),
      u"Reload chosen plugin",
      self.iface.mainWindow()
    )
    self.iface.registerMainWindowAction(self.actionRun, "F5")
    self.actionRun.setWhatsThis(u"Reload chosen plugin")
    plugin = currentPlugin()
    if plugin:
      self.actionRun.setWhatsThis(u"Reload plugin: %s" % plugin)
      self.actionRun.setText(u"Reload plugin: %s" % plugin)
    self.iface.addPluginToMenu("&Plugin Reloader", self.actionRun)
    m = self.toolButton.menu()
    m.addAction(self.actionRun)
    self.toolButton.setDefaultAction(self.actionRun)
    self.actionRun.triggered.connect(self.run)
    self.actionConfigure = QAction(
      QIcon(os.path.join(os.path.dirname(__file__), "reload-conf.png")),
      u"Configure",
      self.iface.mainWindow()
    )
    self.iface.registerMainWindowAction(self.actionConfigure, "Shift+F5")
    self.actionConfigure.setWhatsThis(u"Choose a plugin to be reloaded")
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
      reloadPlugin(plugin)
      self.iface.mainWindow().restoreState(state)
      self.iface.messageBar().pushMessage("<b>%s</b> reloaded." % plugin, QGis.Info)

  def configure(self):
    dlg = ConfigureReloaderDialog(self.iface)
    dlg.exec_()
    if dlg.result():
      plugin = dlg.comboPlugin.currentText()
      settings = QSettings()
      self.actionRun.setWhatsThis(u"Reload plugin: %s" % plugin)
      self.actionRun.setText(u"Reload plugin: %s" % plugin)
      settings.setValue('/PluginReloader/plugin', plugin)
