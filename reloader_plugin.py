# -*- coding: utf-8 -*-
# ***************************************************************************
# reloader_plugin.py  -  A Python Plugin Reloader for QGIS
# ---------------------
#     begin                : 2010-01-24
#     copyright            : (C) 2010 by Borys Jurgiel
#     email                : qgis at borysjurgiel dot pl
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
import subprocess
from time import time
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
from qgis.PyQt import uic
from qgis.core import Qgis
from qgis.utils import plugins, reloadPlugin, updateAvailablePlugins, unloadPlugin, loadPlugin, startPlugin
from pyplugin_installer import installer as plugin_installer

Ui_ConfigureReloaderDialogBase = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'configurereloaderbase.ui'))[0]

def currentPlugin():
    settings = QSettings()
    return unicode(settings.value('/PluginReloader/plugin', '', type=str))

def setCurrentPlugin(plugin):
    ''' param plugin (str): plugin dir (module name)
    '''
    settings = QSettings()
    settings.setValue('/PluginReloader/plugin', plugin)

def notificationsEnabled():
    settings = QSettings()
    return settings.value('/PluginReloader/notify', True, type=bool)

def getExtraCommands():
    settings = QSettings()
    return settings.value('/PluginReloader/extraCommands', '')

def setNotificationsEnabled(enabled):
    ''' param enabled (bool): Yes or no I'm asking?
    '''
    settings = QSettings()
    return settings.setValue('/PluginReloader/notify', enabled)

def extraCommandsEnabled():
    settings = QSettings()
    return settings.value('/PluginReloader/extraCommandsEnabled', True, type=bool)

def setExtraCommandsEnabled(enabled):
    settings = QSettings()
    return settings.setValue('/PluginReloader/extraCommandsEnabled', enabled)

def setExtraCommands(commands):
    settings = QSettings()
    return settings.setValue('/PluginReloader/extraCommands', commands)

def handleExtraCommands(message_bar, translator):
  try:
    extraCommands = getExtraCommands()
    if extraCommands.strip() != "":  # Prevent an empty command to be run
      extraCommands = extraCommands.replace('%PluginName%', currentPlugin())
      extraCommands = extraCommands.replace('%PluginPath%', plugin_installer.plugins.all()[currentPlugin()]['library'])

      completed_process = subprocess.run(
        extraCommands,
        shell=True,
        capture_output=True,
        check=True,
      )

      message_bar.pushMessage(
        completed_process.stdout.decode('utf-8', 'replace'),
        Qgis.Info
      )

    successExtraCommands = True

  except subprocess.CalledProcessError as exc:
    message_bar.pushMessage(
      translator('Could not execute extra commands: {}').format(exc.stderr.decode('utf-8', 'replace')),
      Qgis.Warning
    )
    successExtraCommands = False

  return successExtraCommands

