from src.usecases.uc_factory import UCFactory

from src.controladores.control_adicionar_email_fastapi import ControllerHTTPAdicionarEmailFastAPI
from src.controladores.control_remover_email_fastapi import ControllerHTTPRemoverEmailFastAPI
from src.controladores.control_editar_email_fastapi import ControllerHTTPEditarEmailFastAPI
from src.controladores.control_adicionar_endereco_fastapi import ControllerHTTPAdicionarEnderecoFastAPI
from src.controladores.control_remover_endereco_fastapi import ControllerHTTPRemoverEnderecoFastAPI
from src.controladores.control_editar_endereco_fastapi import ControllerHTTPEditarEnderecoFastAPI
from src.controladores.control_adicionar_telefone_fastapi import ControllerHTTPAdicionarTelefoneFastAPI
from src.controladores.control_remover_telefone_fastapi import ControllerHTTPRemoverTelefoneFastAPI
from src.controladores.control_editar_telefone_fastapi import ControllerHTTPEditarTelefoneFastAPI
from src.controladores.control_deletar_usuario_por_email_fastapi import CDeletarUsuarioPorEmailFastAPI
from src.controladores.control_cadastrar_usuario import ControllerHTTPCadastrarUsuario


class ControllerFactoryFastAPI:
    _useCases: UCFactory

    def __init__(self, _useCases: UCFactory):
        self._useCases = _useCases

    def cAdicionarEmail(self, body: dict):
        return ControllerHTTPAdicionarEmailFastAPI()(body, self._useCases.ucAdicionarEmail())

    def cRemoverEmail(self, body: dict):
        return ControllerHTTPRemoverEmailFastAPI()(body, self._useCases.ucRemoverEmail())

    def cEditarEmail(self, body: dict):
        return ControllerHTTPEditarEmailFastAPI()(body, self._useCases.ucEditarEmail())

    def cAdicionarEndereco(self, body: dict):
        return ControllerHTTPAdicionarEnderecoFastAPI()(body, self._useCases.ucAdicionarEndereco())

    def cRemoverEndereco(self, body: dict):
        return ControllerHTTPRemoverEnderecoFastAPI()(body, self._useCases.ucRemoverEndereco())

    def cEditarEndereco(self, body: dict):
        return ControllerHTTPEditarEnderecoFastAPI()(body, self._useCases.ucEditarEndereco())

    def cAdicionarTelefone(self, body: dict):
        return ControllerHTTPAdicionarTelefoneFastAPI()(body, self._useCases.ucAdicionarTelefone())

    def cRemoverTelefone(self, body: dict):
        return ControllerHTTPRemoverTelefoneFastAPI()(body, self._useCases.ucRemoverTelefone())

    def cEditarTelefone(self, body: dict):
        return ControllerHTTPEditarTelefoneFastAPI()(body, self._useCases.ucEditarTelefone())

    def cCadastrarUsuario(self, body: dict):
        return ControllerHTTPCadastrarUsuario()(body, self._useCases.ucCadastrarUsuario())

    def cDeletarUsuarioPorEmail(self, body: dict):
        return CDeletarUsuarioPorEmailFastAPI()(body, self._useCases.ucDeletarUsuarioPorEmail())