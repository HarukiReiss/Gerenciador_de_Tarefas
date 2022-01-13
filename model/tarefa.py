
class Tarefa():
    def __init__(self, id, nome, descricao, status, project_id, lista_colabs=[]):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.status = status
        self.proj_id = project_id
        self.lista_colabs = lista_colabs

    def get_task(self):
        return(self.nome, self.descricao, self.status, self.proj_id, self.lista_colabs)
