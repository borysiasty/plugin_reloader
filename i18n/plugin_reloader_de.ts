<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="de_DE">
<context>
    <name>ConfigurationDialogBase</name>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="30"/>
        <source>Configure Plugin reloader</source>
        <translation>Plugin-Reloader-Einstellungen</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="151"/>
        <source>Display a notification once the plugin is reloaded</source>
        <translation>Benachrichtigung anzeigen, sobald das Plugin neu geladen wurde</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="86"/>
        <source>Select &amp;the plugin you want to reload</source>
        <translation>Selek&amp;tion des neu zu ladenden Plugins</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="197"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;QGIS will try to execute any commands typed here in a shell before reloading the plugin.&lt;/p&gt;
&lt;p&gt;This can be useful, for example, if you need to copy the new source code into the QGIS plugins directory.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;QGIS wird versuchen, alle hier eingegebenen Befehle in einer Shell auszuführen, bevor das Plugin neu geladen wird.&lt;/p&gt;
&lt;p&gt;Dies kann nützlich sein, wenn der neue Quellcode in das QGIS-Plugin-Verzeichnis kopiert werden muss.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="148"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Push a notification about the successful reload to the QGIS message bar.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Check this&lt;/span&gt;, if you like to be sure you reloaded the right plugin.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Uncheck this&lt;/span&gt;, if you hate trivial notifications covering error messages from the plugin.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Sende eine Benachrichtigung über das erfolgreiche Neuladen an die QGIS-Nachrichtenleiste.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Aktiviere&lt;/span&gt; diese Option,um zu überprüfen ob das richtige Plugin neu geladen wurde.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Deaktiviere&lt;/span&gt; diese Option, wenn triviale Benachrichtigungen zu Fehlermeldungen des Plugins nicht angezeigt werden sollen.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="74"/>
        <source>Note: any %PluginName% will be replaced by the plugin&apos;s name.</source>
        <translation>Bemerkung: %PluginName% wird ersetzt durch den Plugin Namen.</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="201"/>
        <source>Run the commands below before reloading</source>
        <translation>Befehle, die vor dem Neuladen ausgeführt werden sollen</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="169"/>
        <source>Number of recent plugins in the menu</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="92"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-style:italic;color:red&quot;&gt;
This section is deprecated. Use the new drop-down menu in the toolbar instead.
&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="166"/>
        <source>Maximum number of entries in the drop-down menu</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="208"/>
        <source>Display description with the current plugin name beside the icon in the Plugin toolbar.</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="211"/>
        <source>Display the plugin name in the toolbar</source>
        <translation type="unfinished"></translation>
    </message>
</context>
<context>
    <name>Plugin</name>
    <message>
        <location filename="../Plugin.py" line="104"/>
        <source>Reload plugin: </source>
        <translation type="obsolete">Plugin neu laden: </translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="214"/>
        <source>Reload plugin: {}</source>
        <translation>Plugin neu laden: {}</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="99"/>
        <source>&amp;Plugin Reloader</source>
        <translation>&amp;Plugin-Reloader</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="133"/>
        <source>Configure</source>
        <translation>Konfigurieren</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="256"/>
        <source>Plugin &lt;b&gt;{}&lt;/b&gt; not found.</source>
        <translation>Plugin &lt;b&gt;{}&lt;/b&gt; nicht gefunden.</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="342"/>
        <source>&lt;b&gt;{}&lt;/b&gt; reloaded in {} ms.</source>
        <translation>&lt;b&gt;{}&lt;/b&gt; neu geladen in {} ms.</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="382"/>
        <source>Could not execute extra commands: {}</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="126"/>
        <source>Reload a plugin...</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="113"/>
        <source>Reload recent plugin</source>
        <translation type="unfinished"></translation>
    </message>
</context>
<context>
    <name>PluginSelectionDialogBase</name>
    <message>
        <location filename="../PluginSelectionDialogBase.ui" line="30"/>
        <source>Reload a plugin</source>
        <translation type="unfinished"></translation>
    </message>
    <message>
        <location filename="../PluginSelectionDialogBase.ui" line="52"/>
        <source>Select &amp;the plugin you want to reload</source>
        <translation type="unfinished">Selek&amp;tion des neu zu ladenden Plugins</translation>
    </message>
</context>
</TS>
