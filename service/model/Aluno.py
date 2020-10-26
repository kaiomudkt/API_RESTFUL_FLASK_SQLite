import json
from datetime import date

from service import db

class AlunoModel():
    '''aplica em massa'''

    def get_all(self, limite, pagina):
        db.cursor.execute("SELECT * FROM aluno")
        resp = db.cursor.fetchall()
        db.conn.commit()
        return json.dumps(resp)

    def insert(self, rga, nome, curso):
        registrado_em = date.today()
        db.cursor.execute(
            "INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES(?, ?, ?, ?, ?)",
            (nome, rga, curso, 'inativo', registrado_em))
        db.cursor.execute("SELECT * FROM aluno")
        resp = db.cursor.fetchall()
        db.conn.commit()
        return json.dumps(resp)

    '''aplica unitariamente'''

    def get_by_id(self, id):
        db.cursor.execute("SELECT * FROM aluno where id = ?", [id])
        resp = db.cursor.fetchall()
        db.conn.commit()
        return json.dumps(resp)

    def edit_by_id(self, id, rga, nome, curso):
        db.cursor.execute("UPDATE aluno set (nome = '{nome}', rga, curso)  where id = ")
        aluno = db.cursor.execute("SELECT * FROM aluno where id = ? ", [id])
        return aluno

    def delete_by_id(self, id):
        return "removendo alundo deste ID " + id
