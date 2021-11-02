from src.interfaces.i_repo_professor import IArmazenamentoProfessor
from src.usecases.erros.erros_usecase import ErroEmailInvalido


class UCDeletarProfessorPorEmail:
    repo: IArmazenamentoProfessor

    def __init__(self, repo: IArmazenamentoProfessor):
        self.repo = repo

    def __call__(self, email: str):
        if not email:
            raise ErroEmailInvalido
        cond = self.repo.deletarProfessorPorEmail(email)
        # Fazer algo com a condicao? Erro não deletado? / não encontrado? acho que não né?
