import logging
from fastapi import Response, status, HTTPException

from src.interfaces.i_repo_professor import IArmazenamentoProfessor
from src.usecases.erros.erros_usecase import ErroInesperado, ErroEmailInvalido
from src.usecases.professor.uc_deletar_professor_por_email import UCDeletarProfessorPorEmail


class CDeletarProfessorPorEmail:
    repo: IArmazenamentoProfessor
    uc: UCDeletarProfessorPorEmail

    def __init__(self, repo: IArmazenamentoProfessor):
        self.repo = repo
        self.uc = UCDeletarProfessorPorEmail(self.repo)

    def __call__(self, email: str):

        try:
            self.uc(email)

            return Response(content="Professor deletado com sucesso", status_code=status.HTTP_200_OK)

        except ErroEmailInvalido as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}:{str(e)}")
            raise HTTPException(detail=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
