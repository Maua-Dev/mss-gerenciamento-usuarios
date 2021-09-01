from fastapi import FastAPI
import os
import json

from src.init import Init
from src.config import *
from src.controladores.fabricas.fabrica_controlador_fastapi import FabricaControladorFastAPI


ctrl: FabricaControladorFastAPI = Init(_TIPO_REPOSITORIO=TIPO_REPOSITORIO.MOCK, _TIPO_CONTROLADOR=TIPO_CONTROLADOR.FASTAPI)()

app = FastAPI()

@app.get("/")
async def root():
    caminhoRaiz = os.path.dirname(__file__)
    caminhoConfig = os.path.join(caminhoRaiz, CONFIG.NOME_ARQUIVO_CONFIG.value)
    caminhoConfigController = os.path.join(caminhoRaiz, CONFIG.CAMINHO_CONFIG_CONTROLLER.value)
    with open(caminhoConfig) as file1, open(caminhoConfigController) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    return {"mss": data1[CONFIG.MSS.value],
            "porta": data2[CONFIG.PORTA.value]}

@app.post("/email")
async def adicionarEmail(request: dict):
    return ctrl.adicionarEmail(request)

@app.delete("/email")
async def removerEmail(request: dict):
    return ctrl.removerEmail(request)

@app.put("/email")
async def editarEmail(request: dict):
    return ctrl.editarEmail(request)

@app.post("/cadastro/")
async def cadastro(request: dict):
    return ctrl.cadastrarUsuario(request)


@app.post("/telefone")
async def adicionarTelefone(request: dict):
    return ctrl.adicionarTelefone(request)

@app.delete("/telefone")
async def removerTelefone(request: dict):
    return ctrl.removerTelefone(request)

@app.put("/telefone")
async def editarTelefone(request: dict):
    return ctrl.editarTelefone(request)

@app.post("/endereco")
async def adicionarEndereco(request: dict):
    return ctrl.adicionarEndereco(request)

@app.delete("/endereco")
async def removerEndereco(request: dict):
    return ctrl.removerEndereco(request)

@app.put("/endereco")
async def editarEndereco(request: dict):
    return ctrl.editarEndereco(request)

@app.delete("/usuario")
async def deletarUsuarioPorEmail(request: dict):
    return ctrl.deletarUsuarioPorEmail(request)
