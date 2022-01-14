from qt_core import *

class CardTasks(QWidget):
    def __init__(self, tarefa):
        super().__init__()
        uic.loadUi('view/card_task.ui', self)

        self.t = tarefa
        self.nome.setText(self.t.nome)
        self.desc.setText(self.t.desc)
        self.colab.setText(str(tarefa.lista_colab))
        if self.t.status == 1:
            self.status.setText('Concluída!')
        elif self.t.status == 0:
            self.status.setText('Em andamento...')
