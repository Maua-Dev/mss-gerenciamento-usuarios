from devmaua.src.models.aluno import Aluno
from devmaua.src.models.ra import RA

from src.interfaces.i_repo_aluno import IArmazenamentoAluno
from src.repositorios.erros.erros_armazem_volatil import ErroNaoEncontrado
from src.usecases.erros.erros_uc_aluno import ErroAlunoNaoEncontrado


class UCGetAlunoPorRA:
    repo: IArmazenamentoAluno

    def __init__(self, repo: IArmazenamentoAluno):
        self.repo = repo

    def __call__(self, ra: RA) -> Aluno:
        try:
            return self.repo.getAlunoPorRA(ra)

        # Feito dessa forma para não depender de repo -> No controller não usamos erro de repo, pois é mutavel
        except ErroNaoEncontrado:
            raise ErroAlunoNaoEncontrado()
