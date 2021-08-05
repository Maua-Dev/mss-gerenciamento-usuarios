from devmaua.src.models.usuario import Usuario
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from uvicorn.middleware.debug import PlainTextResponse

from src.controladores.control_cadastrar_usuario import controlCadastrarUsuario
from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario
from src.usecases.erros.erros_usecase import ErroUsuarioExiste, ErroDadosUsuarioInvalidos
from typing import Any, Dict, AnyStr, List, Union

app = FastAPI()


armazenamento = ArmazenamentoUsuarioVolatil()
cadastrarUsuarioUC = UCCadastrarUsuario(armazenamento)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/cadastro/")
async def cadastro(request: dict):
    return await controlCadastrarUsuario(request, cadastrarUsuarioUC)





