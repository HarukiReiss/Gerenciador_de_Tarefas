from qt_core import *

class Projeto(QWidget):
    def __init__(self, projeto=None):
        super().__init__()
        uic.loadUi('view/projeto.ui', self)