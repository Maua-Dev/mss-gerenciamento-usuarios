from devmaua.src.models.aluno import Aluno
from devmaua.src.models.ra import RA
from devmaua.src.models.usuario import Usuario
from fastapi import FastAPI

from src.controladores.fastapi.aluno.c_cadastrar_aluno import CCadastrarAluno
from src.controladores.fastapi.aluno.c_deletar_aluno_por_email import CDeletarAlunoPorEmail
from src.controladores.fastapi.aluno.c_get_aluno_por_ra import CGetAlunoPorRA
from src.controladores.fastapi.usuario.c_get_usuario_por_userid import CHttpGetUsuarioPorUserIdFastAPI
from src.interfaces.i_repo_aluno import IArmazenamentoAluno
from src.interfaces.i_repo_usuario import IArmazenamentoUsuario
from src.config.enums.fastapi import *
from src.config.proj_config import ProjConfig
from src.controladores.fastapi.roteadores.roteador import Roteador

from src.controladores.fastapi.usuario.c_adicionar_email_fastapi import ControllerHTTPAdicionarEmailFastAPI
from src.controladores.fastapi.usuario.c_remover_email_fastapi import ControllerHTTPRemoverEmailFastAPI
from src.controladores.fastapi.usuario.c_editar_email_fastapi import ControllerHTTPEditarEmailFastAPI
from src.controladores.fastapi.usuario.c_adicionar_endereco_fastapi import ControllerHTTPAdicionarEnderecoFastAPI
from src.controladores.fastapi.usuario.c_remover_endereco_fastapi import ControllerHTTPRemoverEnderecoFastAPI
from src.controladores.fastapi.usuario.c_editar_endereco_fastapi import ControllerHTTPEditarEnderecoFastAPI
from src.controladores.fastapi.usuario.c_adicionar_telefone_fastapi import ControllerHTTPAdicionarTelefoneFastAPI
from src.controladores.fastapi.usuario.c_remover_telefone_fastapi import ControllerHTTPRemoverTelefoneFastAPI
from src.controladores.fastapi.usuario.c_editar_telefone_fastapi import ControllerHTTPEditarTelefoneFastAPI
from src.controladores.fastapi.usuario.c_deletar_usuario_por_email_fastapi import CDeletarUsuarioPorEmailFastAPI
from src.controladores.fastapi.usuario.c_cadastrar_usuario import ControllerHTTPCadastrarUsuario
from src.controladores.fastapi.usuario.c_get_usuario_por_email import CHttpGetUsuarioPorEmailFastAPI
from src.controladores.fastapi.usuario.c_get_usuario_por_telefone import CHttpGetUsuarioPorTelefoneFastAPI


class FabricaControladorFastapi:
    repoUsuario: IArmazenamentoUsuario
    repoAluno: IArmazenamentoAluno

    __config__: dict

    protocolo: str
    host: str
    porta: str
    root: str
    url: str

    app: FastAPI

    def __init__(self, repoUsuario: IArmazenamentoUsuario, repoAluno: IArmazenamentoAluno):
        self.repoUsuario = repoUsuario
        self.repoAluno = repoAluno

        self.__config__ = ProjConfig.getFastapi()

        self.protocolo = self.__config__[KEY.PROTOCOLO.value]
        self.host = self.__config__[KEY.HOST.value]
        self.porta = self.__config__[KEY.PORTA.value]
        self.root = self.__config__[KEY.ROOT.value]
        self.url = f'{self.protocolo}://{self.host}:{self.porta}{self.root}'

        self.app = FastAPI()
        self.app.include_router(Roteador(self))

    def adicionarEmail(self, body: dict):
        return ControllerHTTPAdicionarEmailFastAPI(self.repoUsuario)(body)

    def removerEmail(self, body: dict):
        return ControllerHTTPRemoverEmailFastAPI(self.repoUsuario)(body)

    def editarEmail(self, body: dict):
        return ControllerHTTPEditarEmailFastAPI(self.repoUsuario)(body)

    def adicionarEndereco(self, body: dict):
        return ControllerHTTPAdicionarEnderecoFastAPI(self.repoUsuario)(body)

    def removerEndereco(self, body: dict):
        return ControllerHTTPRemoverEnderecoFastAPI(self.repoUsuario)(body)

    def editarEndereco(self, body: dict):
        return ControllerHTTPEditarEnderecoFastAPI(self.repoUsuario)(body)

    def adicionarTelefone(self, body: dict):
        return ControllerHTTPAdicionarTelefoneFastAPI(self.repoUsuario)(body)

    def removerTelefone(self, body: dict):
        return ControllerHTTPRemoverTelefoneFastAPI(self.repoUsuario)(body)

    def editarTelefone(self, body: dict):
        return ControllerHTTPEditarTelefoneFastAPI(self.repoUsuario)(body)

    def cadastrarUsuario(self, body: Usuario):
        return ControllerHTTPCadastrarUsuario(self.repoUsuario)(body)

    def deletarUsuarioPorEmail(self, body: dict):
        return CDeletarUsuarioPorEmailFastAPI(self.repoUsuario)(body)

    def getUsuarioPorUserId(self, userId: int):
        return CHttpGetUsuarioPorUserIdFastAPI(self.repoUsuario)(userId)

    def getUsuarioPorEmail(self, email: str):
        return CHttpGetUsuarioPorEmailFastAPI(self.repoUsuario)(email)

    def getUsuarioPorTelefone(self, ddd: int, numero: str):
        return CHttpGetUsuarioPorTelefoneFastAPI(self.repoUsuario)(ddd, numero)

# ===== Aluno

    def cadastrarAluno(self, aluno: Aluno):
        return CCadastrarAluno(self.repoAluno)(aluno)

    def deletarAlunoPorEmail(self, email: str):
        return CDeletarAlunoPorEmail(self.repoAluno)(email)

    def getPorRa(self, ra: RA):
        return CGetAlunoPorRA(self.repoAluno)(ra)
