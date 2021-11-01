from fastapi import Response, status

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_endereco import ErroDadosEnderecoInvalidos

from src.usecases.usuario.uc_adicionar_endereco import UCAdicionarEndereco

from src.interfaces.IRepoUsuario import IArmazenamentoUsuario

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido
from src.usecases.erros.erros_usecase import ErroInesperado

import logging


class ControllerHTTPAdicionarEnderecoFastAPI:
    repo: IArmazenamentoUsuario
    uc: UCAdicionarEndereco

    def __init__(self, repo: IArmazenamentoUsuario):
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
            return Response(content="Endereço adicionado com sucesso", status_code=status.HTTP_200_OK)
        
        except ErroUsuarioNaoExiste as e:
            return Response(content=str(e), status_code=status.HTTP_404_NOT_FOUND)
            
        except (ErroEnderecoInvalido, ErroDadosUsuarioInvalidos, ErroDadosEnderecoInvalidos, KeyError) as e:
            return Response(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception(f"{str(ErroInesperado())}:{str(e)}")
            return Response(content=str(ErroInesperado()), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
