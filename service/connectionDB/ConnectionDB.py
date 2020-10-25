import sqlite3
from flask import current_app
from service import service

class ConnectionDB():
    def __init__(self, path='bancoDeDados.db'):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        self.exec_schema()

    '''tem q acontecer somente uma vez'''
    def exec_schema(self):
        self.cursor.execute('DROP TABLE IF EXISTS aluno')
        self.cursor.execute('CREATE TABLE aluno (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, rga TEXT, curso TEXT, situacao TEXT, registrado_em TEXT)')
        # with current_app.open_resource('schema.sql') as f:
        #     self.conn.executescript(f.read().decode('utf8'))