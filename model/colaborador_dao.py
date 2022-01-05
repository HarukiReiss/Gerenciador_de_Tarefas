from model.colaborador import Colaborador
"""from model import database"""

def insert(colaborador):
    """try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = INSERT INTO Colaboradores (nome, email)
            VALUES (?,?);
        cursor.execute(sql, colaborador.get_dados_lista())
        conn.commit()
    except Exception as e:
        print('Ocorreu um erro!')
        print(e)
    finally:
        conn.close()"""

def update(colaborador):
    """try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = UPDATE Colaboradores SET nome=?, email=? WHERE id=?;
        l = colaborador.get_dados_lista()
        l.append(colaborador.id)
        cursor.execute(sql, 1)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()"""

def update_lixeira(id, deletado):
    """try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = UPDATE Colaboradores SET deletado=? WHERE id=?;
        cursor.execute(sql, [deletado.id])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close"""

def delete(id):
    """try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = DELETE FROM Colaboradores WHERE id=?;
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()"""


def deleteLixeiraAll():
    """try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = DELETE FROM Colaboradores WHERE deletado=1;
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()"""

def selectAll():
    """lista = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = SELECT * FROM Colaboradores WHERE deletado = 0 ORDER BY upper(nome);
        result = cursor.fetchall()
        for r in result:
            novo_colaborador = Colaborador(
                r[0], r[1], r[2])
            lista.append(novo_colaborador)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista"""

def selectDeletedAll():
    """lista = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = SELECT * FROM Colaboradores WHERE deletado = 1 ORDER BY upper(nome);
        cursor.execute(sql)
        result = cursor.fetchall()
        for r in result:
            novo_colaborador = Colaborador(
                r[0], r[1], r[2])
            lista.append(novo_colaborador)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista"""






    