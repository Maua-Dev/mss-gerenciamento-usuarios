from devmaua.src.models.professor import Professor

from src.interfaces.i_repo_professor import IArmazenamentoProfessor
from src.repositorios.erros.erros_armazem_volatil import ErroNaoEncontrado
from src.usecases.erros.erros_uc_professor import ErroProfessorJaCadastrado


class UCCadastrarProfessor:
    repo: IArmazenamentoProfessor

    def __init__(self, repo: IArmazenamentoProfessor):
        self.repo = repo

    def __call__(self, prof: Professor):
        try:
            if self.repo.getProfessorPorId(prof.ID):
                raise ErroProfessorJaCadastrado

        # Considerar implementação com None ou False
        except ErroNaoEncontrado:
            # Professor nao cadastrado -> cadastrar
            self.repo.cadastrarProfessor(prof)
