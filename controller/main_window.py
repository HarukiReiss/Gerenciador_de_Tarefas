from controller.card_projeto import CardProjeto
from controller.colaboradores import Colaboradores
from controller.projetos import Projetos
import model.projeto_dao as proj_dao
from qt_core import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        self.stackedWidget.insertWidget(1, Colaboradores())

        self.lista_projetos = []

        self.projeto.clicked.connect(lambda: self.openWindow(0))
        self.colaborador.clicked.connect(lambda: self.openWindow(1))

        self.new_project.clicked.connect(self.new_proj)

        self.load_project()
    
    def load_project(self):
        for i in reversed(range(self.project_layout.count())):
            self.project_layout.itemAt(i).widget().deleteLater()
        
        self.lista_projetos = proj_dao.selectAll()
        for p in self.lista_projetos:
            self.project_layout.addWidget(CardProjeto(p, self))

    def openWindow(self, i):
        self.stackedWidget.setCurrentIndex(i)

    def new_proj(self, proj=None):
        self.stackedWidget.insertWidget(2, Projetos(self, proj))
        self.openWindow(2)
    
    