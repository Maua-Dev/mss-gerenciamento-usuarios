import logging
from fastapi import Response, status, HTTPException

from devmaua.src.models.aluno import Aluno
from src.interfaces.i_repo_aluno import IArmazenamentoAluno
from src.usecases.aluno.uc_cadastrar_aluno import UCCadastrarAluno
from src.usecases.erros.erros_uc_aluno import ErroAlunoJaCadastrado
from src.usecases.erros.erros_usecase import ErroInesperado


class CCadastrarAluno:
    repo: IArmazenamentoAluno
    uc: UCCadastrarAluno

    def __init__(self, repo: IArmazenamentoAluno):
        self.repo = repo
        self.uc = UCCadastrarAluno(self.repo)

    def __call__(self, aluno: Aluno):

        try:
            self.uc(aluno)

            return Response(content="Aluno criado com sucesso", status_code=status.HTTP_200_OK)

        except (ErroAlunoJaCadastrado, ValueError) as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}:{str(e)}")
            raise HTTPException(detail=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
