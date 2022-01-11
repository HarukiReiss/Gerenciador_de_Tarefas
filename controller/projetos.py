from qt_core import *
import model.colaborador_dao as colab_dao
import model.projeto_dao as proj_dao
from model.projeto import Projeto

class Projetos(QWidget):
    def __init__(self, parent, projeto):
        super().__init__()
        uic.loadUi('view/projetos.ui', self)

        self.parent = parent
        self.p = projeto
        self.lista_colabs = []
        self.lista_add_colabs = []
        
        
        self.carrega_dados()

        self.add_colab.clicked.connect(self.addColab)
        self.del_colab.clicked.connect(self.delColab)
        self.task_add.clicked.connect(self.addTask)
        self.save.clicked.connect(self.saveProject)
        self.excluir.clicked.connect(self.delProject)

        if self.p != False:
            self.project_name_edit.setText(self.p.nome)
            self.project_desc_edit.setText(self.p.descricao)
        else:
            self.excluir.hide()

    def carrega_dados(self):
        temp_lista = []
        self.lista_colabs = colab_dao.selectAll()
        for c in self.lista_colabs:
            temp_lista.append(c.nome)
        self.colab_add.addItems(temp_lista)

    def addColab(self):
        i = self.colab_add.currentIndex()
        c = self.lista_colabs[i]
        if self.isExist(c) == False:
            self.lista_add_colabs.append(c)
            self.colab_del.addItem(self.lista_colabs[i].nome)
            self.colab_qtd.setText({len(self.lista_add_colabs)})

    def delColab(self):
        i = self.colab_del.currentIndex()
        if i >= 0:
            self.lista_add_colabs.remove(self.lista_add_colabs[i])
            self.colab_del.removeItem(i)
            self.colab_qtd_setText({len(self.lista_add_colabs)})

    def isExist(self, colab):
        for c in self.lista_add_colabs:
            if c.id == colab.id:
                return True

        return False

    def addTask(self):
        pass

    def saveProject(self):
        nome = self.project_name_edit.text()
        desc = self.project_desc_edit.text()
        if nome != '' and desc != '':
            if self.p == False:
                proj_dao.insert(Projeto(None, nome, desc))
            else:
                pass
        
        self.parent.openWindow(0)

    def delProject(self):
        pass







    