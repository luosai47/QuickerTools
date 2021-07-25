# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GoodExpressionMainPage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyperclip


class MainPage(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 299)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(330, 270, 161, 20))
        self.buttonBox.setMouseTracking(True)
        self.buttonBox.setTabletTracking(True)
        self.buttonBox.setAcceptDrops(True)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(16, 160, 60, 40))
        self.label.setObjectName("label")
        self.checkBox_zhaiyao = QtWidgets.QCheckBox(Dialog)
        self.checkBox_zhaiyao.setGeometry(QtCore.QRect(90, 170, 72, 17))
        self.checkBox_zhaiyao.setTristate(True)
        self.checkBox_zhaiyao.setObjectName("checkBox_zhaiyao")
        self.checkBox_biaozheng = QtWidgets.QCheckBox(Dialog)
        self.checkBox_biaozheng.setGeometry(QtCore.QRect(140, 170, 72, 17))
        self.checkBox_biaozheng.setObjectName("checkBox_biaozheng")
        self.checkBox_taren = QtWidgets.QCheckBox(Dialog)
        self.checkBox_taren.setGeometry(QtCore.QRect(190, 170, 72, 17))
        self.checkBox_taren.setObjectName("checkBox_taren")
        self.checkBox_chengshangqixia = QtWidgets.QCheckBox(Dialog)
        self.checkBox_chengshangqixia.setGeometry(QtCore.QRect(240, 170, 72, 17))
        self.checkBox_chengshangqixia.setObjectName("checkBox_chengshangqixia")
        self.checkBox_qita = QtWidgets.QCheckBox(Dialog)
        self.checkBox_qita.setGeometry(QtCore.QRect(370, 170, 51, 20))
        self.checkBox_qita.setObjectName("checkBox_qita")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 218, 91, 40))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(5, 5, 490, 150))
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setOverwriteMode(True)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(90, 210, 405, 51))
        self.textEdit_3.setTabChangesFocus(True)
        self.textEdit_3.setOverwriteMode(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(420, 170, 70, 20))
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 170, 70, 20))
        self.lineEdit_2.setTabletTracking(True)
        self.lineEdit_2.setAutoFillBackground(True)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">添加标签</span></p></body></html>"))
        self.checkBox_zhaiyao.setText(_translate("Dialog", "摘要"))
        self.checkBox_biaozheng.setText(_translate("Dialog", "衔接"))
        self.checkBox_taren.setText(_translate("Dialog", "他人"))
        self.checkBox_chengshangqixia.setText(_translate("Dialog", "表征"))
        self.checkBox_qita.setText(_translate("Dialog", "其他"))
        self.label_2.setText(_translate("Dialog",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; "
                                        "font-weight:600;\">添加来源</span></p><p align=\"center\"><span style=\" "
                                        "font-size:10pt; font-weight:600;\">(如文献名称)</span></p></body></html>"))
        self.textEdit.setHtml(_translate("Dialog",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                         "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                         "type=\"text/css\">\n "
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; "
                                         "font-weight:400; font-style:normal;\">\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
                                         f"{pyperclip.paste()} </p></body></html>"))
        self.textEdit_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                     "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Luosai First Article</p></body></html>"))
        self.lineEdit.setText(_translate("Dialog", "DFT"))
        self.lineEdit_2.setText(_translate("Dialog", "XRD"))
