from src.usecases.uc_adicionar_email import UCAdicionarEmail
from fastapi import FastAPI

from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil

from src.controladores.control_adicionar_email_fastapi import ControllerHTTPAdicionarEmailFastAPI

app = FastAPI()


armazenamento = ArmazenamentoUsuarioVolatil()
adicionarEmailUC = UCAdicionarEmail(armazenamento)
controllerAdicionarEmail = ControllerHTTPAdicionarEmailFastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/email")
async def adicionarEmail(request: dict):
    return controllerAdicionarEmail.adicionarEmail(request, adicionarEmailUC)
