from flask import request, jsonify
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
        req = request.get_json()
        rga = req['rga']
        nome = req['nome']
        curso = req['curso']
        return AlunoController().insert(rga, nome, curso)

    def delete(self):
        return {'405': '(método não permitido)'}, 405

    def put(self):
        return {'405': '(método não permitido)'}, 405

    def patch(self):
        return {'405': '(método não permitido)'}, 405

    def options(self):
        return {'405': '(método não permitido)'}, 405


api.add_resource(Alunos, '/alunos')


class AlunosID(Resource):

    def get(self, id: int):
        return AlunoController().get_by_id(id)

    def put(self, id: int):
        req = request.get_json()
        rga = req['rga']
        nome = req['nome']
        curso = req['curso']
        situacao = req['situacao']
        return AlunoController().edit_by_id(id, rga, nome, curso, situacao)

    def delete(self, id: int):
        return AlunoController().delete_by_id(id)

    def post(self, id: int):
        return {'405': '(método não permitido)'}, 405

api.add_resource(AlunosID, '/alunos/<id>')

@api.resource('/alunos/')
class Foo(Resource):
    def get(self):
        return {"404": "ID não informado!"}