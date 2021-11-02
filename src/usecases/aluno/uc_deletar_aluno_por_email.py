from src.interfaces.IRepoAluno import IArmazenamentoAluno
from src.usecases.erros.erros_uc_aluno import ErroEmailInvalido


class UCDeletarAlunoPorEmail:
    repo: IArmazenamentoAluno

    def __init__(self, repo: IArmazenamentoAluno):
        self.repo = repo

    def __call__(self, email: str):
        if not email:
            raise ErroEmailInvalido
        cond = self.repo.deletarAlunoPorEmail(email)
        # Fazer algo com a condicao? Erro não deletado? / não encontrado? acho que não né?

