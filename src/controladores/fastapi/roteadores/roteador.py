from fastapi import APIRouter

from .rotas.rotas_mss_info import RotasMssInfo
from .rotas.rotas_email import RotasEmail
from .rotas.rotas_endereco import RotasEndereco
from .rotas.rotas_telefone import RotasTelefone
from .rotas.rotas_cadastro import RotasCadastro
from .rotas.rotas_usuario import RotasUsuario


class Roteador(APIRouter):

    def __init__(self, _ctrl):

        super().__init__()

        self.include_router(RotasMssInfo())
        self.include_router(RotasEmail(_ctrl))
        self.include_router(RotasEndereco(_ctrl))
        self.include_router(RotasTelefone(_ctrl))
        self.include_router(RotasUsuario(_ctrl))
        self.include_router(RotasCadastro(_ctrl))












