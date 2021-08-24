from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil

from src.usecases.uc_adicionar_email import UCAdicionarEmail
from src.usecases.uc_remover_email import UCRemoverEmail
from src.usecases.uc_editar_email import UCEditarEmail
from src.usecases.uc_adicionar_endereco import UCAdicionarEndereco
from src.usecases.uc_remover_endereco import UCRemoverEndereco
from src.usecases.uc_editar_endereco import UCEditarEndereco
from src.usecases.uc_adicionar_telefone import UCAdicionarTelefone
from src.usecases.uc_remover_telefone import UCRemoverTelefone
from src.usecases.uc_editar_telefone import UCEditarTelefone
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario
from src.usecases.uc_deletar_usuario_por_email import UCDeletarUsuarioPorEmail


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