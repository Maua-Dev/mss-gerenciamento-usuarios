import logging

from devmaua.src.models.professor import Professor
from fastapi import Response, status, HTTPException

from src.interfaces.i_repo_professor import IArmazenamentoProfessor
from src.usecases.erros.erros_uc_professor import ErroProfessorJaCadastrado
from src.usecases.erros.erros_usecase import ErroInesperado
from src.usecases.professor.uc_cadastrar_professor import UCCadastrarProfessor


class CCadastrarProfessor:
    repo: IArmazenamentoProfessor
    uc: UCCadastrarProfessor

    def __init__(self, repo: IArmazenamentoProfessor):
        self.repo = repo
        self.uc = UCCadastrarProfessor(self.repo)

    def __call__(self, prof: Professor):

        try:
            self.uc(prof)

            return Response(content="Professor criado com sucesso", status_code=status.HTTP_200_OK)

        except (ErroProfessorJaCadastrado, ValueError) as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}:{str(e)}")
            raise HTTPException(detail=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
