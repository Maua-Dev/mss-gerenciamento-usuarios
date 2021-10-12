from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_endereco import ErroDadosEnderecoInvalidos

from src.usecases.uc_adicionar_endereco import UCAdicionarEndereco

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido

from http import HTTPStatus
import logging


class ControllerHTTPAdicionarEnderecoFastAPI:
    repo: IArmazenamento
    uc: UCAdicionarEndereco

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCAdicionarEndereco(self.repo)
    
    def __call__(self, body: dict):
        """ Estilo do body:
            {
                "usuario": dict de dicionario,
                "endereco": dict de endereco
            }       
        """
        try:
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            endereco = Endereco.criarEnderecoPorDict(body['endereco'])
            
            self.uc(usuario, endereco)
            return Response(content="Endereço adicionado com sucesso", status_code=HTTPStatus.OK)
        
        except ErroUsuarioNaoExiste as e:
            return Response(content=str(e), status_code=HTTPStatus.NOT_FOUND)
            
        except (ErroEnderecoInvalido, ErroDadosUsuarioInvalidos, ErroDadosEnderecoInvalidos, KeyError) as e:
            return Response(content=str(e), status_code=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            logging.exception("Erro inesperado")
            return Response(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
