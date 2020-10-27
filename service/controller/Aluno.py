# from service.connectionDB.ConnectionDB import ConnectionDB
from service.model.Aluno import AlunoModel


class AlunoController():
    '''aplica em massa'''

    def get_all(self, limite, pagina):
        return AlunoModel().get_all(limite, pagina)

    def insert(self, rga, nome, curso):
        return AlunoModel().insert(rga, nome, curso)

    '''aplica unitariamente'''

    def get_by_id(self, id):
        return AlunoModel().get_by_id(id)

    def edit_by_id(self, id, rga, nome, curso, situacao):
        return AlunoModel().edit_by_id(id, rga, nome, curso, situacao)

    def delete_by_id(self, id):
        return AlunoModel().delete_by_id(id)
