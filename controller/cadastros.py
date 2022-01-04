from qt_core import *


class Cadastros(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/cadastros.ui', self)