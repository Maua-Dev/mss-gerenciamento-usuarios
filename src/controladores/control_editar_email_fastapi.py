from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.email import Email
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_email import ErroDadosEmailInvalidos

from src.usecases.uc_editar_email import UCEditarEmail

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroManipulacaoEmailFaculdade

class ControllerHTTPEditarEmailFastAPI():
    
    def __call__(self, body: dict, editarEmailUC: UCEditarEmail):
        """ Estrutura do body:
            {
                "usuario": dict de usuario,
                "email": dict de email,
                "emailNovo": Optional[str] (novo email),
                "tipo": Optional[TipoEmail] (novo tipo),
                "prioridade": Optional[int] (nova prioridade)
            }
        """
        
        try:
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            email = Email.criarEmailPorDict(body['email'])
            
            editarEmailUC(usuario, email, body['emailNovo'], body['tipo'], body['prioridade'])
            response = Response(content="Email editado com sucesso", status_code=200)
        
        except ErroUsuarioInvalido:
            response = Response(content=str(ErroUsuarioInvalido), status_code=400)
            
        except ErroEmailInvalido:
            response = Response(content=str(ErroEmailInvalido), status_code=400)
            
        except ErroDadosUsuarioInvalidos:
            response = Response(content=str(ErroDadosUsuarioInvalidos), status_code=400)
            
        except ErroDadosEmailInvalidos:
            response = Response(content=str(ErroDadosEmailInvalidos), status_code=400)
            
        except KeyError:
            response = Response(content=str(KeyError), status_code=400)
            
        except ErroManipulacaoEmailFaculdade:
            response = Response(content=str(ErroManipulacaoEmailFaculdade), status_code=400)
                        
        return response