import logging

from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from src.interfaces.i_repo_professor import IArmazenamentoProfessor

from src.usecases.erros.erros_uc_professor import ErroProfessorNaoEncontrado
from src.usecases.erros.erros_usecase import ErroInesperado
from src.usecases.professor.uc_get_professor_por_id import UCGetProfessorPorID


class CGetProfessorPorID:
    repo: IArmazenamentoProfessor
    uc: UCGetProfessorPorID

    def __init__(self, repo: IArmazenamentoProfessor):
        self.repo = repo
        self.uc = UCGetProfessorPorID(self.repo)

    def __call__(self, profId: str):

        try:
            prof = self.uc(profId)

            content = jsonable_encoder(prof.__dict__)

            return JSONResponse(content=content, status_code=status.HTTP_200_OK)

        except ValueError as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except ErroProfessorNaoEncontrado as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}:{str(e)}")
            raise HTTPException(detail=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
