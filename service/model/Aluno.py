from service.connectionDB.conndb import Conndb


'''https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/'''
class AlunoModel:
    def __int__(self):
        self.conndb = Conndb()

    '''aplica em massa'''
    def get_all(self, limite, pagina):
        return "lista de todos os alunos da pagina " + pagina + " em " + limite

    def insert(self, rga, nome, curso):
        try:
            #db = self.conndb.get_db()
            resp = self.conndb.c.execute("INSERT INTO aluno (nome,rga,curso) VALUES(?, ?, ?)", (nome, rga, curso))
            self.conndb.conn.commit()
            msg = "Record successfully added"
        except:
            #con.rollback()
            msg = "error in insert operation"
        finally:
            self.conndb.conn.close()
            print(msg)
            return resp

    '''aplica unitariamente'''
    def get_by_id(self, id):
        return "aludo deste id: " + id

    def edit_by_id(self, id, rga, nome, curso):
        return "aplicou edição nos dados deste aluno do ID " + id + " rga" + rga + " nome " + nome + " curso " + curso

    def delete_by_id(self, id):
        return "removendo alundo deste ID " + id
