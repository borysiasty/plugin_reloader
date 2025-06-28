<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="es" sourcelanguage="en">
<context>
    <name>ConfigurationDialogBase</name>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="30"/>
        <source>Configure Plugin reloader</source>
        <translation>Configurar Plugin Reloader</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="148"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Push a notification about the successful reload to the QGIS message bar.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Check this&lt;/span&gt;, if you like to be sure you reloaded the right plugin.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Uncheck this&lt;/span&gt;, if you hate trivial notifications covering error messages from the plugin.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Mostrar una notificación sobre la recarga exitosa en la barra de mensajes de QGIS.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Marque esto&lt;/span&gt;, si desea estar seguro de que recargó el complemento correcto.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Desmarque esto&lt;/span&gt;, si odia las notificaciones triviales que cubren los mensajes de error del complemento.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="151"/>
        <source>Display a notification once the plugin is reloaded</source>
        <translation>Mostrar una notificación una vez que el complemento sea recargado</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="197"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;QGIS will try to execute any commands typed here in a shell before reloading the plugin.&lt;/p&gt;
&lt;p&gt;This can be useful, for example, if you need to copy the new source code into the QGIS plugins directory.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;QGIS intentará ejecutar cualquier comando escrito aquí en una terminal antes de recargar el complemento.&lt;/p&gt;
&lt;p&gt;Esto puede ser útil, por ejemplo, si necesita copiar el nuevo código fuente al directorio de complementos de QGIS.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="74"/>
        <source>Note: any %PluginName% will be replaced by the plugin&apos;s name.</source>
        <translation>Nota: cualquier %PluginName% será reemplazado por el nombre del complemento.</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="86"/>
        <source>Select &amp;the plugin you want to reload</source>
        <translation>Seleccione &amp;el complemento que desea recargar</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="201"/>
        <source>Run the commands below before reloading</source>
        <translation>Ejecutar los comandos de abajo antes de recargar</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="169"/>
        <source>Number of recent plugins in the menu</source>
        <translation>Número de complementos recientes en el menú</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="92"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-style:italic;color:red&quot;&gt;
This section is deprecated. Use the new drop-down menu in the toolbar instead.
&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-style:italic;color:red&quot;&gt;
Esta sección está obsoleta. Use el nuevo menú desplegable en la barra de herramientas en su lugar.
&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="166"/>
        <source>Maximum number of entries in the drop-down menu</source>
        <translation>Número máximo de entradas en el menú desplegable</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="208"/>
        <source>Display description with the current plugin name beside the icon in the Plugin toolbar.</source>
        <translation>Mostrar descripción con el nombre del complemento actual al lado del icono en la barra de herramientas de Complementos.</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="211"/>
        <source>Display the plugin name in the toolbar</source>
        <translation>Mostrar el nombre del complemento en la barra de herramientas</translation>
    </message>
</context>
<context>
    <name>Plugin</name>
    <message>
        <location filename="../Plugin.py" line="104"/>
        <source>Reload plugin: </source>
        <translation type="obsolete">Recargar complemento: </translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="214"/>
        <source>Reload plugin: {}</source>
        <translation>Recargar complemento: {}</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="99"/>
        <source>&amp;Plugin Reloader</source>
        <translation>&amp;Plugin Reloader</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="133"/>
        <source>Configure</source>
        <translation>Configurar</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="256"/>
        <source>Plugin &lt;b&gt;{}&lt;/b&gt; not found.</source>
        <translation>Complemento &lt;b&gt;{}&lt;/b&gt; no encontrado.</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="342"/>
        <source>&lt;b&gt;{}&lt;/b&gt; reloaded in {} ms.</source>
        <translation>&lt;b&gt;{}&lt;/b&gt; recargado en {} ms.</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="382"/>
        <source>Could not execute extra commands: {}</source>
        <translation>No se pudieron ejecutar comandos adicionales: {}</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="126"/>
        <source>Reload a plugin...</source>
        <translation>Recargar un complemento...</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="113"/>
        <source>Reload recent plugin</source>
        <translation>Recargar complemento reciente</translation>
    </message>
</context>
<context>
    <name>PluginSelectionDialogBase</name>
    <message>
        <location filename="../PluginSelectionDialogBase.ui" line="30"/>
        <source>Reload a plugin</source>
        <translation>Recargar un complemento</translation>
    </message>
    <message>
        <location filename="../PluginSelectionDialogBase.ui" line="52"/>
        <source>Select &amp;the plugin you want to reload</source>
        <translation>Seleccione &amp;el complemento que desea recargar</translation>
    </message>
</context>
</TS>