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

from qgis.PyQt.QtCore import Qt, QSettings


class Settings():
    """A helper class for handling reloader's all QSettings."""

    PREFIX = '/PluginReloader'
    """QSettings branch used by the plugin"""

    DEFAULT_RECENT_PLUGINS_COUNT = 5

    @classmethod
    def recentPlugins(cls, listAll: bool = False) -> list[str]:
        """Recently used plugins. The most recent first.

        :param listAll: List all stored plugins instead of cropping
                        to the currently configured number.
        """
        if plugins := QSettings().value(f'{cls.PREFIX}/recentPlugins', '',
                                        type=str):
            plugins = [plugin.strip() for plugin in plugins]
        else:
            # Fallback to the old setting
            currentPlugin = QSettings().value(f'{cls.PREFIX}/plugin', type=str)
            plugins = [currentPlugin] if currentPlugin else []

        if not listAll:
            plugins = plugins[:cls.recentPluginsCount()]
        return plugins

    @classmethod
    def updateRecentPlugins(cls, recentPlugin: str):
        """Set the recently reloaded plugin list. The most recent first."""
        plugins = cls.recentPlugins()
        if recentPlugin in plugins:
            plugins.remove(recentPlugin)
        plugins = [recentPlugin] + plugins
        plugins = plugins[:cls.recentPluginsCount()]
        QSettings().setValue(f'{cls.PREFIX}/recentPlugins', plugins)

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
        return QSettings().value(f'{cls.PREFIX}/extraCommandsEnabled', False,
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

    @classmethod
    def recentPluginsCount(cls) -> int:
        """Get the number of recent plugins to display in the menu."""
        return QSettings().value(f'{cls.PREFIX}/recentPluginsCount',
                                 cls.DEFAULT_RECENT_PLUGINS_COUNT,
                                 type=int)

    @classmethod
    def setRecentPluginsCount(cls, count: int):
        """Set number of recent plugins to display in the menu."""
        QSettings().setValue(f'{cls.PREFIX}/recentPluginsCount', count)

    @classmethod
    def toolButtonStyle(cls) -> Qt.ToolButtonStyle:
        """Get toolbar button style (with text or icon only)."""
        if cls.toolButtonTextEnabled():
            buttonStyle = Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        else:
            buttonStyle = Qt.ToolButtonStyle.ToolButtonIconOnly
        return buttonStyle

    @classmethod
    def toolButtonTextEnabled(cls) -> bool:
        """Whether to display text beside the toolbar icon."""
        return QSettings().value(f'{cls.PREFIX}/toolButtonTextEnabled',
                                 True, type=bool)

    @classmethod
    def setToolButtonTextEnabled(cls, state: bool):
        """Enable or disable text displayed beside the toolbar icon."""
        QSettings().setValue(f'{cls.PREFIX}/toolButtonTextEnabled', state)
