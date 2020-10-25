from service.connectionDB.ConnectionDB import ConnectionDB
import json
from datetime import date

class AlunoModel():
    def __init__(self):
        self.connectionDB = ConnectionDB()

    '''aplica em massa'''

    def get_all(self, limite, pagina):
        self.connectionDB.cursor.execute("SELECT * FROM aluno")
        resp = self.connectionDB.cursor.fetchall()
        self.connectionDB.conn.close()
        print(resp)
        return json.dumps(resp)

    def insert(self, rga, nome, curso):
        registrado_em = date.today()
        self.connectionDB.cursor.execute("INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES(?, ?, ?, ?, ?)",
                                         (nome, rga, curso, 'inativo', registrado_em))
        self.connectionDB.cursor.execute("SELECT * FROM aluno")
        resp = self.connectionDB.cursor.fetchall()
        self.connectionDB.conn.close()
        print(resp)
        return json.dumps(resp)

    '''aplica unitariamente'''

    def get_by_id(self, id):
        return "aludo deste id: " + id

    def edit_by_id(self, id, rga, nome, curso):
        return "aplicou edição nos dados deste aluno do ID " + id + " rga" + rga + " nome " + nome + " curso " + curso

    def delete_by_id(self, id):
        return "removendo alundo deste ID " + id
