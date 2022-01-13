from qt_core import *

class CardTasks(QWidget):
    def __init__(self, tarefa):
        super().__init__()
        uic.loadUi('view/card_task.ui', self)

        self.t = tarefa
        self.nome.setText(self.t.nome)
        self.desc.setText(self.t.desc)
        self.colab.setText(str(tarefa.project_id))
        if self.t.state == 1:
            self.state.setText('Concluída!')
        elif self.t.state == 0:
            self.state.setText('Em andamento...')
