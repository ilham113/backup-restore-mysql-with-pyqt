# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restore.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(290, 400)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 281, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 258, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LDb = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.LDb.setObjectName("LDb")
        self.verticalLayout.addWidget(self.LDb)
        self.nama_db = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nama_db.setObjectName("nama_db")
        self.verticalLayout.addWidget(self.nama_db)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.path = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.path.setObjectName("path")
        self.horizontalLayout.addWidget(self.path)
        self.button_browser = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_browser.setObjectName("button_browser")
        self.horizontalLayout.addWidget(self.button_browser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.button_restore = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_restore.setObjectName("button_restore")
        self.verticalLayout.addWidget(self.button_restore)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Backup & Restore Database Duta Parkir"))
        self.label.setText(_translate("Form", " Restore"))
        self.LDb.setText(_translate("Form", "Nama Database"))
        self.label_3.setText(_translate("Form", "File SQl"))
        self.button_browser.setText(_translate("Form", "Browser"))
        self.button_restore.setText(_translate("Form", "restore"))
        self.label_2.setText(_translate("Form", "Database Duta Parkir"))
