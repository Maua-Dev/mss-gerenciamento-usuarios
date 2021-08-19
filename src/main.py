from fastapi import FastAPI

from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_factory import UCFactory
from src.controladores.fabricas.fabrica_controlador_fastapi import FabricaControladorFastAPI


repo = ArmazenamentoUsuarioVolatil()
useCases = UCFactory(repo)
ctrl = FabricaControladorFastAPI(useCases)

app = FastAPI()

@app.get("/")
async def root():
    return {"mss": "gerenciamento_usuarios",
            "porta": 8080}

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
