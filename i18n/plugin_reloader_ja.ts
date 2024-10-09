<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="ja_JP">
<context>
    <name>ConfigurationDialogBase</name>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="30"/>
        <source>Configure Plugin reloader</source>
        <translation>プラグインリローダを設定</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="148"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Push a notification about the successful reload to the QGIS message bar.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Check this&lt;/span&gt;, if you like to be sure you reloaded the right plugin.&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Uncheck this&lt;/span&gt;, if you hate trivial notifications covering error messages from the plugin.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;リロード成功時に QGIS メッセージバーにプッシュ通信する。&lt;/p&gt;&lt;p&gt;リロードするプラグインを確認する場合に&lt;span style=&quot; font-weight:600;&quot;&gt;これをチェック&lt;/span&gt;。&lt;/p&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Uncheck this&lt;/span&gt;プラグインからの些細なエラーメッセージが嫌いな場合は&lt;span style=&quot; font-weight:600;&quot;&gt;チェックを外す&lt;/span&gt;。&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="151"/>
        <source>Display a notification once the plugin is reloaded</source>
        <translation>プラグインがリロードされた際に通知</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="197"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;QGIS will try to execute any commands typed here in a shell before reloading the plugin.&lt;/p&gt;
&lt;p&gt;This can be useful, for example, if you need to copy the new source code into the QGIS plugins directory.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;QGIS は、プラグインをリロードする前に以下のコマンドをシェルで実行します。&lt;/p&gt;
&lt;p&gt;これは、例えば新しいソースをプラグインフォルダにコピーするなどのことができます。&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="74"/>
        <source>Note: any %PluginName% will be replaced by the plugin&apos;s name.</source>
        <translation>注: %PluginName% はプラグイン名に置換されます。</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="86"/>
        <source>Select &amp;the plugin you want to reload</source>
        <translation>&amp;T リロードしたいプラグインを選択</translation>
    </message>
    <message>
        <location filename="../ConfigurationDialogBase.ui" line="201"/>
        <source>Run the commands below before reloading</source>
        <translation>リロード前に以下のコマンドを実行</translation>
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
        <translation type="obsolete">プラグインをリロード: </translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="214"/>
        <source>Reload plugin: {}</source>
        <translation>プラグインをリロード: {}</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="99"/>
        <source>&amp;Plugin Reloader</source>
        <translation>&amp;P プラグイン リローダ</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="133"/>
        <source>Configure</source>
        <translation>設定</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="256"/>
        <source>Plugin &lt;b&gt;{}&lt;/b&gt; not found.</source>
        <translation>プラグイン &lt;b&gt;{}&lt;/b&gt; が見つかりませんでした。</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="342"/>
        <source>&lt;b&gt;{}&lt;/b&gt; reloaded in {} ms.</source>
        <translation>&lt;b&gt;{}&lt;/b&gt; は {} ms でリロードされました。</translation>
    </message>
    <message>
        <location filename="../Plugin.py" line="382"/>
        <source>Could not execute extra commands: {}</source>
        <translation>追加コマンドを実行できませんした: {}</translation>
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
        <translation type="unfinished">&amp;T リロードしたいプラグインを選択</translation>
    </message>
</context>
</TS>
