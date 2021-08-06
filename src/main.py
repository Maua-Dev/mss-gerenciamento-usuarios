from fastapi import FastAPI

from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil

from src.controladores.control_adicionar_email_fastapi import ControllerHTTPAdicionarEmailFastAPI
from src.usecases.uc_adicionar_email import UCAdicionarEmail

from src.controladores.control_remover_email_fastapi import ControllerHTTPRemoverEmailFastAPI
from src.usecases.uc_remover_email import UCRemoverEmail

from src.controladores.control_cadastrar_usuario import ControllerHTTPCadastrarUsuario
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario


app = FastAPI()

armazenamento = ArmazenamentoUsuarioVolatil()

adicionarEmailUC = UCAdicionarEmail(armazenamento)
controllerAdicionarEmail = ControllerHTTPAdicionarEmailFastAPI()

removerEmailUC = UCRemoverEmail(armazenamento)
controllerRemoverEmail = ControllerHTTPRemoverEmailFastAPI()

cadastrarUsuarioUC = UCCadastrarUsuario(armazenamento)
controllerCadastrarUsuario = ControllerHTTPCadastrarUsuario()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/email")
async def adicionarEmail(request: dict):
    return controllerAdicionarEmail.adicionarEmail(request, adicionarEmailUC)

@app.delete("/email")
async def removerEmail(request: dict):
    return controllerRemoverEmail.removerEmail(request, removerEmailUC = removerEmailUC)

@app.post("/cadastro/")
async def cadastro(request: dict):
    return controllerCadastrarUsuario.cadastrar(request, cadastrarUsuarioUC)