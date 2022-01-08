import sqlite3

from model.colaborador_dao import createTableColabs
from model.projeto_dao import createTableProjeto


def connect():
    conn = sqlite3.connect('database/G_Projetos.sqlite')
    return conn

def createDB():
    conn = connect()
    cursor = conn.cursor
    createTableColabs(cursor)
    createTableProjeto(cursor)
    conn.commit()
    conn.close()
