import logging
from fastapi import Response, status, HTTPException

from devmaua.src.models.aluno import Aluno
from src.interfaces.IRepoAluno import IArmazenamentoAluno
from src.usecases.aluno.uc_deletar_aluno_por_email import UCDeletarAlunoPorEmail
from src.usecases.erros.erros_uc_aluno import ErroAlunoJaCadastrado, ErroEmailInvalido
from src.usecases.erros.erros_usecase import ErroInesperado


class CDeletarAlunoPorEmail:
    repo: IArmazenamentoAluno
    uc: UCDeletarAlunoPorEmail

    def __init__(self, repo: IArmazenamentoAluno):
        self.repo = repo
        self.uc = UCDeletarAlunoPorEmail(self.repo)

    def __call__(self, email: str):

        try:
            self.uc(email)

            return Response(content="Email deletado com sucesso", status_code=status.HTTP_200_OK)

        except ErroEmailInvalido as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}:{str(e)}")
            raise HTTPException(detail=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
