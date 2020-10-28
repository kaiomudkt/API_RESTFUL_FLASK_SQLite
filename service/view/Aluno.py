from flask import request
from flask_restful import Resource, Api

from service import service
from service.controller.Aluno import AlunoController

api = Api(service)


class Alunos(Resource):

    def get(self):
        limite = request.args['limite']
        pagina = request.args['pagina']
        nome = request.args.get("nome")
        if nome:
            return AlunoController().get_all(limite, pagina, nome)
        else:
            return AlunoController().get_all(limite, pagina)

    def post(self):
        rga = request.form['rga']
        nome = request.form['nome']
        curso = request.form['curso']
        return AlunoController().insert(rga, nome, curso)

    def delete(self):
        return {'405': '(método não permitido)'}

    def put(self):
        return {'405': '(método não permitido)'}

    def patch(self):
        return {'405': '(método não permitido)'}

    def options(self):
        return {'405': '(método não permitido)'}


api.add_resource(Alunos, '/alunos')


class AlunosID(Resource):

    def get(self, id: int):
        return AlunoController().get_by_id(id)

    def put(self, id: int):
        rga = request.form['rga']
        nome = request.form['nome']
        curso = request.form['curso']
        if request.form['situacao']:
            return AlunoController().edit_by_id(id, rga, nome, curso, request.form['situacao'])
        else:
            return AlunoController().edit_by_id(id, rga, nome, curso)

    def delete(self, id: int):
        return AlunoController().delete_by_id(id)

    def options(self):
        return {'405': '(método não permitido)'}

    def patch(self):
        return {'405': '(método não permitido)'}

    def post(self):
        return {'405': '(método não permitido)'}


api.add_resource(AlunosID, '/alunos/<id>')
