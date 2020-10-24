import sqlite3

from service.connectionDB.conndb import Conndb


class AlunoModel():

    def __init__(self):
        print("instanciou AlunoModel")
        self.conndb = Conndb()
        self.conn = self.conndb.conn
        self.cur = self.conn.cur
        self.kaio = 'Kaio Lino'

    '''aplica em massa'''

    def get_all(self, limite, pagina):
        return "lista de todos os alunos da pagina " + pagina + " em " + limite

    def insert(self, rga, nome, curso, situacao):
        try:
            # db = self.conndb.get_db()
            conn = sqlite3.connect('database.db')
            resp = conn.cursor().execute("INSERT INTO aluno (nome, rga, curso, situacao) VALUES(?, ?, ?, ?)",
                                         (nome, rga, curso, situacao))
            conn.commit()
            msg = "Record successfully added"
        except:
            # conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.cursor().close()
            print(msg)
            return msg

    '''aplica unitariamente'''

    def get_by_id(self, id):
        return "aludo deste id: " + id

    def edit_by_id(self, id, rga, nome, curso):
        return "aplicou edição nos dados deste aluno do ID " + id + " rga" + rga + " nome " + nome + " curso " + curso

    def delete_by_id(self, id):
        return "removendo alundo deste ID " + id
