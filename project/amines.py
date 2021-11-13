import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from project import Example


class Amines(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('amines.ui', self)
        self.initUI()
        self.textEdit.setReadOnly(True)
        self.connection = sqlite3.connect("tests.sqlite")
        self.answer_1.clicked.connect(self.answer1)
        self.answer_2.clicked.connect(self.answer2)
        self.answer_3.clicked.connect(self.answer3)

    def answer1(self):
        if self.answer_1.text() == 'ответ':
            con = sqlite3.connect("tests.sqlite")
            cur = con.cursor()
            result = cur.execute("""SELECT answer FROM answers
                        WHERE id=(SELECT id FROM tests WHERE number = 1 AND
                        topic=(SELECT id FROM topics WHERE topic =
                        'арены'))""").fetchall()
            self.ans_1.setText(result[0][0])
            self.answer_1.setText('скрыть ответ')
            con.close()
        else:
            self.ans_1.setText('')
            self.answer_1.setText('ответ')

    def answer2(self):
        if self.answer_2.text() == 'ответ':
            con = sqlite3.connect("tests.sqlite")
            cur = con.cursor()
            result = cur.execute("""SELECT answer FROM answers
                        WHERE id=(SELECT id FROM tests WHERE number = 2 AND
                        topic=(SELECT id FROM topics WHERE topic =
                        'арены'))""").fetchall()
            self.ans_2.setText(result[0][0])
            self.answer_2.setText('скрыть ответ')
            con.close()
        else:
            self.ans_2.setText('')
            self.answer_2.setText('ответ')

    def answer3(self):
        if self.answer_3.text() == 'ответ':
            con = sqlite3.connect("tests.sqlite")
            cur = con.cursor()
            result = cur.execute("""SELECT answer FROM answers
                        WHERE id=(SELECT id FROM tests WHERE number = 3 AND
                        topic=(SELECT id FROM topics WHERE topic =
                        'арены'))""").fetchall()
            self.ans_3.setText(result[0][0])
            self.answer_3.setText('скрыть ответ')
            con.close()
        else:
            self.ans_3.setText('')
            self.answer_3.setText('ответ')

    def initUI(self):
        self.btn_return.clicked.connect(self.hello)

    def hello(self):
        self.cams = Example()
        self.cams.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Amines()
    ex.show()
    sys.exit(app.exec())
