from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_telefone import ErroDadosTelefoneInvalidos

from src.usecases.uc_editar_telefone import UCEditarTelefone

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroTelefoneInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido


class ControllerHTTPEditarTelefoneFastAPI():
    
    def __call__(self, body: dict, editarTelefoneUC: UCEditarTelefone):
        """ Estrutura do body:
            {
                "usuario": dict de usuario,
                "telefone": dict de telefone,
                "tipo": Optional[TipoTelefone],
                "ddd": Optional[int],
                "numero": Optional[str],
                "prioridade": Optional[int]
            }
        """
        
        try:
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            telefone = Telefone.criarTelefonePorDict(body['telefone'])
            
            editarTelefoneUC(usuario, telefone, body['tipo'], body['ddd'], body['numero'], body['prioridade'])
            response = Response(content="Telefone editado com sucesso", status_code=200)
        
        except ErroUsuarioInvalido:
            response = Response(content=str(ErroUsuarioInvalido), status_code=400)
            
        except ErroTelefoneInvalido:
            response = Response(content=str(ErroTelefoneInvalido), status_code=400)
            
        except ErroDadosUsuarioInvalidos:
            response = Response(content=str(ErroDadosUsuarioInvalidos), status_code=400)
            
        except ErroDadosTelefoneInvalidos:
            response = Response(content=str(ErroDadosTelefoneInvalidos), status_code=400)
            
        except KeyError:
            response = Response(content=str(KeyError), status_code=400)
                            
        return response