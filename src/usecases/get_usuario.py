from devmaua.src.models.ra import RA
from src.interfaces.interface_gerenciamento_usuarios import IArmazenamento


class getter_usuario():

    usuarios_repo: IArmazenamento

    def __init__(self, usuarios_repo: IArmazenamento):
        self.usuarios_repo = usuarios_repo

    def get_por_id(self, id: int):
        try:
            return self.usuarios_repo.getUsuario(id)
        except:
            return False

