# from service.connectionDB.ConnectionDB import ConnectionDB
from service.model.Aluno import AlunoModel
import re

class AlunoController():
    '''aplica em massa'''

    def get_all(self, limite: int, pagina: int, nome=None):
        return AlunoModel().get_all(limite, pagina, nome)

    def insert(self, rga: str, nome: str, curso: str):
        match = re.findall('\d{4}.\d{4}.\d{3}.\d{1}', rga)
        if not match:
            return {'400': 'RGA inválido'}, 400
        else:
            return AlunoModel().insert(rga, nome, curso)

    '''aplica unitariamente'''

    def get_by_id(self, id: int):
        return AlunoModel().get_by_id(id)

    def edit_by_id(self, id: int, rga: str, nome: str, curso: str, situacao: str):
        return AlunoModel().edit_by_id(id, rga, nome, curso, situacao)

    def delete_by_id(self, id: int):
        return AlunoModel().delete_by_id(id)
