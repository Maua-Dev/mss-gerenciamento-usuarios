import json
import os

from src.controladores.fabricas.fabrica_controlador_fastapi import FabricaControladorFastAPI
from src.config import *
from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.models.erros.erros import *


class Init:
    tipoRepositorio: str
    tipoControlador: str
    rotaRaiz: str
    rotaConfig: str

    def __init__(self, _TIPO_REPOSITORIO: TIPO_REPOSITORIO = None, _TIPO_CONTROLADOR: TIPO_CONTROLADOR = None):
        self.rotaRaiz = os.path.dirname(__file__)
        self.rotaConfig = os.path.join(self.rotaRaiz, CONFIG.NOME_ARQUIVO_CONFIG.value)
        with open(self.rotaConfig) as file:
            data = json.load(file)

        if _TIPO_REPOSITORIO == None:
            self.tipoRepositorio = data[CONFIG.TIPO_REPOSITORIO.value]
        else:
            self.tipoRepositorio = _TIPO_REPOSITORIO.value

        if _TIPO_CONTROLADOR == None:
            self.tipoControlador = data[CONFIG.TIPO_CONTROLADOR.value]
        else:
            self.tipoControlador = _TIPO_CONTROLADOR.value

    def __call__(self, *args, **kwargs):

        if self.tipoRepositorio == TIPO_REPOSITORIO.MOCK.value:
            repo = ArmazenamentoUsuarioVolatil()
        else:
            raise ErroRepositorioInvalido

        if self.tipoControlador == TIPO_CONTROLADOR.FASTAPI.value:
            ctrl = FabricaControladorFastAPI(repo)
        else:
            raise ErroControladorInvalido

        return ctrl
