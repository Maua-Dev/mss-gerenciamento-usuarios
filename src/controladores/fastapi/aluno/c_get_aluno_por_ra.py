import logging

from devmaua.src.models.ra import RA

from src.interfaces.IRepoAluno import IArmazenamentoAluno
from src.usecases.aluno.uc_get_aluno_por_ra import UCGetAlunoPorRA
from fastapi import Response, HTTPException, status

from src.usecases.erros.erros_uc_aluno import ErroAlunoNaoEncontrado
from src.usecases.erros.erros_usecase import ErroInesperado


class CGetAlunoPorRA:
    repo: IArmazenamentoAluno
    uc: UCGetAlunoPorRA

    def __init__(self, repo: IArmazenamentoAluno):
        self.repo = repo
        self.uc = UCGetAlunoPorRA(self.repo)

    def __call__(self, ra: RA):

        try:
            self.uc(ra)

            return Response(content="Email deletado com sucesso", status_code=status.HTTP_200_OK)

        except ValueError as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except ErroAlunoNaoEncontrado as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}:{str(e)}")
            raise HTTPException(detail=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
