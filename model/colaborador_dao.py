from model.colaborador import Colaborador
from model import database

def createTableColabs(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS "Colaboradores" (
        "id"    INTERGER,
        "nome"  TEXT NOT NULL,
        "email" TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT));""")

def insert(colab):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Colaboradores (nome, email)
            VALUES (?,?);"""
        cursor.execute(sql, colab.get_dados_lista())
        conn.commit()
    except Exception as e:
        print('Ocorreu um erro!')
        print(e)
    finally:
        conn.close()

def update(colab):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE Colaboradores SET nome=?, email=? WHERE id=?;"""
        l = colab.get_dados_lista()
        l.append(colab.id)
        cursor.execute(sql, 1)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def delete(id):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Colaboradores WHERE id=?;"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()

def selectAll():
    lista = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Colaboradores ORDER BY upper(nome);"""
        cursor.execute(sql)
        result = cursor.fetchall()
        for r in result:
            novo_colaborador = Colaborador(r[0], r[1], r[2])
            lista.append(novo_colaborador)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista








    