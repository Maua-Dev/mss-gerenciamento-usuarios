from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil

from src.usecases.usuario.uc_adicionar_email import UCAdicionarEmail
from src.usecases.usuario.uc_get_usuario_por_telefone import UCGetUsuarioPorTelefone
from src.usecases.usuario.uc_remover_email import UCRemoverEmail
from src.usecases.usuario.uc_editar_email import UCEditarEmail
from src.usecases.usuario.uc_adicionar_endereco import UCAdicionarEndereco
from src.usecases.usuario.uc_remover_endereco import UCRemoverEndereco
from src.usecases.usuario.uc_editar_endereco import UCEditarEndereco
from src.usecases.usuario.uc_adicionar_telefone import UCAdicionarTelefone
from src.usecases.usuario.uc_remover_telefone import UCRemoverTelefone
from src.usecases.usuario.uc_editar_telefone import UCEditarTelefone
from src.usecases.usuario.uc_cadastrar_usuario import UCCadastrarUsuario
from src.usecases.usuario.uc_deletar_usuario_por_email import UCDeletarUsuarioPorEmail
from src.usecases.usuario.uc_get_usuario_por_userid import UCGetUsuarioPorUserId
from src.usecases.usuario.uc_get_usuario_por_email import UCGetUsuarioPorEmail


class FabricaUsecases:
    repo: ArmazenamentoUsuarioVolatil

    def __init__(self, repo: ArmazenamentoUsuarioVolatil):
        self.repo = repo

    def adicionarEmail(self):
        return UCAdicionarEmail(self.repo)

    def removerEmail(self):
        return UCRemoverEmail(self.repo)

    def editarEmail(self):
        return UCEditarEmail(self.repo)

    def adicionarEndereco(self):
        return UCAdicionarEndereco(self.repo)

    def removerEndereco(self):
        return UCRemoverEndereco(self.repo)

    def editarEndereco(self):
        return UCEditarEndereco(self.repo)

    def adicionarTelefone(self):
        return UCAdicionarTelefone(self.repo)

    def removerTelefone(self):
        return UCRemoverTelefone(self.repo)

    def editarTelefone(self):
        return UCEditarTelefone(self.repo)

    def cadastrarUsuario(self):
        return UCCadastrarUsuario(self.repo)

    def deletarUsuarioPorEmail(self):
        return UCDeletarUsuarioPorEmail(self.repo)

    def getUsuarioPorUserId(self):
        return UCGetUsuarioPorUserId(self.repo)

    def getUsuarioPorEmail(self):
        return UCGetUsuarioPorEmail(self.repo)

    def getUsuarioPorTelefone(self):
        return UCGetUsuarioPorTelefone(self.repo)
