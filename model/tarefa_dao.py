from model import database
from model.tarefa import Tarefa

task_list = []

def add_task(tarefa):
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """INSERT INTO Tarefas (nome, descricao, status, project_id, colab)
                VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(sql, Tarefa.get_task())
        conn.commit()
    except Exception as e:
        print("Ocorreu um erro!")
        print(e)
    finally:
        conn.close()

def selectAll(proj_id):
    t_list = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """SELECT * FROM Tarefas WHERE project_id=?"""
        cursor.execute(sql, [proj_id])
        result = cursor.fetchall()
        for c in result:
            new_task = Tarefa(c[0], c[1], c[2], c[3], c[4], c[5])
            t_list.append(new_task)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return t_list

def edit_task(tarefa):
    pass

def delete_task(id):
    pass

