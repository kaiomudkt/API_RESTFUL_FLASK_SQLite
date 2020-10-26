from flask import request
from flask_restful import Resource, Api
from service import service
from service.controller.Aluno import AlunoController

api = Api(service)

class Alunos(Resource):

    def get(self):
        limite = request.args['limite']
        pagina = request.args['pagina']
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

'''Este endopoint permite que os usuários do serviço obtenham todos os alunos cadastrados no sistema.
200 (sucesso): Os dados do usuário
404 (não encontrado): Uma mensagem informando que o usuário não foi encontrado.'''
class AlunosID(Resource):

    def get(self, id):
        return AlunoController().get_by_id(id)

    def put(self, id):
        rga = request.form['rga']
        nome = request.form['nome']
        curso = request.form['curso']
        #situacao = request.form['situacao']
        return AlunoController().edit_by_id(id, rga, nome, curso)

    def delet(self, id):
        return AlunoController().delete_by_id(id)

    def options(self):
        return {'405': '(método não permitido)'}

    def patch(self):
        return {'405': '(método não permitido)'}

    def post(self):
        return {'405': '(método não permitido)'}

api.add_resource(AlunosID, '/alunos/<id>')
