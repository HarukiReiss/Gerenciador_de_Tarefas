
class Colaborador():
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def get_dados_lista(self):
        lista_dados = [self.nome, self.email]

        return lista_dados
