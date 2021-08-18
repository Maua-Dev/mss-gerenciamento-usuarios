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


class UCFactory:
    repo: ArmazenamentoUsuarioVolatil

    def __init__(self, repo: ArmazenamentoUsuarioVolatil):
        self.repo = repo

    def ucAdicionarEmail(self):
        return UCAdicionarEmail(self.repo)

    def ucRemoverEmail(self):
        return UCRemoverEmail(self.repo)

    def ucEditarEmail(self):
        return UCEditarEmail(self.repo)

    def ucAdicionarEndereco(self):
        return UCAdicionarEndereco(self.repo)

    def ucRemoverEndereco(self):
        return UCRemoverEndereco(self.repo)

    def ucEditarEndereco(self):
        return UCEditarEndereco(self.repo)

    def ucAdicionarTelefone(self):
        return UCAdicionarTelefone(self.repo)

    def ucRemoverTelefone(self):
        return UCRemoverTelefone(self.repo)

    def ucEditarTelefone(self):
        return UCEditarTelefone(self.repo)

    def ucCadastrarUsuario(self):
        return UCCadastrarUsuario(self.repo)

    def ucDeletarUsuarioPorEmail(self):
        return UCDeletarUsuarioPorEmail(self.repo)