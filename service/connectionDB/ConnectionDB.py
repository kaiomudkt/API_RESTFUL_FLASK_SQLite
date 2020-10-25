import sqlite3


class ConnectionDB():
    def __init__(self, path='bancoDeDados.db'):
        self.conn = sqlite3.connect(path)
        #self.conn = self.db.conn()
        self.cursor = self.conn.cursor()
        self.execute_scheme()

    # def conn(self):
    #     return sqlite3.connect(self.path)

    def execute_scheme(self):
        pass
        # self.cursor.execute('DROP TABLE IF EXISTS aluno')
        #self.cursor.execute('CREATE TABLE aluno (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, rga TEXT, curso TEXT, situacao TEXT, registrado_em TEXT)')
