from fastapi import FastAPI

from src.controladores.control_cadastrar_usuario import controlCadastrarUsuario
from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

app = FastAPI()


armazenamento = ArmazenamentoUsuarioVolatil()
cadastrarUsuarioUC = UCCadastrarUsuario(armazenamento)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/cadastro/")
async def cadastro(request: dict):
    return controlCadastrarUsuario(request, cadastrarUsuarioUC)





