from devmaua.src.models.ra import RA
from devmaua.src.models.usuario import Usuario

from src.interfaces.interface_gerenciamento_usuarios import IArmazenamento
from src.interfaces.interface_alteracao_infos_cadastro import IAlteracaoInfosCadastro


class ArmazenamentoUsuarioVolatil(IArmazenamento, IAlteracaoInfosCadastro):
    armazem: list[Usuario]

    def __init__(self):
        self.armazem = []


    def usuario_existe(self, outro_usuario: Usuario):
        for u in self.armazem:
            if u.nome == outro_usuario.nome and u.nascimento == outro_usuario.nascimento:
                return True
        return False

    def cadastrar_usuario(self, usuario: Usuario):
        self.armazem.append(usuario)


    def get_usuario(self, ra: RA):
        pass


    def logar_usuario(self, login: str, senha: str):
        pass
    
    def adicionarTelefone(self, usuario: Usuario, telefone: Telefone) -> bool:
        if usuario in self.armazem:
            if telefone != None:
                self.armazem[self.armazem.index(usuario)].contato.telefones.append(telefone)
                return True
        return False