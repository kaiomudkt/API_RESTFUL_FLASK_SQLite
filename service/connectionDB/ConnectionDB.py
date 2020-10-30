import sqlite3


class ConnectionDB():

    def __init__(self, path='storage.db'):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()
        self.exec_schema()

    '''tem q acontecer somente uma vez'''

    def exec_schema(self):
        self.cursor.execute('DROP TABLE IF EXISTS aluno')
        self.cursor.execute('CREATE TABLE aluno (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, rga TEXT, curso TEXT, situacao TEXT, registrado_em TEXT)')
        self.cursor.execute("INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('ccc', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019')")
        self.cursor.execute("INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('bbbb', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019')")
        self.cursor.execute("INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('dddd', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019') ")
        self.cursor.execute("INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('aaaaa', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019') ")
        self.cursor.execute("INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('gggggg', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019') ")
        self.cursor.execute("INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('ffff', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019') ")
        self.cursor.execute("INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('eeeee', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019') ")
        self.cursor.execute("INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES ('hhhh', '2018.1907.125-5', 'SI', 'ativo', '25/12/2019') ")
        self.conn.commit()
        # with current_app.open_resource('schema.sql') as f:
        #     self.conn.executescript(f.read().decode('utf8'))
