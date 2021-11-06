import logging

from devmaua.src.models.professor import Professor
from fastapi import Response, HTTPException, status

from src.interfaces.i_repo_professor import IArmazenamentoProfessor
from src.usecases.erros.erros_uc_professor import ErroProfessorNaoEncontrado
from src.usecases.erros.erros_usecase import ErroInesperado
from src.usecases.professor.uc_editar_professor import UCEditarProfessor


class CEditarProfessor:
    repo: IArmazenamentoProfessor
    uc: UCEditarProfessor

    def __init__(self, repo: IArmazenamentoProfessor):
        self.repo = repo
        self.uc = UCEditarProfessor(self.repo)

    def __call__(self, profNovo: Professor):

        try:
            self.uc(profNovo)

            return Response(content="Professor editado com sucesso", status_code=status.HTTP_200_OK)

        except ValueError as e:     # de model <Professor>
            raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except ErroProfessorNaoEncontrado as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}:{str(e)}")
            raise HTTPException(detail=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
