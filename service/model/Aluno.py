class AlunoModel:
    def __int__(self):
        pass

    '''aplica em massa'''

    def get_all(self, limite, pagina):
        return "lista de todos os alunos da pagina " + pagina + " em " + limite

    def insert(self, rga, nome, curso):
        return "inseriu no BD novo aluno com RGA: " + rga + ' nome: ' + nome + ' Curso:' + curso

    '''aplica unitariamente'''

    def get_by_id(self, id):
        return "aludo deste id: "+id

    def edit_by_id(self, id, rga, nome, curso):
        return "aplicou edição nos dados deste aluno do ID " + id + " rga" + rga + " nome " + nome + " curso " + curso

    def delete_by_id(self, id):
        return "removendo alundo deste ID "+id
