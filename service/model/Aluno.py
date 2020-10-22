class AlunoModel:
    def __int__(self):
        pass

    '''aplica em massa'''
    def get_all(self, page):
        return "lista de todos os alunos"

    def insert(self, data):
        return "inseriu no BD "


    '''aplica unitariamente'''
    def get_by_id(self, id):
        return "aludo deste id"

    def edit_by_id(self, id, data):
        return "aplicou edição nos dados deste aluno do ID"

    def delete_by_id(self, id):
        return "removendo alundo deste ID"