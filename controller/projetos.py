from qt_core import *
from controller.card_task import CardTasks
import model.colaborador_dao as colab_dao
import model.projeto_dao as proj_dao
import model.tarefa_dao as task_dao
from model.projeto import Projeto
from model.tarefa import Tarefa

class Projetos(QWidget):
    def __init__(self, parent, projeto=None):
        super().__init__()
        uic.loadUi('view/projetos.ui', self)

        self.parent = parent
        self.p = projeto
        self.lista_colabs = []
        self.lista_add_colabs = []
        self.lista_tasks = []
        
        
        self.carrega_dados()

        self.add_colab.clicked.connect(self.addColab)
        self.del_colab.clicked.connect(self.delColab)
        self.task_add.clicked.connect(self.addTask)
        self.save.clicked.connect(self.saveProject)
        self.excluir.clicked.connect(self.delProject)

        if self.p != False:
            self.project_name_edit.setText(self.p.nome)
            self.project_desc_edit.setText(self.p.descricao)
            self.carrega_tasks(projeto)
        else:
            self.excluir.hide()

    def carrega_dados(self):
        temp_lista = []
        self.lista_colabs = colab_dao.selectAll()
        for c in self.lista_colabs:
            temp_lista.append(c.nome)
        self.colab_add.addItems(temp_lista)

    def carrega_tasks(self, projeto):
        for i in reversed(range(self.painel_tasks.count())):
            self.painel_tasks.itemAt(i).widget().deleteLater()
        lista = self.p.lista_tarefas
        for t in lista:
            self.painel_tasks.addWidget(CardTasks(t))

    def carrega_t(self):
        for i in reversed(range(self.painel_tasks.count())):
            self.painel_tasks.itemAt(i).widget().deleteLater()

        lista = self.lista_tasks
        for t in lista:
            self.painel_tasks.addWidget(CardTasks(t))

    def addColab(self):
        i = self.colab_add.currentIndex()
        c = self.lista_colabs[i]
        if self.isExist(c) == False:
            self.lista_add_colabs.append(c)
            self.colab_del.addItem(self.lista_colabs[i].nome)
            self.colab_qtd.setText(f'{len(self.lista_add_colabs)}')

    def delColab(self):
        i = self.colab_del.currentIndex()
        if i >= 0:
            self.lista_add_colabs.remove(self.lista_add_colabs[i])
            self.colab_del.removeItem(i)
            self.colab_qtd_setText(f'{len(self.lista_add_colabs)}')

    def isExist(self, colab):
        for c in self.lista_add_colabs:
            if c.id == colab.id:
                return True

        return False

    def addTask(self):
        nome = self.task_name.text()
        desc = self.task_desc.text()
        if (self.finalizado.isChecked()):
            status = 1
        elif (self.pendente.isChecked()):
            status = 0
        colab = len(self.lista_add_colabs)
        task_dao.add_task(Tarefa(None, nome, desc, status, colab))
        self.lista_tasks.append(Tarefa(None, nome, desc, status, colab))
        self.carrega_t

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
        if self.p != False:
            print('Excluir projeto com id = ',self.p.id)







    