# -*- coding: utf-8 -*-
# ***************************************************************************
# __init__.py  -  A Python Plugin Reloader for QGIS
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

def name():
  return "Plugin reloader"

def version():
  return "Version 0.6.3"

def description():
  return "Reloads a chosen plugin in one click (only useful for Python Plugin Developers)"

def qgisMinimumVersion():
  return "1.5"

def experimental():
  return True

def author():
  return "Borys Jurgiel"

def authorName():
  return author()

def email():
  return "qgis at borysjurgiel dot pl"


def classFactory(iface):
  from reloader_plugin import ReloaderPlugin
  return ReloaderPlugin(iface)
