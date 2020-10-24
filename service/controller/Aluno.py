from service.model.Aluno import AlunoModel


class AlunoController():
    def __int__(self):
        print("Instanciou AlunoController")

    '''aplica em massa'''

    def get_all(self, limite, pagina):
        return AlunoModel().get_all(limite, pagina)

    def insert(self, rga, nome, curso, situacao):
        print('chegou insert')
        aluno = AlunoModel()
        print(aluno.kaio)
        return AlunoModel().insert(rga, nome, curso, situacao)

    '''aplica unitariamente'''

    def get_by_id(self, id):
        return AlunoModel().get_by_id(id)

    def edit_by_id(self, id, rga, nome, curso):
        return AlunoModel().edit_by_id(id, rga, nome, curso)

    def delete_by_id(self, id):
        return AlunoModel().delete_by_id(id)
