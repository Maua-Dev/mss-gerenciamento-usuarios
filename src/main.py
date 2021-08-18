from fastapi import FastAPI

from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_factory import UCFactory
from src.controladores.control_factory_fastapi import ControllerFactoryFastAPI


repo = ArmazenamentoUsuarioVolatil()
useCases = UCFactory(repo)
ctrl = ControllerFactoryFastAPI(useCases)

app = FastAPI()

@app.get("/")
async def root():
    return {"mss": "gerenciamento_usuarios",
            "porta": 8080}

@app.post("/email")
async def adicionarEmail(request: dict):
    return ctrl.cAdicionarEmail(request)

@app.delete("/email")
async def removerEmail(request: dict):
    return ctrl.cRemoverEmail(request)

@app.put("/email")
async def editarEmail(request: dict):
    return ctrl.cEditarEmail(request)

@app.post("/cadastro/")
async def cadastro(request: dict):
    return ctrl.cCadastrarUsuario(request)


@app.post("/telefone")
async def adicionarTelefone(request: dict):
    return ctrl.cAdicionarTelefone(request)

@app.delete("/telefone")
async def removerTelefone(request: dict):
    return ctrl.cRemoverTelefone(request)

@app.put("/telefone")
async def editarTelefone(request: dict):
    return ctrl.cEditarTelefone(request)

@app.post("/endereco")
async def adicionarEndereco(request: dict):
    return ctrl.cAdicionarEndereco(request)

@app.delete("/endereco")
async def removerEndereco(request: dict):
    return ctrl.cRemoverEndereco(request)

@app.put("/endereco")
async def editarEndereco(request: dict):
    return ctrl.cEditarEndereco(request)

@app.delete("/usuario")
async def deletarUsuarioPorEmail(request: dict):
    return ctrl.cDeletarUsuarioPorEmail(request)
