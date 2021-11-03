import logging

from devmaua.src.models.aluno import Aluno

from src.interfaces.i_repo_aluno import IArmazenamentoAluno
from src.usecases.aluno.uc_editar_aluno import UCEditarAluno
from fastapi import Response, HTTPException, status

from src.usecases.erros.erros_uc_aluno import ErroAlunoNaoEncontrado
from src.usecases.erros.erros_usecase import ErroInesperado


class CEditarAluno:
    repo: IArmazenamentoAluno
    uc: UCEditarAluno

    def __init__(self, repo: IArmazenamentoAluno):
        self.repo = repo
        self.uc = UCEditarAluno(self.repo)

    def __call__(self, alunoNovo: Aluno):

        try:
            self.uc(alunoNovo)

            return Response(content="Aluno editado com sucesso", status_code=status.HTTP_200_OK)

        except ValueError as e:     # de model <Aluno>
            raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except ErroAlunoNaoEncontrado as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}:{str(e)}")
            raise HTTPException(detail=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
