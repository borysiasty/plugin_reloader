<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="pl_PL">
<context>
    <name>ConfigurationDialogBase</name>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="0"/>
        <source>Configure Plugin reloader</source>
        <translation>Konfiguracja Plugin Reloadera</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="0"/>
        <location filename="../ConfigurationDialogBase.ui" line="0"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;QGIS will try to execute any commands typed here in a shell before reloading the plugin.&lt;/p&gt;
&lt;p&gt;This can be useful, for example, if you need to copy the new source code into the QGIS plugins directory.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Wprowadź komendy wiersza poleceń, które mają być wykonane przed przeładowaniem wtyczki.&lt;/p&gt;
&lt;p&gt;Może to być na przykład kopiowanie kodu źródłowego wtyczki z katalogu roboczego do katalogu wtyczek QGIS.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="0"/>
        <source>Note: any %PluginName% will be replaced by the plugin&apos;s name.</source>
        <translation>Możesz użyć zmiennej %PluginName% zamiast nazwy wtyczki.</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="0"/>
        <source>Select &amp;the plugin you want to reload</source>
        <translation>Wybierz &amp;wtyczkę do przeładowania</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="0"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-style:italic;color:red&quot;&gt;
This section is deprecated. Use the new drop-down menu in the toolbar instead.
&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-style:italic;color:red&quot;&gt;
Ta sekcja została wyłączona. Wybieraj wtyczki z nowego rozwijalnego menu w pasku narzędzi.
&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="0"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Push a notification about the successful reload to the QGIS message bar.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Check this&lt;/span&gt;, if you like to be sure you reloaded the right plugin.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Uncheck this&lt;/span&gt;, if you hate trivial notifications covering error messages from the plugin.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Wyświetlaj potwierdzenie przeładowania wtyczki w pasku powiadomień QGIS-a.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Zaznacz&lt;/span&gt;, jeśli chcesz mieć pewność, że przeładowujesz właściwą wtyczkę.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Odznacz&lt;/span&gt;, jeśli wolisz mniej powiadomień.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="0"/>
        <source>Display a notification once the plugin is reloaded</source>
        <translation>Wyświetlaj powiadomienie o przeładowaniu wtyczki</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="0"/>
        <source>Maximum number of entries in the drop-down menu</source>
        <translation>Maksymalna liczba wpisów w menu rozwijalnym</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="0"/>
        <source>Number of recent plugins in the menu</source>
        <translation>Liczba ostatnio przeładowanych wtyczek w menu</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="0"/>
        <source>Run the commands below before reloading</source>
        <translation>Uruchom poniższe polecenia przed przeładowaniem</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="0"/>
        <source>Display description with the current plugin name beside the icon in the Plugin toolbar.</source>
        <translation>Wyświetlaj opis z nazwą aktualnie wybranej wtyczki obok ikony na pasku narzędzi.</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="0"/>
        <source>Display the plugin name in the toolbar</source>
        <translation>Wyświetlaj nazwę wtyczki na pasku narzędzi</translation>
    </message>
</context>
<context>
    <name>Plugin</name>
    <message>
        <location filename="../Plugin.py" line="88"/>
        <source>&amp;Plugin Reloader</source>
        <translation>&amp;Plugin Reloader</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="103"/>
        <source>Reload recent plugin</source>
        <translation>Przeładuj ostatnią wtyczkę</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="117"/>
        <source>Reload a plugin...</source>
        <translation>Przeładuj wtyczkę...</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="124"/>
        <source>Configure</source>
        <translation>Ustawienia</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="168"/>
        <source>Reload plugin: {}</source>
        <translation>Przeładuj wtyczkę: {}</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="285"/>
        <source>Plugin &lt;b&gt;{}&lt;/b&gt; not found.</source>
        <translation>Nie znaleziono wtyczki &lt;b&gt;{}&lt;/b&gt;.</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="391"/>
        <source>&lt;b&gt;{}&lt;/b&gt; reloaded in {} ms.</source>
        <translation>Wtyczka &lt;b&gt;{}&lt;/b&gt; przeładowana w {} ms.</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="394"/>
        <source> &lt;b&gt;WARNING&lt;/b&gt;: removing duplicated widget(s) not cleaned up by the plugin during unload: &lt;b&gt;{}&lt;/b&gt;.</source>
        <translation> &lt;b&gt;OSTRZEŻENIE&lt;/b&gt;: usuwam zduplikowane widgety pozostawione przez wtyczkę podczas wyłączania: &lt;b&gt;{}&lt;/b&gt;.</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="472"/>
        <source>Could not execute extra commands: {}</source>
        <translation>Nie mogę uruchomić polecenia przed przeładowaniem: {}</translation>
    </message>
</context>
<context>
    <name>PluginSelectionDialogBase</name>
    <message>
        <location filename="../PluginSelectionDialogBase.ui" line="0"/>
        <source>Reload a plugin</source>
        <translation>Przeładuj wtyczkę</translation>
    </message>
    <message>
        <location filename="../PluginSelectionDialogBase.ui" line="0"/>
        <source>Select &amp;the plugin you want to reload</source>
        <translation>Wybierz &amp;wtyczkę do przeładowania</translation>
    </message>
</context>
</TS>
