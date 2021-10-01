from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.email import Email
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_email import ErroDadosEmailInvalidos

from src.usecases.uc_editar_email import UCEditarEmail

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroManipulacaoEmailFaculdade

from src.controladores.fastapi.enums.status_code import STATUS_CODE


class ControllerHTTPEditarEmailFastAPI():

    repo: IArmazenamento

    def __init__(self, repo: IArmazenamento):
        self.repo = repo

    def __call__(self, body: dict):
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
            editarEmailUC = UCEditarEmail(self.repo)
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            email = Email.criarEmailPorDict(body['email'])
            
            editarEmailUC(usuario, email, body['emailNovo'], body['tipo'], body['prioridade'])
            response = Response(content="Email editado com sucesso", status_code=STATUS_CODE.OK.value)
        
        except ErroUsuarioInvalido:
            response = Response(content=str(ErroUsuarioInvalido), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except ErroEmailInvalido:
            response = Response(content=str(ErroEmailInvalido), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except ErroDadosUsuarioInvalidos:
            response = Response(content=str(ErroDadosUsuarioInvalidos), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except ErroDadosEmailInvalidos:
            response = Response(content=str(ErroDadosEmailInvalidos), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except KeyError:
            response = Response(content=str(KeyError), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except ErroManipulacaoEmailFaculdade:
            response = Response(content=str(ErroManipulacaoEmailFaculdade), status_code=STATUS_CODE.BAD_REQUEST.value)
                        
        return response