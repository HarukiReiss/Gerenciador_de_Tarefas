from qt_core import *

class CardProjeto(QWidget):
    def __init__(self, projeto, parente):
        super().__init__()
        uic.loadUi('view/card_projeto.ui', self)

        self.p = projeto
        self.parente = parente

        self.nome.setText(self.p.nome)
        
    def mousePressEvent(self, event):
        pass