class ConfigureReloaderDialog (QDialog, Ui_ConfigureReloaderDialogBase):
  def __init__(self, parent):
    super().__init__()
    self.iface = parent
    self.setupUi(self)
    self.cbNotifications.setChecked(notificationsEnabled())
    self.cbExtraCommands.setChecked(extraCommandsEnabled())
    self.pteExtraCommands.setPlainText(getExtraCommands())

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
    try:
      self.toolButton.setPopupMode(QToolButton.ToolButtonPopupMode.MenuButtonPopup)
    except AttributeError:
      # Just in case old (Py)Qt versions would not support it
      self.toolButton.setPopupMode(QToolButton.MenuButtonPopup)
    self.toolBtnAction = self.iface.addToolBarWidget(self.toolButton)

    if QSettings().value('locale/overrideFlag', type=bool):
        locale = QSettings().value('locale/userLocale')
    else:
        locale = QLocale.system().name()

    locale_path = os.path.join(
        os.path.dirname(__file__),
        'i18n',
        'plugin_reloader_{}.qm'.format(locale[0:2]))

    if os.path.exists(locale_path):
        self.translator = QTranslator()
        self.translator.load(locale_path)
        QCoreApplication.installTranslator(self.translator)

  def tr(self, message):
    return QCoreApplication.translate('ReloaderPlugin', message)

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
    keys = [key for key in settings.childKeys() if key.startswith(self.tr('Reload plugin: '))]
    if settings.contains(self.tr('Reload chosen plugin')):
        keys.append(self.tr('Reload chosen plugin'))
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
      self.tr('Reload chosen plugin'),
      self.iface.mainWindow()
    )
    self.actionRun.setToolTip(self.tr('Reload chosen plugin'))
    plugin = currentPlugin()
    if plugin:
      self.actionRun.setToolTip(self.tr('Reload plugin: {}').format(plugin))
      self.actionRun.setText(self.tr('Reload plugin: {}').format(plugin))
    self.iface.addPluginToMenu(self.tr('&Plugin Reloader'), self.actionRun)
    self.iface.registerMainWindowAction(self.actionRun, self.theBestShortcutForPluginReload())
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
    self.actionConfigure.setToolTip(self.tr('Choose a plugin to be reloaded'))
    m.addAction(self.actionConfigure)
    self.iface.addPluginToMenu(self.tr('&Plugin Reloader'), self.actionConfigure)
    self.actionConfigure.triggered.connect(self.configure)

  def unload(self):
    for action in [self.actionRun,self.actionConfigure]:
        self.iface.removePluginMenu(self.tr('&Plugin Reloader'),action)
        self.iface.removeToolBarIcon(action)
        self.iface.unregisterMainWindowAction(action)

    self.iface.removeToolBarIcon(self.toolBtnAction)

  def run(self):
    if len(plugin_installer.plugins.all()) == 0:
      plugin_installer.plugins.rebuild()

    if extraCommandsEnabled():
      successExtraCommands = handleExtraCommands(self.iface.messageBar(), self.tr)
      if not successExtraCommands:
        return

    plugin = currentPlugin()

    #update the plugin list first! The plugin could be removed from the list if was temporarily broken.
    updateAvailablePlugins()

    #try to load from scratch the plugin saved in QSettings if not loaded
    if plugin not in plugins and plugin != "":
      loadPlugin(plugin)
      startPlugin(plugin)
      updateAvailablePlugins()

    #give one chance for correct (not a loop)
    if plugin not in plugins:
      self.iface.messageBar().pushMessage(self.tr('Plugin <b>{}</b> not found.').format(plugin), Qgis.Warning, 0)
      self.configure()
      self.iface.messageBar().currentItem().dismiss()
      plugin = currentPlugin()

    if plugin in plugins:
      state = self.iface.mainWindow().saveState()

      # Unload submodules
      for key in [key for key in sys.modules.keys()]:
        if '{}.'.format(plugin) in key:
          if hasattr(sys.modules[key], 'qCleanupResources'):
            sys.modules[key].qCleanupResources()
          del sys.modules[key]

      # Reload plugin and check if it was successful.
      # Starting with QGIS 3.22, qgis.utils.reloadPlugin() returns True/False
      # but it returns nothing in prior versions. The function is
      # thus replicated for compatibility.
      startTime = time()
      unloadPlugin(plugin)
      loadPlugin(plugin)
      pluginStarted = startPlugin(plugin)
      endTime = time()

      self.iface.mainWindow().restoreState(state)
      if notificationsEnabled() and pluginStarted:
        # Not sure if we're more interested in the total time (a developer's business) or just qgis.utils.reloadPlugin
        # (to see how much a huge plugin slows down the QGIS start).
        duration = int(round((endTime - startTime) * 1000))
        self.iface.messageBar().pushMessage(
          self.tr('<b>{}</b> reloaded in {} ms.').format(plugin, duration),
          Qgis.Success
          )

  def configure(self):
    if len(plugin_installer.plugins.all()) == 0:
      plugin_installer.plugins.rebuild()

    dlg = ConfigureReloaderDialog(self.iface)
    dlg.exec()
    if dlg.result():
      plugin = dlg.comboPlugin.currentText()
      settings = QSettings()
      self.actionRun.setToolTip(self.tr('Reload plugin: {}').format(plugin))
      self.actionRun.setText(self.tr('Reload plugin: {}').format(plugin))
      setCurrentPlugin(plugin)
      setNotificationsEnabled(dlg.cbNotifications.isChecked())
      setExtraCommandsEnabled(dlg.cbExtraCommands.isChecked())
      setExtraCommands(dlg.pteExtraCommands.toPlainText())
