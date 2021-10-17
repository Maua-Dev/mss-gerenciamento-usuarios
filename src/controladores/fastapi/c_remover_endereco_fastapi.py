from fastapi import Response, status

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_endereco import ErroDadosEnderecoInvalidos

from src.usecases.uc_remover_endereco import UCRemoverEndereco

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste

import logging


class ControllerHTTPRemoverEnderecoFastAPI:
    repo: IArmazenamento
    uc: UCRemoverEndereco

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCRemoverEndereco(self.repo)

    def __call__(self, body: dict):
        """ Estrutura do body:
            {
                "usuario": dict de usuario,
                "endereco": dict de endereco
            }
        
        """
        
        try:
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            endereco = Endereco.criarEnderecoPorDict(body['endereco'])
            
            self.uc(usuario, endereco)

            return Response(content="Endereco removido com sucesso", status_code=status.HTTP_200_OK)
        
        except ErroUsuarioNaoExiste as e:
            return Response(content=str(e), status_code=status.HTTP_404_NOT_FOUND)
            
        except (ErroEnderecoInvalido, ErroDadosUsuarioInvalidos, ErroDadosEnderecoInvalidos, KeyError) as e:
            return Response(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception("Erro inesperado")
            return Response(content="Erro inesperado", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
