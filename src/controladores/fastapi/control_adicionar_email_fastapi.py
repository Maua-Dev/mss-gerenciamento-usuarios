from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.email import Email
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_email import ErroDadosEmailInvalidos

from src.usecases.uc_adicionar_email import UCAdicionarEmail

from src.interfaces.interface_alteracao_infos_cadastro import IAlteracaoInfosCadastro

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEmailInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido

from src.controladores.fastapi.enums.status_code import STATUS_CODE

class ControllerHTTPAdicionarEmailFastAPI():

    repo: IAlteracaoInfosCadastro

    def __init__(self, repo: IAlteracaoInfosCadastro):
        self.repo = repo
    
    def __call__(self, body: dict):
        
        try:
            adicionarEmailUC = UCAdicionarEmail(self.repo)
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            email = Email.criarEmailPorDict(body['email'])
            
            adicionarEmailUC(usuario, email)
            response = Response(content="Email adicionado com sucesso", status_code=STATUS_CODE.OK.value)
        
        except ErroUsuarioInvalido:
            response = Response(content=str(ErroUsuarioInvalido), status_code=STATUS_CODE.ERRO.value)
            
        except ErroEmailInvalido:
            response = Response(content=str(ErroEmailInvalido), status_code=STATUS_CODE.ERRO.value)
            
        except ErroDadosUsuarioInvalidos:
            response = Response(content=str(ErroDadosUsuarioInvalidos), status_code=STATUS_CODE.ERRO.value)
            
        except ErroDadosEmailInvalidos:
            response = Response(content=str(ErroDadosEmailInvalidos), status_code=STATUS_CODE.ERRO.value)
            
        except KeyError:
            response = Response(content=str(KeyError), status_code=STATUS_CODE.ERRO.value)
            
        return response