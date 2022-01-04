from model.colaborador import Colaborador
import model.colaborador_dao as colaborador_dao
from qt_core import *


class CadColaborador(QWidget):
    def __init__(self, mainWindow, colaborador=None):
        super().__init__()
        uic.loadUi('view/cad_colaborador.ui', self)
        self.mainWindow = mainWindow
        self.colaborador = colaborador
        if colaborador != False:
            self.carrega_colaborador()
        
    
    def fechar_page(self):
        pass
    
    def carrega_colaborador(self):
        pass

    def salvar_colaborador(self):
        nome = self.nome.text()
        email = self.email.text()

        if self.colaborador != False:
            colaborador_editado = Colaborador(self.colaborador.id, nome, email)
            colaborador_dao.update(colaborador_editado)
        
        else:
            colaborador_novo = Colaborador(None, nome, email)
            colaborador_dao.insert(colaborador_novo)


