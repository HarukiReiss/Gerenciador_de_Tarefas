from qt_core import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        self.projeto.clicked.connect(lambda: self.openWindow(0))
        self.colaborador.clicked.connect(lambda: self.openWindow(1))

    def openWindow(self, i):
        self.stackedWidget.setCurrentIndex(i)
    
    