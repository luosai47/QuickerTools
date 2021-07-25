import sqlite3
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
from GoodExpressionMainPage import *



class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle('主界面')
        self.setWindowIcon(QIcon('icon.ico'))

        self.ui.buttonBox.accepted.connect(self.write_in)

        self.show()

    def write_in(self):
        Tag_content = ''
        if self.ui.checkBox_zhaiyao.isChecked()==True:
            Tag_content = Tag_content + '摘要 '
        if self.ui.checkBox_biaozheng.isChecked()==True:
            Tag_content = Tag_content + '衔接 '
        if self.ui.checkBox_taren.isChecked()==True:
            Tag_content = Tag_content + '他人 '
        if self.ui.checkBox_chengshangqixia.isChecked()==True:
            Tag_content = Tag_content + self.ui.lineEdit_2.text() + ' '
        if self.ui.checkBox_qita.isChecked()==True:
            Tag_content = Tag_content + self.ui.lineEdit.text() + ' '
        conn = sqlite3.connect(r'data/GoodExpression.db')
        cur = conn.cursor()
        sql = 'insert into MainPage (Content, Source, Tag)' \
              'values (?,?,?)'

        data = (self.ui.textEdit.toPlainText(), self.ui.textEdit_3.toPlainText(), Tag_content)
        cur.execute(sql, data)
        conn.commit()
        cur.close()
        conn.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())