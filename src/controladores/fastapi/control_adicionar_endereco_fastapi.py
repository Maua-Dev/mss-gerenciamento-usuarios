from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_endereco import ErroDadosEnderecoInvalidos

from src.usecases.uc_adicionar_endereco import UCAdicionarEndereco

from src.interfaces.interface_alteracao_infos_cadastro import IAlteracaoInfosCadastro

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido

from src.controladores.fastapi.enums.status_code import STATUS_CODE


class ControllerHTTPAdicionarEnderecoFastAPI():

    repo: IAlteracaoInfosCadastro

    def __init__(self, repo: IAlteracaoInfosCadastro):
        self.repo = repo
    
    def __call__(self, body: dict):
        """ Estilo do body:
            {
                "usuario": dict de dicionario,
                "endereco": dict de endereco
            }       
        """
        try:
            adicionarEnderecoUC = UCAdicionarEndereco(self.repo)
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            endereco = Endereco.criarEnderecoPorDict(body['endereco'])
            
            adicionarEnderecoUC(usuario, endereco)
            response = Response(content="Endereco adicionado com sucesso", status_code=STATUS_CODE.OK.value)
        
        except ErroUsuarioInvalido:
            response = Response(content=str(ErroUsuarioInvalido), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except ErroEnderecoInvalido:
            response = Response(content=str(ErroEnderecoInvalido), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except ErroDadosUsuarioInvalidos:
            response = Response(content=str(ErroDadosUsuarioInvalidos), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except ErroDadosEnderecoInvalidos:
            response = Response(content=str(ErroDadosEnderecoInvalidos), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        except KeyError:
            response = Response(content=str(KeyError), status_code=STATUS_CODE.BAD_REQUEST.value)
            
        return response