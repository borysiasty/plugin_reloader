<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="fr" sourcelanguage="en">
<context>
    <name>ConfigurationDialogBase</name>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="30"/>
        <source>Configure Plugin reloader</source>
        <translation>Configurer Plugin Reloader</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="148"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Push a notification about the successful reload to the QGIS message bar.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Check this&lt;/span&gt;, if you like to be sure you reloaded the right plugin.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Uncheck this&lt;/span&gt;, if you hate trivial notifications covering error messages from the plugin.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Affiche une notification à propos du rechargement dans la barre de message de QGIS.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Cochez&lt;/span&gt;, si vous aimez être certain que vous avez rechargé la bonne extension.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Décochez&lt;/span&gt;, si vous détestez les notifications triviales masquant les messages d&apos;erreur de l&apos;extension.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="151"/>
        <source>Display a notification once the plugin is reloaded</source>
        <translation>Afficher une notification une fois l&apos;extension rechargée</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="197"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;QGIS will try to execute any commands typed here in a shell before reloading the plugin.&lt;/p&gt;
&lt;p&gt;This can be useful, for example, if you need to copy the new source code into the QGIS plugins directory.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;QGIS exécutera dans une interface système (shell) toute commandes inscrite ici avant de recharger l&apos;extension.&lt;/p&gt;
&lt;p&gt;Ceci peut être utile si, par exemple, vous souhaitez effectuer une copie de votre nouveau code source dans le répertoire d&apos;extensions de QGIS.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="74"/>
        <source>Note: any %PluginName% will be replaced by the plugin&apos;s name.</source>
        <translation>Note: tout %PluginName% sera remplacé par le nom de l&apos;extension.</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="86"/>
        <source>Select &amp;the plugin you want to reload</source>
        <translation>Sélec&amp;tionnez l&apos;extension à recharger</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="201"/>
        <source>Run the commands below before reloading</source>
        <translation>Exécuter les commandes ci-dessous avant le rechargement</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="169"/>
        <source>Number of recent plugins in the menu</source>
        <translation>Nombre d&apos;extensions récentes dans le menu</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="92"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-style:italic;color:red&quot;&gt;
This section is deprecated. Use the new drop-down menu in the toolbar instead.
&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-style:italic;color:red&quot;&gt;
Cette section est dépréciée. Utilisez le nouveau menu déroulant dans la barre d&apos;outils.
&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="166"/>
        <source>Maximum number of entries in the drop-down menu</source>
        <translation>Nombre maximum d&apos;entrées dans le menu déroulant</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="208"/>
        <source>Display description with the current plugin name beside the icon in the Plugin toolbar.</source>
        <translation>Afficher la description avec le nom de l&apos;extension actuelle à côté de l&apos;icône dans la barre d&apos;outils de l&apos;extension.</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="211"/>
        <source>Display the plugin name in the toolbar</source>
        <translation>Afficher le nom de l&apos;extension dans la barre d&apos;outils</translation>
    </message>
</context>
<context>
    <name>Plugin</name>
    <message>
        <location filename="../Plugin.py" line="104"/>
        <source>Reload plugin: </source>
        <translation type="obsolete">Recharger l&apos;extension: </translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="214"/>
        <source>Reload plugin: {}</source>
        <translation>Recharger l&apos;extension: {}</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="99"/>
        <source>&amp;Plugin Reloader</source>
        <translation>&amp;Plugin Reloader</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="133"/>
        <source>Configure</source>
        <translation>Configurer</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="256"/>
        <source>Plugin &lt;b&gt;{}&lt;/b&gt; not found.</source>
        <translation>Extension &lt;b&gt;{}&lt;/b&gt; introuvable.</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="342"/>
        <source>&lt;b&gt;{}&lt;/b&gt; reloaded in {} ms.</source>
        <translation>&lt;b&gt;{}&lt;/b&gt; rechargé en {} ms.</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="382"/>
        <source>Could not execute extra commands: {}</source>
        <translation>Impossible d&apos;exécuter des commandes supplémentaires : {}</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="126"/>
        <source>Reload a plugin...</source>
        <translation>Recharger l&apos;extension...</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="113"/>
        <source>Reload recent plugin</source>
        <translation>Recharger l&apos;extension récente</translation>
    </message>
</context>
<context>
    <name>PluginSelectionDialogBase</name>
    <message>
        <location filename="../PluginSelectionDialogBase.ui" line="30"/>
        <source>Reload a plugin</source>
        <translation>Recharger l&apos;extension</translation>
    </message>
    <message>
        <location filename="../PluginSelectionDialogBase.ui" line="52"/>
        <source>Select &amp;the plugin you want to reload</source>
        <translation>Sélec&amp;tionnez l&apos;extension à recharger</translation>
    </message>
</context>
</TS>
