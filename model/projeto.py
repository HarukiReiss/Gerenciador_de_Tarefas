
class Projeto():
    def __init__ (self, id, nome, descricao, lista_tarefas=[]):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.lista_tarefas = lista_tarefas
        
    def getProject(self):
        return [self.nome, self.descricao]

