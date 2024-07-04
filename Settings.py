"""Python Plugin Reloader for QGIS: Reloader's settings.

    begin                : 2024-07-04
    copyright            : (C) 2024 by Borys Jurgiel
    email                : qgis at borysjurgiel dot pl
    The "Reload" icon copyright by Matt Ball http://www.mattballdesign.com

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
"""

from qgis.PyQt.QtCore import QSettings


class Settings():
    """A helper class for handling reloader's all QSettings."""

    PREFIX = '/PluginReloader'
    """QSettings branch used by the plugin"""

    @classmethod
    def currentPlugin(cls) -> str:
        """Plugin to be reloaded, The.

        NOTE: Pylint doesn't allow to start method docstrings with 'the' ;)
        """
        return QSettings().value(f'{cls.PREFIX}/plugin', '', type=str)

    @classmethod
    def setCurrentPlugin(cls, plugin: str):
        """Set the plugin to be reloaded."""
        QSettings().setValue(f'{cls.PREFIX}/plugin', plugin)

    @classmethod
    def notificationsEnabled(cls) -> bool:
        """Whether plugin reload confirmaion message is enabled."""
        return QSettings().value(f'{cls.PREFIX}/notify', True, type=bool)

    @classmethod
    def setNotificationsEnabled(cls, enabled: bool):
        """Enable or disable plugin reload confirmaion message."""
        QSettings().setValue(f'{cls.PREFIX}/notify', enabled)

    @classmethod
    def extraCommandsEnabled(cls) -> bool:
        """Whether CLI command execution before plugin reload is enabled."""
        return QSettings().value(f'{cls.PREFIX}/extraCommandsEnabled', True,
                                 type=bool)

    @classmethod
    def setExtraCommandsEnabled(cls, enabled: bool):
        """Enable or disable CLI command execution prior to plugin reload."""
        QSettings().setValue(f'{cls.PREFIX}/extraCommandsEnabled', enabled)

    @classmethod
    def getExtraCommands(cls) -> str:
        """CLI commands to be executed prior to the plugin reload."""
        return QSettings().value(f'{cls.PREFIX}/extraCommands', '')

    @classmethod
    def setExtraCommands(cls, commands: str):
        """Set CLI commands to be executed prior to the plugin reload."""
        QSettings().setValue(f'{cls.PREFIX}/extraCommands', commands)
