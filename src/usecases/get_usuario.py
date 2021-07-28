from devmaua.src.models.ra import RA
from src.interfaces.interface_gerenciamento_usuarios import gerenciamento_usuarios


class getter_usuario():
    usuarios: gerenciamento_usuarios

    def __init__(self, usuarios: gerenciamento_usuarios):
        self.usuarios = usuarios

    def get(self, ra: RA):
        try:
            return self.usuarios.get_usuario(ra)
        except:
            return False
