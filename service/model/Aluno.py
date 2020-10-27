import json
from datetime import date

from service import db

#http://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte2.html
class AlunoModel():
    '''aplica em massa'''

    def get_all(self, limite=25, pagina=1, nome=None):
        if nome:
            if self.exist_nome(nome):
                query = "SELECT * FROM aluno where nome = %s "
                db.cursor.execute(query % nome)
            else:
                return {"404": "Nome não encontrado"}, 404
        else:
            # https://www.sqlshack.com/pagination-in-sql-server/
            #esta com erro 400
            query = "SELECT * FROM aluno OFFSET %s * %s ROWS FETCH NEXT %s ROWS ONLY"
            db.cursor.execute(query, (pagina, limite, limite,))
        resp = db.cursor.fetchall()
        db.conn.commit()
        return json.dumps(resp)

    def exist_nome(self, nome):
        query = "SELECT * FROM aluno where nome = ?"
        aluno = db.cursor.execute(query, [nome])
        return aluno.fetchone() is not None

    def insert(self, rga, nome, curso):
        registrado_em = date.today()
        query = "INSERT INTO aluno (nome, rga, curso, situacao, registrado_em) VALUES(?, ?, ?, ?, ?)"
        db.cursor.execute(query, (nome, rga, curso, 'ativo', registrado_em))
        db.cursor.execute("SELECT * FROM aluno")
        #tem que retornar o novo aluno, mas qual o id do novo user?
        resp = db.cursor.fetchall()
        db.conn.commit()
        return json.dumps(resp)

    '''aplica unitariamente'''

    def get_by_id(self, id):
        if self.exist(id):
            query = "SELECT * FROM aluno where id = ?"
            db.cursor.execute(query, [id])
            resp = db.cursor.fetchall()
            db.conn.commit()
            return json.dumps(resp)
        else:
            return {"404": "Usuário com ID "+id+" não foi encontrado"}, 404

    def edit_by_id(self, id, rga, nome, curso, situacao):
        if self.exist(id):
            query = "UPDATE aluno set (nome = ?, rga = ?, curso = ?)  where id = ? "
            db.cursor.execute(query, (nome, rga, curso, id))
            return self.get_by_id(id)
        else:
            return {"404": "Usuário com ID "+id+" não foi encontrado"}, 404

    def delete_by_id(self, id):
        if self.exist(id):
            aluno = self.get_by_id(id)
            query = "DELETE FROM aluno where id = ?"
            db.cursor.execute(query, id)
            db.conn.commit()
            return aluno
        else:
            return {"404": "Usuário com ID "+id+" não foi encontrado"}, 404

    def exist(self, id):
        query = "SELECT * FROM aluno where id = ?"
        aluno = db.cursor.execute(query, [id])
        return aluno.fetchone() is not None