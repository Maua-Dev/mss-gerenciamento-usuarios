from devmaua.src.models.aluno import Aluno

from src.interfaces.i_repo_aluno import IArmazenamentoAluno
from src.repositorios.erros.erros_armazem_volatil import ErroNaoEncontrado
from src.usecases.erros.erros_uc_aluno import ErroAlunoJaCadastrado


class UCCadastrarAluno:
    repo: IArmazenamentoAluno

    def __init__(self, repo: IArmazenamentoAluno):
        self.repo = repo

    def __call__(self, aluno: Aluno):
        try:
            if self.repo.getAlunoPorRA(aluno.ra):
                raise ErroAlunoJaCadastrado

        # Considerar implementação com None ou False
        except ErroNaoEncontrado:
            # Aluno nao cadastrado -> cadastrar
            self.repo.cadastrarAluno(aluno)
