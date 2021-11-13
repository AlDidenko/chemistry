import sys

from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.btn_alkanes.clicked.connect(self.alkanes)
        self.btn_alkenes.clicked.connect(self.alkenes)
        self.btn_alkynes.clicked.connect(self.alkynes)
        self.btn_cycloalkanes.clicked.connect(self.cycloalkanes)
        self.btn_alkadienes.clicked.connect(self.alkadienes)
        self.btn_ketones.clicked.connect(self.ketones)
        self.btn_alcohols.clicked.connect(self.alcohols)
        self.btn_carboxylic.clicked.connect(self.carboxylic)
        self.btn_amines.clicked.connect(self.amines)
        self.btn_phenol.clicked.connect(self.phenol)
        self.btn_reactions.clicked.connect(self.reactions)

    def alkanes(self):
        from alkanes import Alkanes
        self.cams = Alkanes()
        self.cams.show()
        self.close()

    def alkenes(self):
        from alkenes import Alkenes
        self.cams = Alkenes()
        self.cams.show()
        self.close()

    def alkynes(self):
        from alkynes import Alkynes
        self.cams = Alkynes()
        self.cams.show()
        self.close()

    def cycloalkanes(self):
        from cycloalkanes import Cycloalkanes
        self.cams = Cycloalkanes()
        self.cams.show()
        self.close()

    def alkadienes(self):
        from alkadienes import Alkadienes
        self.cams = Alkadienes()
        self.cams.show()
        self.close()

    def ketones(self):
        from ketones import Ketones
        self.cams = Ketones()
        self.cams.show()
        self.close()

    def alcohols(self):
        from alcohols import Alcohols
        self.cams = Alcohols()
        self.cams.show()
        self.close()

    def carboxylic(self):
        from carboxylic import Carboxylic
        self.cams = Carboxylic()
        self.cams.show()
        self.close()

    def amines(self):
        from amines import Amines
        self.cams = Amines()
        self.cams.show()
        self.close()

    def phenol(self):
        from phenol import Phenol
        self.cams = Phenol()
        self.cams.show()
        self.close()

    def reactions(self):
        from reactions import Reactions
        self.cams = Reactions()
        self.cams.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
