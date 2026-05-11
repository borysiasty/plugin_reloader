<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="ja_JP">
  <context>
    <name>ConfigurationDialogBase</name>
    <message>
      <location filename="../ConfigurationDialogBase.ui" line="0" />
      <source>Configure Plugin reloader</source>
      <translation>プラグインリローダを設定</translation>
    </message>
    <message>
      <location filename="../ConfigurationDialogBase.ui" line="0" />
      <location filename="../ConfigurationDialogBase.ui" line="0" />
      <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;QGIS will try to execute any commands typed here in a shell before reloading the plugin.&lt;/p&gt;
&lt;p&gt;This can be useful, for example, if you need to copy the new source code into the QGIS plugins directory.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
      <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;QGIS は、プラグインをリロードする前に以下のコマンドをシェルで実行します。&lt;/p&gt;
&lt;p&gt;これは、例えば新しいソースをプラグインフォルダにコピーするなどのことができます。&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
      <location filename="../ConfigurationDialogBase.ui" line="0" />
      <source>Note: any %PluginName% will be replaced by the plugin's name.</source>
      <translation>注: %PluginName% はプラグイン名に置換されます。</translation>
    </message>
    <message>
      <location filename="../ConfigurationDialogBase.ui" line="0" />
      <source>Select &amp;the plugin you want to reload</source>
      <translation>&amp;T リロードしたいプラグインを選択</translation>
    </message>
    <message>
      <location filename="../ConfigurationDialogBase.ui" line="0" />
      <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=" font-style:italic;color:red"&gt;
This section is deprecated. Use the new drop-down menu in the toolbar instead.
&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
      <translation type="unfinished" />
    </message>
    <message>
      <location filename="../ConfigurationDialogBase.ui" line="0" />
      <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Push a notification about the successful reload to the QGIS message bar.&lt;/p&gt;&lt;p&gt;&lt;span style=" font-weight:600;"&gt;Check this&lt;/span&gt;, if you like to be sure you reloaded the right plugin.&lt;/p&gt;&lt;p&gt;&lt;span style=" font-weight:600;"&gt;Uncheck this&lt;/span&gt;, if you hate trivial notifications covering error messages from the plugin.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
      <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;リロード成功時に QGIS メッセージバーにプッシュ通信する。&lt;/p&gt;&lt;p&gt;リロードするプラグインを確認する場合に&lt;span style=" font-weight:600;"&gt;これをチェック&lt;/span&gt;。&lt;/p&gt;&lt;p&gt;&lt;span style=" font-weight:600;"&gt;Uncheck this&lt;/span&gt;プラグインからの些細なエラーメッセージが嫌いな場合は&lt;span style=" font-weight:600;"&gt;チェックを外す&lt;/span&gt;。&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
      <location filename="../ConfigurationDialogBase.ui" line="0" />
      <source>Display a notification once the plugin is reloaded</source>
      <translation>プラグインがリロードされた際に通知</translation>
    </message>
    <message>
      <location filename="../ConfigurationDialogBase.ui" line="0" />
      <source>Maximum number of entries in the drop-down menu</source>
      <translation type="unfinished" />
    </message>
    <message>
      <location filename="../ConfigurationDialogBase.ui" line="0" />
      <source>Number of recent plugins in the menu</source>
      <translation type="unfinished" />
    </message>
    <message>
      <location filename="../ConfigurationDialogBase.ui" line="0" />
      <source>Run the commands below before reloading</source>
      <translation>リロード前に以下のコマンドを実行</translation>
    </message>
    <message>
      <location filename="../ConfigurationDialogBase.ui" line="0" />
      <source>Display description with the current plugin name beside the icon in the Plugin toolbar.</source>
      <translation type="unfinished" />
    </message>
    <message>
      <location filename="../ConfigurationDialogBase.ui" line="0" />
      <source>Display the plugin name in the toolbar</source>
      <translation type="unfinished" />
    </message>
  </context>
  <context>
    <name>Plugin</name>
    <message>
      <location filename="../Plugin.py" line="88" />
      <source>&amp;Plugin Reloader</source>
      <translation>&amp;P プラグイン リローダ</translation>
    </message>
    <message>
      <location filename="../Plugin.py" line="103" />
      <source>Reload recent plugin</source>
      <translation type="unfinished" />
    </message>
    <message>
      <location filename="../Plugin.py" line="117" />
      <source>Reload a plugin...</source>
      <translation type="unfinished" />
    </message>
    <message>
      <location filename="../Plugin.py" line="124" />
      <source>Configure</source>
      <translation>設定</translation>
    </message>
    <message>
      <location filename="../Plugin.py" line="168" />
      <source>Reload plugin: {}</source>
      <translation>プラグインをリロード: {}</translation>
    </message>
    <message>
      <location filename="../Plugin.py" line="285" />
      <source>Plugin &lt;b&gt;{}&lt;/b&gt; not found.</source>
      <translation>プラグイン &lt;b&gt;{}&lt;/b&gt; が見つかりませんでした。</translation>
    </message>
    <message>
      <location filename="../Plugin.py" line="391" />
      <source>&lt;b&gt;{}&lt;/b&gt; reloaded in {} ms.</source>
      <translation>&lt;b&gt;{}&lt;/b&gt; は {} ms でリロードされました。</translation>
    </message>
    <message>
      <location filename="../Plugin.py" line="394" />
      <source> &lt;b&gt;WARNING&lt;/b&gt;: removing duplicated widget(s) not cleaned up by the plugin during unload: &lt;b&gt;{}&lt;/b&gt;.</source>
      <translation type="unfinished" />
    </message>
    <message>
      <location filename="../Plugin.py" line="472" />
      <source>Could not execute extra commands: {}</source>
      <translation>追加コマンドを実行できませんした: {}</translation>
    </message>
    <message>
      <source>Reload plugin: </source>
      <translation type="vanished">プラグインをリロード: </translation>
    </message>
  </context>
  <context>
    <name>PluginSelectionDialogBase</name>
    <message>
      <location filename="../PluginSelectionDialogBase.ui" line="0" />
      <source>Reload a plugin</source>
      <translation type="unfinished" />
    </message>
    <message>
      <location filename="../PluginSelectionDialogBase.ui" line="0" />
      <source>Select &amp;the plugin you want to reload</source>
      <translation type="unfinished">&amp;T リロードしたいプラグインを選択</translation>
    </message>
  </context>
</TS>
