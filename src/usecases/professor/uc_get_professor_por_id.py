from devmaua.src.models.professor import Professor

from src.interfaces.i_repo_professor import IArmazenamentoProfessor
from src.repositorios.erros.erros_armazem_volatil import ErroNaoEncontrado
from src.usecases.erros.erros_uc_professor import ErroProfessorNaoEncontrado


class UCGetProfessorPorID:
    repo: IArmazenamentoProfessor

    def __init__(self, repo: IArmazenamentoProfessor):
        self.repo = repo

    def __call__(self, profId: str) -> Professor:
        try:
            return self.repo.getProfessorPorId(profId)

        # Feito dessa forma para não depender de repo -> No controller não usamos erro de repo, pois é mutavel
        except ErroNaoEncontrado:
            raise ErroProfessorNaoEncontrado()
