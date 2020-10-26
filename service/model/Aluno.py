import json
from datetime import date

from service import db

class AlunoModel():
    '''aplica em massa'''

    def get_all(self, limite, pagina):
        db.cursor.execute("SELECT * FROM aluno")
        resp = db.cursor.fetchall()
        #db.conn.close()
        db.conn.commit()
        return json.dumps(resp)

    def insert(self, rga, nome, curso):
        registrado_em = date.today()
        db.cursor.execute(
            "INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES(?, ?, ?, ?, ?)",
            (nome, rga, curso, 'inativo', registrado_em))
        db.cursor.execute("SELECT * FROM aluno")
        resp = db.cursor.fetchall()
        #db.conn.close()
        db.conn.commit()
        return json.dumps(resp)

    '''aplica unitariamente'''

    def get_by_id(self, id):
        return "aludo deste id: " + id

    def edit_by_id(self, id, rga, nome, curso):
        return "aplicou edição nos dados deste aluno do ID " + id + " rga" + rga + " nome " + nome + " curso " + curso

    def delete_by_id(self, id):
        return "removendo alundo deste ID " + id
