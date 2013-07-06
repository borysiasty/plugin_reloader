# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configurereloaderbase.ui'
#
# Created: Sat Aug 21 00:27:45 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ConfigureReloaderDialogBase(object):
    def setupUi(self, ConfigureReloaderDialogBase):
        ConfigureReloaderDialogBase.setObjectName("ConfigureReloaderDialogBase")
        ConfigureReloaderDialogBase.resize(314, 123)
        ConfigureReloaderDialogBase.setMaximumSize(QtCore.QSize(350, 150))
        ConfigureReloaderDialogBase.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/plugin_reloader/reload-conf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConfigureReloaderDialogBase.setWindowIcon(icon)
        ConfigureReloaderDialogBase.setWhatsThis("")
        self.gridLayout_2 = QtGui.QGridLayout(ConfigureReloaderDialogBase)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureReloaderDialogBase)
        self.buttonBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.comboPlugin = QtGui.QComboBox(ConfigureReloaderDialogBase)
        self.comboPlugin.setMinimumSize(QtCore.QSize(220, 0))
        self.comboPlugin.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboPlugin.setObjectName("comboPlugin")
        self.gridLayout_2.addWidget(self.comboPlugin, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 4, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        self.label = QtGui.QLabel(ConfigureReloaderDialogBase)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.label.setBuddy(self.comboPlugin)

        self.retranslateUi(ConfigureReloaderDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureReloaderDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureReloaderDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureReloaderDialogBase)

    def retranslateUi(self, ConfigureReloaderDialogBase):
        ConfigureReloaderDialogBase.setWindowTitle(QtGui.QApplication.translate("ConfigureReloaderDialogBase", "Configure Plugin reloader", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ConfigureReloaderDialogBase", " Select the plugin you want to reload", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
