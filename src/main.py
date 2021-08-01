from devmaua.src.models.usuario import Usuario
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from uvicorn.middleware.debug import PlainTextResponse

from src.repositorios.volatil.armazenamento_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_cadastrar_usuario import CadastrarUsuario
from src.usecases.erros.erros_usecase import ErroUsuarioExiste

app = FastAPI()


armazenamento = ArmazenamentoUsuarioVolatil()
cadastrador = CadastrarUsuario(armazenamento)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(status_code=400, content="Erro de criação do usuario")

@app.exception_handler(ErroUsuarioExiste)
async def exception_handler(request, exc):
    return PlainTextResponse(status_code=400, content=str(exc))


@app.post("/cadastro/")
async def cadastro(request: Usuario):
    cadastrador.cadastrar(request)
    return request

@app.get("/cadastro/")
async def cadastro_():
    return armazenamento.armazem



