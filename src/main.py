from fastapi import FastAPI

from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil

from src.controladores.control_adicionar_email_fastapi import ControllerHTTPAdicionarEmailFastAPI
from src.usecases.uc_adicionar_email import UCAdicionarEmail

from src.controladores.control_remover_email_fastapi import ControllerHTTPRemoverEmailFastAPI
from src.usecases.uc_remover_email import UCRemoverEmail

from src.controladores.control_editar_email_fastapi import ControllerHTTPEditarEmailFastAPI
from src.usecases.uc_editar_email import UCEditarEmail

from src.controladores.control_cadastrar_usuario import ControllerHTTPCadastrarUsuario
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

from src.controladores.control_adicionar_telefone_fastapi import ControllerHTTPAdicionarTelefoneFastAPI
from src.usecases.uc_adicionar_telefone import UCAdicionarTelefone

from src.controladores.control_remover_telefone_fastapi import ControllerHTTPRemoverTelefoneFastAPI
from src.usecases.uc_remover_telefone import UCRemoverTelefone

from src.controladores.control_editar_telefone_fastapi import ControllerHTTPEditarTelefoneFastAPI
from src.usecases.uc_editar_telefone import UCEditarTelefone

from src.controladores.control_adicionar_endereco_fastapi import ControllerHTTPAdicionarEnderecoFastAPI
from src.usecases.uc_adicionar_endereco import UCAdicionarEndereco

from src.controladores.control_remover_endereco_fastapi import ControllerHTTPRemoverEnderecoFastAPI
from src.usecases.uc_remover_endereco import UCRemoverEndereco


app = FastAPI()

armazenamento = ArmazenamentoUsuarioVolatil()

adicionarEmailUC = UCAdicionarEmail(armazenamento)
controllerAdicionarEmail = ControllerHTTPAdicionarEmailFastAPI()

removerEmailUC = UCRemoverEmail(armazenamento)
controllerRemoverEmail = ControllerHTTPRemoverEmailFastAPI()

editarEmailUC = UCEditarEmail(armazenamento)
controllerEditarEmail = ControllerHTTPEditarEmailFastAPI()

cadastrarUsuarioUC = UCCadastrarUsuario(armazenamento)
controllerCadastrarUsuario = ControllerHTTPCadastrarUsuario()

adicionarTelefoneUC = UCAdicionarTelefone(armazenamento)
controllerAdicionarTelefone = ControllerHTTPAdicionarTelefoneFastAPI()

removerTelefoneUC = UCRemoverTelefone(armazenamento)
controllerRemoverTelefone = ControllerHTTPRemoverTelefoneFastAPI()

editarTelefoneUC = UCEditarTelefone(armazenamento)
controllerEditarTelefone = ControllerHTTPEditarTelefoneFastAPI()

adicionarEnderecoUC = UCAdicionarEndereco(armazenamento)
controllerAdicionarEndereco = ControllerHTTPAdicionarEnderecoFastAPI()

removerEnderecoUC = UCRemoverEndereco(armazenamento)
controllerRemoverEndereco = ControllerHTTPRemoverEnderecoFastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/email")
async def adicionarEmail(request: dict):
    return controllerAdicionarEmail.adicionarEmail(request, adicionarEmailUC)

@app.delete("/email")
async def removerEmail(request: dict):
    return controllerRemoverEmail.removerEmail(request, removerEmailUC = removerEmailUC)

@app.put("/email")
async def editarEmail(request: dict):
    return controllerEditarEmail.editarEmail(request, editarEmailUC = editarEmailUC)

@app.post("/cadastro/")
async def cadastro(request: dict):
    return controllerCadastrarUsuario.cadastrar(request, cadastrarUsuarioUC)

@app.post("/telefone")
async def adicionarTelefone(request: dict):
    return controllerAdicionarTelefone.adicionarTelefone(request, adicionarTelefoneUC = adicionarTelefoneUC)

@app.delete("/telefone")
async def removerTelefone(request: dict):
    return controllerRemoverTelefone.removerTelefone(request, removerTelefoneUC = removerTelefoneUC)

@app.put("/telefone")
async def editarTelefone(request: dict):
    return controllerEditarTelefone.editarTelefone(request, editarTelefoneUC = editarTelefoneUC)

@app.post("/endereco")
async def adicionarEndereco(request: dict):
    return controllerAdicionarEndereco.adicionarEndereco(request, adicionarEnderecoUC = adicionarEnderecoUC)

@app.delete("/endereco")
async def removerEndereco(request: dict):
    return controllerRemoverEndereco.removerEndereco(request, removerEnderecoUC = removerEnderecoUC)
