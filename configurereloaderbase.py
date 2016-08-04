# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configurereloaderbase.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.gridLayout_2 = QtWidgets.QGridLayout(ConfigureReloaderDialogBase)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfigureReloaderDialogBase)
        self.buttonBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.comboPlugin = QtWidgets.QComboBox(ConfigureReloaderDialogBase)
        self.comboPlugin.setMinimumSize(QtCore.QSize(220, 0))
        self.comboPlugin.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboPlugin.setObjectName("comboPlugin")
        self.gridLayout_2.addWidget(self.comboPlugin, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(ConfigureReloaderDialogBase)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.label.setBuddy(self.comboPlugin)

        self.retranslateUi(ConfigureReloaderDialogBase)
        self.buttonBox.accepted.connect(ConfigureReloaderDialogBase.accept)
        self.buttonBox.rejected.connect(ConfigureReloaderDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureReloaderDialogBase)

    def retranslateUi(self, ConfigureReloaderDialogBase):
        _translate = QtCore.QCoreApplication.translate
        ConfigureReloaderDialogBase.setWindowTitle(_translate("ConfigureReloaderDialogBase", "Configure Plugin reloader"))
        self.label.setText(_translate("ConfigureReloaderDialogBase", " Select the plugin you want to reload"))

from . import resources_rc
