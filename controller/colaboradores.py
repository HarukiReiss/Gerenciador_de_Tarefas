from model.colaborador import Colaborador
import model.colaborador_dao as colaborador_dao
from qt_core import *

class Colaboradores(QWidget):
    lista_colab = []
    colab_atual = None

    def __init__(self):
        super().__init__()
        uic.loadUi('view/colaboradores.ui', self)

        self.carregar_dados()

        self.tabela_colab.verticalHeader().setVisible(False)
        self.tabela_colab.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela_colab.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        self.tabela_colab.setEditTrigger(QTableWidget.NoEditTrigger)
        self.tabela_colab.setSelectionBehavior(QTableWidget.SelectRows)

        self.tabela_colab.clicked.connect(self.on_click)
    
    def carregar_dados(self):
        pass
        