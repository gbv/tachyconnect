# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tachy_joystick.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(280, 315)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(280, 315))
        Dialog.setMaximumSize(QtCore.QSize(280, 315))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.joystickStop = QtWidgets.QPushButton(Dialog)
        self.joystickStop.setMinimumSize(QtCore.QSize(60, 60))
        self.joystickStop.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(25)
        font.setItalic(False)
        self.joystickStop.setFont(font)
        self.joystickStop.setObjectName("joystickStop")
        self.gridLayout.addWidget(self.joystickStop, 1, 1, 1, 1)
        self.joystickDown = QtWidgets.QPushButton(Dialog)
        self.joystickDown.setMinimumSize(QtCore.QSize(60, 60))
        self.joystickDown.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.joystickDown.setFont(font)
        self.joystickDown.setObjectName("joystickDown")
        self.gridLayout.addWidget(self.joystickDown, 2, 1, 1, 1)
        self.joystickLeft = QtWidgets.QPushButton(Dialog)
        self.joystickLeft.setMinimumSize(QtCore.QSize(60, 60))
        self.joystickLeft.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(25)
        self.joystickLeft.setFont(font)
        self.joystickLeft.setObjectName("joystickLeft")
        self.gridLayout.addWidget(self.joystickLeft, 1, 0, 1, 1)
        self.joystickRight = QtWidgets.QPushButton(Dialog)
        self.joystickRight.setMinimumSize(QtCore.QSize(60, 60))
        self.joystickRight.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(25)
        self.joystickRight.setFont(font)
        self.joystickRight.setObjectName("joystickRight")
        self.gridLayout.addWidget(self.joystickRight, 1, 2, 1, 1)
        self.joystickUp = QtWidgets.QPushButton(Dialog)
        self.joystickUp.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(25)
        self.joystickUp.setFont(font)
        self.joystickUp.setIconSize(QtCore.QSize(20, 20))
        self.joystickUp.setObjectName("joystickUp")
        self.gridLayout.addWidget(self.joystickUp, 0, 1, 1, 1)
        self.joystickLock = QtWidgets.QPushButton(Dialog)
        self.joystickLock.setMinimumSize(QtCore.QSize(60, 60))
        self.joystickLock.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(25)
        self.joystickLock.setFont(font)
        self.joystickLock.setObjectName("joystickLock")
        self.gridLayout.addWidget(self.joystickLock, 2, 2, 1, 1)
        self.lockState = QtWidgets.QLabel(Dialog)
        self.lockState.setMinimumSize(QtCore.QSize(60, 60))
        self.lockState.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(18)
        self.lockState.setFont(font)
        self.lockState.setAlignment(QtCore.Qt.AlignCenter)
        self.lockState.setObjectName("lockState")
        self.gridLayout.addWidget(self.lockState, 0, 0, 1, 1)
        self.pwrSearch = QtWidgets.QPushButton(Dialog)
        self.pwrSearch.setMinimumSize(QtCore.QSize(60, 60))
        self.pwrSearch.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pwrSearch.setFont(font)
        self.pwrSearch.setObjectName("pwrSearch")
        self.gridLayout.addWidget(self.pwrSearch, 2, 0, 1, 1)
        self.refHeight = QtWidgets.QLabel(Dialog)
        self.refHeight.setMinimumSize(QtCore.QSize(60, 60))
        self.refHeight.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(10)
        self.refHeight.setFont(font)
        self.refHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.refHeight.setWordWrap(False)
        self.refHeight.setObjectName("refHeight")
        self.gridLayout.addWidget(self.refHeight, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.joystickOk = QtWidgets.QPushButton(Dialog)
        self.joystickOk.setMinimumSize(QtCore.QSize(100, 0))
        self.joystickOk.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.joystickOk.setFont(font)
        self.joystickOk.setObjectName("joystickOk")
        self.horizontalLayout.addWidget(self.joystickOk)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "🕹"))
        self.joystickStop.setText(_translate("Dialog", "🛑"))
        self.joystickDown.setText(_translate("Dialog", "🔽"))
        self.joystickLeft.setText(_translate("Dialog", "◀"))
        self.joystickRight.setText(_translate("Dialog", "▶"))
        self.joystickUp.setText(_translate("Dialog", "🔼"))
        self.joystickLock.setText(_translate("Dialog", "🔒"))
        self.lockState.setToolTip(_translate("Dialog", "Lock state"))
        self.lockState.setText(_translate("Dialog", "🤢"))
        self.pwrSearch.setText(_translate("Dialog", "🤖"))
        self.refHeight.setToolTip(_translate("Dialog", "Reflector height"))
        self.refHeight.setText(_translate("Dialog", "n/a"))
        self.joystickOk.setText(_translate("Dialog", "OK"))