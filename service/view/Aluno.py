from flask import request

from service import service
from service.controller.Aluno import AlunoController



@service.route('/', methods=['GET', 'POST', 'DELETE'])
def users():

    if request.method == 'GET':
        # page = request.args.get('page', default=1, type=int)
        return AlunoController().get_all()
    if request.method == 'POST':
        return "postt"
    if request.method == 'DELETE':
        return "deleteee"
    else:
        return "elseee"



@service.route('/alunos/<int: id>', methods=['GET', 'POST', 'DELETE'])
def user(id):
    """

    @param id:
    @return:
    """
    if request.method == 'GET':
        return AlunoController().get_by_id(id)
    if request.method == 'POST':
        return "postt"
    if request.method == 'DELETE':
        return "deleteee"
    else:
        return "elseee"
