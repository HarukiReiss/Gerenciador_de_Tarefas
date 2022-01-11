from model.colaborador import Colaborador
import model.colaborador_dao as colaborador_dao
from qt_core import *

class Colaboradores(QWidget):
    

    def __init__(self):
        super().__init__()
        uic.loadUi('view/colaboradores.ui', self)

        self.lista_colab = []
        self.colab_atual = None

        self.save.clicked.connect(self.save_colab)
        self.excluir.clicked.connect(self.del_colab)

        self.carregar_dados()

        self.tabela_colab.verticalHeader().setVisible(False)
        self.tabela_colab.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabela_colab.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

        self.tabela_colab.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tabela_colab.setSelectionBehavior(QTableWidget.SelectRows)

        self.tabela_colab.clicked.connect(self.click)
    
    def carregar_dados(self):
        self.lista_colab = colaborador_dao.selectAll()

        self.limpar()
        self.tabela_colab.setRowCount(0)
        for p in self.lista_colab:
            self.addLine(p)

    def addLine(self, p):
        rowCount = self.tabela_colab.rowCount()
        self.tabela_colab.insertRow(rowCount)

        id = QTableWidgetItem(str(p.id))
        nome = QTableWidgetItem(p.nome)
        email = QTableWidgetItem(p.email)

        self.tabela_colab.setItem(rowCount, 0, id)
        self.tabela_colab.setItem(rowCount, 1, nome)
        self.tabela_colab.setItem(rowCount, 2, email)

    def click(self):
        clicked_row = self.tabela_colab.currentRow()
        self.colab_atual = self.lista_colab[clicked_row]
        self.nome_edit.setText(self.colab_atual.nome)
        self.email_edit.setText(self.colab_atual.email)

    def save_colab(self):
        nome = self.nome_edit.text()
        email = self.email_edit.text()
        colab = Colaborador(None, nome, email)

        if nome != '' and email != '':
            if self.colab_atual == None:
                colaborador_dao.insert(colab)
            else:
                colab.id = self.colab_atual.id
                colaborador_dao.update(colab)

            self.carregar_dados()

    def limpar(self):
        self.nome_edit.clear()
        self.email_edit.clear()
        self.colab_atual = None

    def del_colab(self):
        if self.colab_atual != None:
            colaborador_dao.delete(self.colab_atual.id)
            self.carregar_dados()


        