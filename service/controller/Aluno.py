from service.model.Aluno import AlunoModel
import json

class AlunoController:
    def __int__(self):
        pass

    '''aplica em massa'''
    def get_all(self, page):
        return AlunoModel().get_all(page)

    def insert(self, data):
        return AlunoModel().insert(data)


    '''aplica unitariamente'''
    def get_by_id(self, id):
        return AlunoModel().get_by_id(id)

    def edit_by_id(self,id, data):
        return AlunoModel().edit_by_id(id, data)

    def delete_by_id(self, id):
        return AlunoModel().delete_by_id(id)