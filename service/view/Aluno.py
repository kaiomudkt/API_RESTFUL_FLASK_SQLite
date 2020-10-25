from flask import request

from service import service
from service.controller.Aluno import AlunoController


@service.route('/alunos', methods=['GET', 'POST', 'DELETE'])
def alunos():
    '''Este endopoint permite que os usuários do serviço obtenham todos os alunos cadastrados no sistema.
    - limite [inteiro, default=25]: Um valor inteiro e positivo indicando a quantidade de alunos a serem retornados.
    - pagina [inteiro, default=1]:  Um valor inteiro e positivo (começando em 1) indicando a página a ser retornada, permitindo assim a navegação sobre diversas páginas de alunos.
    - nome [string]:  Um texto com nome do aluno a ser encontrado na base dados.
    200 (sucesso): Uma lista de alunos que atende aos parâmetros fornecidos.
    400 (parâmetros inválidos): Uma mensagem informando o erro.'''
    if request.method == 'GET':
        limite = request.args['limite']
        pagina = request.args['pagina']
        return AlunoController().get_all(limite, pagina)
    '''Este endopoint permite que os usuários do serviço cadastrem novos alunos no sistema.
    Ao cadastrar um novo usuário o sistema atribui um número de identificação único (id), 
    a data no qual o registro foi inserido (registrado_em) e, por fim, a situação do aluno (situacao, podendo ser "ativo" ou "inativo").
    - rga (obrigatório, string): Número de matrícula do aluno no formato NNNN.NNNN.NNN-N
    - nome (obrigatório, string): Nome do aluno
    - curso (string): Curso no qual o aluno está inserido
    - 201 (sucesso): Retorna um objeto JSON contendo informações de cadastro do usuário. Deve ser retornado também os dados adicionados pelo servidor (id, registrado_em e situacao).
    - 400 (parâmetros inválidos): Uma mensagem informando o erro.'''
    if request.method == 'POST':
        rga = request.form['rga']
        nome = request.form['nome']
        curso = request.form['curso']
        #situacao = request.form['situacao']
        return AlunoController().insert(rga, nome, curso)
    else:
        return "405 (método não permitido)"


@service.route('/alunos/<id>', methods=['GET', 'PUT', 'DELETE'])
def aluno(id):
    '''Este endopoint permite que os usuários do serviço obtenham todos os alunos cadastrados no sistema.
    200 (sucesso): Os dados do usuário
    404 (não encontrado): Uma mensagem informando que o usuário não foi encontrado.'''
    if request.method == 'GET':
        return AlunoController().get_by_id(id)
    '''Este endopoint permite que os usuários do serviço modifiquem informações de um usuário cadastrado no sistema.
    200 (sucesso): Retorna os dados atualizados do aluno
    404 (não encontrado): Uma mensagem informando que o usuário não foi encontrado.'''
    if request.method == 'PUT':
        rga = request.form['rga']
        nome = request.form['nome']
        curso = request.form['curso']
        return AlunoController().edit_by_id(id, rga, nome, curso)
    '''Este endopoint permite que os usuários do serviço removam um usuário cadastrado no sistema.
     200 (sucesso): Retorna os dados do aluno que foi removido
     404 (não encontrado): Uma mensagem informando que o usuário não foi encontrado.'''
    if request.method == 'DELETE':
        return AlunoController().delete_by_id(id)
    else:
        return "405 (método não permitido)"


@service.route('/', methods=['GET'])
def raiz():
    return "use API RestFul for one Aluno by ID, example: http://127.0.0.1:5000/alunos/1 <br> " \
           "in methods HTTP GET or POST  <br>" \
           "or <br> " \
           "use API RestFul for all Alunos, examples: http://127.0.0.1:5000/alunos" \
           "<br> in methods HTTP GET, PUT or DELETE"
