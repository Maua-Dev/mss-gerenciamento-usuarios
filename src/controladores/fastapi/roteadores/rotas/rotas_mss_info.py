from fastapi import APIRouter

from src.config.proj_config import ProjConfig
from src.controladores.fastapi.http.respostas import *


class RotasMssInfo(APIRouter):

    def __init__(self):

        super().__init__()

        @self.get("/", response_model=ResRoot)
        async def root():
            req = ResRoot(
                deployment=ProjConfig.getDeployment(),
                controlador=ProjConfig.getFastapi())

            print(req)
            return req
