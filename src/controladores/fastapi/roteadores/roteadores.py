from fastapi import APIRouter, Depends

from src.init import Init
from src.config.proj_config import ProjConfig
from src.controladores.fastapi.http.respostas import *
from src.fabricas.controladores.fastapi.fabrica_controlador_fastapi import FabricaControladorFastapi

roteador = APIRouter(prefix="",
                     dependencies=[Depends(Init)],
                     responses={404: {"description": "Not found"}})
(_, _ctrl) = Init()()


@roteador.get("/", response_model=ResRoot)
async def root():
    req = ResRoot(
        deployment=ProjConfig.getDeployment(),
        controlador=ProjConfig.getFastapi())

    print(req)
    return req

@roteador.post("/email")
async def adicionarEmail(request: dict):
    return _ctrl.adicionarEmail(request)

@roteador.delete("/email")
async def removerEmail(request: dict):
    return _ctrl.removerEmail(request)

@roteador.put("/email")
async def editarEmail(request: dict):
    return _ctrl.editarEmail(request)

@roteador.post("/cadastro/")
async def cadastro(request: dict):
    return _ctrl.cadastrarUsuario(request)


@roteador.post("/telefone")
async def adicionarTelefone(request: dict):
    return _ctrl.adicionarTelefone(request)

@roteador.delete("/telefone")
async def removerTelefone(request: dict):
    return _ctrl.removerTelefone(request)

@roteador.put("/telefone")
async def editarTelefone(request: dict):
    return _ctrl.editarTelefone(request)

@roteador.post("/endereco")
async def adicionarEndereco(request: dict):
    return _ctrl.adicionarEndereco(request)

@roteador.delete("/endereco")
async def removerEndereco(request: dict):
    return _ctrl.removerEndereco(request)

@roteador.put("/endereco")
async def editarEndereco(request: dict):
    return _ctrl.editarEndereco(request)

@roteador.delete("/usuario")
async def deletarUsuarioPorEmail(request: dict):
    return _ctrl.deletarUsuarioPorEmail(request)