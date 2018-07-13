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

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import QGis
from qgis.utils import plugins, reloadPlugin, updateAvailablePlugins, loadPlugin, startPlugin
from configurereloaderbase import Ui_ConfigureReloaderDialogBase
import resources_rc


if QGis.QGIS_VERSION_INT >= 10900:
    SIPv2 = True
else:
    SIPv2 = False


def currentPlugin():
    settings = QSettings()
    if SIPv2:
      return unicode(settings.value('/PluginReloader/plugin', '', type=str))
    else:
      return unicode(settings.value('/PluginReloader/plugin', QVariant('')).toString())


class ConfigureReloaderDialog (QDialog, Ui_ConfigureReloaderDialogBase):
  def __init__(self, parent):
    QDialog.__init__(self)
    self.iface = parent
    self.setupUi(self)
    self.plugins = plugins.keys()
    self.plugins.sort()
    #update the plugin list first! The plugin could be removed from the list if was temporarily broken.
    #Still doesn't work in every case. TODO?: try to load from scratch the plugin saved in QSettings if doesn't exist
    plugin = currentPlugin()
    updateAvailablePlugins()
    #if not plugins.has_key(plugin):
      #try:
        #loadPlugin(plugin)
        #startPlugin(plugin)
      #except:
        #pass
    #updateAvailablePlugins()

    for plugin in self.plugins:
      self.comboPlugin.addItem(plugin)
    plugin = currentPlugin()
    if plugins.has_key(plugin):
      self.comboPlugin.setCurrentIndex(self.plugins.index(plugin))



class ReloaderPlugin():
  def __init__(self, iface):
    self.iface = iface
    self.toolButton = QToolButton()
    self.toolButton.setMenu(QMenu())
    self.toolButton.setPopupMode(QToolButton.MenuButtonPopup)
    self.iface.addToolBarWidget(self.toolButton)


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
      QIcon(":/plugins/plugin_reloader/reload.png"), 
      u"Reload chosen plugin", 
      self.iface.mainWindow()
    )
    self.actionRun.setWhatsThis(u"Reload chosen plugin")
    plugin = currentPlugin()
    if plugin:
      self.actionRun.setWhatsThis(u"Reload plugin: %s" % plugin)
      self.actionRun.setText(u"Reload plugin: %s" % plugin)
    self.iface.addPluginToMenu("&Plugin Reloader", self.actionRun)
    self.iface.registerMainWindowAction(self.actionRun, self.theBestShortcutForPluginReload())
    m = self.toolButton.menu()
    m.addAction(self.actionRun)
    self.toolButton.setDefaultAction(self.actionRun)
    QObject.connect(self.actionRun, SIGNAL("triggered()"), self.run)
    self.actionConfigure = QAction(
      QIcon(":/plugins/plugin_reloader/reload-conf.png"), 
      u"Choose a plugin to be reloaded", 
      self.iface.mainWindow()
    )
    self.iface.registerMainWindowAction(self.actionConfigure, "Shift+F5")
    self.actionConfigure.setWhatsThis(u"Choose a plugin to be reloaded")
    m.addAction(self.actionConfigure)
    self.iface.addPluginToMenu("&Plugin Reloader", self.actionConfigure)
    QObject.connect(self.actionConfigure, SIGNAL("triggered()"), self.configure)


  def unload(self):
    self.iface.removePluginMenu("&Plugin Reloader",self.actionRun)
    self.iface.removePluginMenu("&Plugin Reloader",self.actionConfigure)
    self.iface.removeToolBarIcon(self.actionRun)
    self.iface.removeToolBarIcon(self.actionConfigure)
    self.iface.unregisterMainWindowAction(self.actionRun)
    self.iface.unregisterMainWindowAction(self.actionConfigure)


  def run(self):
    plugin = currentPlugin()
    #update the plugin list first! The plugin could be removed from the list if was temporarily broken.
    updateAvailablePlugins()
    #try to load from scratch the plugin saved in QSettings if not loaded
    if not plugins.has_key(plugin):
      try:
        loadPlugin(plugin)
        startPlugin(plugin)
      except:
        pass
    updateAvailablePlugins()
    #give one chance for correct (not a loop)
    if not plugins.has_key(plugin):
      self.configure()
      plugin = currentPlugin()
    if plugins.has_key(plugin):
      state = self.iface.mainWindow().saveState()
      reloadPlugin(plugin)
      self.iface.mainWindow().restoreState(state)


  def configure(self):
    dlg = ConfigureReloaderDialog(self.iface)
    dlg.exec_()
    if dlg.result():
      plugin = dlg.comboPlugin.currentText()
      settings = QSettings()
      if SIPv2:
        settings.setValue('/PluginReloader/plugin', plugin)
      else:
        settings.setValue('/PluginReloader/plugin', QVariant(plugin))
      self.actionRun.setWhatsThis(u"Reload plugin: %s" % plugin)
      self.actionRun.setText(u"Reload plugin: %s" % plugin)
    # call the reloading immediately - note that it may cause a loop!!
    #self.run()
