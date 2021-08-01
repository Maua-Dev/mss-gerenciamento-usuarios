from devmaua.src.models.ra import RA
from src.interfaces.interface_gerenciamento_usuarios import IArmazenamento


class GetUsuario():

    usuariosRepo: IArmazenamento

    def __init__(self, usuariosRepo: IArmazenamento):
        self.usuariosRepo = usuariosRepo

    def get_por_id(self, id: int):
        try:
            return self.usuariosRepo.get_usuario(id)
        except:
            return False

