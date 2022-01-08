from model import database
from model.projeto import Projeto


def createTableProjeto(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "Projetos" (
        "id"	INTEGER,
        "nome"	TEXT NOT NULL,
        "descricao"	TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
    );
    """)

def insert(proj):
    try: 
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Projetos (nome,descricao) 
            VALUES (?,?);"""
        cursor.execute(sql, [proj.nome, proj.descricao])
        conn.commit()

        if len(proj.lista_tarefas) > 0:
            pass

    except Exception as e:
        print('Deu erro!!!')
        print(e)
    finally:  
        conn.close() 


def selectAll():
    lista = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Projetos ORDER BY upper(nome);"""
        cursor.execute(sql)
        result = cursor.fetchall() 
        for r in result:
            lista_tarefas = []

            colab = Projeto(r[0], r[1], r[2],lista_tarefas)
            lista.append(colab)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista