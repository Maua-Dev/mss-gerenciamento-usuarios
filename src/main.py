from devmaua.src.models.usuario import Usuario
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from uvicorn.middleware.debug import PlainTextResponse

from src.controladores.control_cadastrar_usuario import cadastrarUsuario
from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_cadastrar_usuario import CadastrarUsuario
from src.usecases.erros.erros_usecase import ErroUsuarioExiste, ErroDadosUsuarioInvalidos
from typing import Any, Dict, AnyStr, List, Union

app = FastAPI()


armazenamento = ArmazenamentoUsuarioVolatil()
cadastrarUsuarioUC = CadastrarUsuario(armazenamento)

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.exception_handler(ErroDadosUsuarioInvalidos)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(status_code=400, content=str(exc))

@app.exception_handler(ErroUsuarioExiste)
async def exception_handler(request, exc):
    return PlainTextResponse(status_code=400, content=str(exc))


@app.post("/cadastro/")
async def cadastro(request: dict):
    return await cadastrarUsuario(request, cadastrarUsuarioUC)





