from qt_core import *

class CardProjeto(QWidget):
    def __init__(self, projeto, parent):
        super().__init__()
        uic.loadUi('view/card_projeto.ui', self)

        self.p = projeto
        self.parent = parent

        self.nome.setText(self.p.nome)
        
    def mousePressEvent(self, event):
        print('Projeto: ', self.p.nome)
        self.parent.new_proj(self.p)


