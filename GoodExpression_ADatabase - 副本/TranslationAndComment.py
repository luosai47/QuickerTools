# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TranslationAndComment.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class TranslationAndComment(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 188)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(330, 150, 160, 30))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textEdit_Translation = QtWidgets.QTextEdit(Dialog)
        self.textEdit_Translation.setGeometry(QtCore.QRect(0, 30, 250, 100))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textEdit_Translation.setFont(font)
        self.textEdit_Translation.setObjectName("textEdit_Translation")
        self.textEdit_Translation_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_Translation_2.setGeometry(QtCore.QRect(250, 30, 250, 100))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.textEdit_Translation_2.setFont(font)
        self.textEdit_Translation_2.setObjectName("textEdit_Translation_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 8, 81, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(250, 8, 81, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit_Translation.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'楷体\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">翻译中请您耐心等待</p></body></html>"))
        self.label.setText(_translate("Dialog", "翻译修改："))
        self.label_2.setText(_translate("Dialog", "添加评论："))

