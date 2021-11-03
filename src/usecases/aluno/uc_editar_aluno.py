from devmaua.src.models.aluno import Aluno

from src.interfaces.i_repo_aluno import IArmazenamentoAluno
from src.usecases.erros.erros_uc_aluno import ErroAlunoNaoEncontrado


class UCEditarAluno:
    repo: IArmazenamentoAluno

    def __init__(self, repo: IArmazenamentoAluno):
        self.repo = repo

    def __call__(self, aluno: Aluno):
        cond = self.repo.editarAluno(aluno)

        if not cond:
            raise ErroAlunoNaoEncontrado
