from devmaua.src.models.professor import Professor

from src.interfaces.i_repo_professor import IArmazenamentoProfessor
from src.usecases.erros.erros_uc_professor import ErroProfessorNaoEncontrado


class UCEditarProfessor:
    repo: IArmazenamentoProfessor

    def __init__(self, repo: IArmazenamentoProfessor):
        self.repo = repo

    def __call__(self, prof: Professor):
        cond = self.repo.editarProfessor(prof)

        if not cond:
            raise ErroProfessorNaoEncontrado
