import sys
import sqlite3

from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from project import Example


class Reactions(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('reactions.ui', self)
        self.connection = sqlite3.connect("reactions.sqlite")
        self.btn_result.clicked.connect(self.run)
        self.btn_return.clicked.connect(self.hello)
        self.c = [self.alkanes, self.alkenes, self.alkynes,
                  self.cycloalkanes, self.alkadienes, self.alcohols,
                  self.aldehyde, self.arenas, self.phenol,
                  self.carboxylic, self.amines, self.permangatan,
                  self.iodine, self.burn, self.silver,
                  self.copper, self.copper_oxide, self.copper_hydroxide,
                  self.nitrating_mixture, self.ferric_chloride, self.metals,
                  self.litmus, self.bromine_water]

    def run(self):
        self.result.setText('')
        topic, reagent = '', ''
        for i in self.c:
            if i.isChecked() and topic == '':
                topic = i.text()
            elif i.isChecked():
                reagent = i.text()

        con = sqlite3.connect("reactions.sqlite")
        cur = con.cursor()
        result = cur.execute(f"""SELECT result FROM results
                    WHERE topic=(SELECT id FROM topics WHERE topic = '{topic}'
                    AND reagent=(SELECT id FROM reagents WHERE reagent =
                    '{reagent}'))""").fetchall()
        if len(result) == 0:
            self.result.setText('Реакция не идет')
        else:
            self.result.setText(result[0][0])
        con.close()

    def hello(self):
        self.cams = Example()
        self.cams.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Reactions()
    ex.show()
    sys.exit(app.exec())
