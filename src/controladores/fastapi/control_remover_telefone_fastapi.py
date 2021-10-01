from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_telefone import ErroDadosTelefoneInvalidos

from src.usecases.uc_remover_telefone import UCRemoverTelefone

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroTelefoneInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido

from src.controladores.fastapi.enums.status_code import STATUS_CODE


class ControllerHTTPRemoverTelefoneFastAPI():

    repo: IArmazenamento

    def __init__(self, repo: IArmazenamento):
        self.repo = repo

    def __call__(self, body: dict):
        """ Estrutura do body:
            {
                "usuario": dict de usuario,
                "telefone": dict de telefone
            }
        
        """
        
        try:
            removerTelefoneUC = UCRemoverTelefone(self.repo)
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            telefone = Telefone.criarTelefonePorDict(body['telefone'])
            
            removerTelefoneUC(usuario, telefone)
            response = Response(content="Telefone removido com sucesso", status_code=STATUS_CODE.OK.value)
        
        except ErroUsuarioInvalido:
            response = Response(content=str(ErroUsuarioInvalido), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except ErroTelefoneInvalido:
            response = Response(content=str(ErroTelefoneInvalido), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except ErroDadosUsuarioInvalidos:
            response = Response(content=str(ErroDadosUsuarioInvalidos), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except ErroDadosTelefoneInvalidos:
            response = Response(content=str(ErroDadosTelefoneInvalidos), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except KeyError:
            response = Response(content=str(KeyError), status_code=STATUS_CODE.BAD_REQUEST.value)
                        
        return response