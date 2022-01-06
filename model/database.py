import sqlite3

from model.colaborador_dao import createTableColabs


def connect():
    conn = sqlite3.connect('database/G_Projetos.sqlite')
    return conn

def createDB():
    conn = connect()
    cursor = conn.cursor
    createTableColabs(cursor)
    conn.commit()
    conn.close()
