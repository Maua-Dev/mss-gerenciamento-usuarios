from fastapi import Response, status

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_endereco import ErroDadosEnderecoInvalidos

from src.usecases.uc_editar_endereco import UCEditarEndereco

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroEnderecoInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste

import logging


class ControllerHTTPEditarEnderecoFastAPI:
    repo: IArmazenamento
    uc: UCEditarEndereco

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCEditarEndereco(self.repo)

    def __call__(self, body: dict):
        """ Estrutura do body:
            {
                "usuario": dict de usuario,
                "endereco": dict de endereco,
                "logradouro": Optional[str],
                "numero": Optional[int],
                "cep": Optional[str],
                "complemento": Optional[str],
                "tipo": Optional[TipoEndereco]
            }
        """
        
        try:
            usuario = Usuario.criarUsuarioPorDict(body['usuario'])
            endereco = Endereco.criarEnderecoPorDict(body['endereco'])
            
            self.uc(usuario, endereco, body['logradouro'], body['numero'], body['cep'], body['complemento'], body['tipo'])

            return Response(content="Endereco editado com sucesso", status_code=status.HTTP_200_OK)
        
        except ErroUsuarioNaoExiste as e:
            return Response(content=str(e), status_code=status.HTTP_404_NOT_FOUND)
            
        except (ErroEnderecoInvalido, ErroDadosUsuarioInvalidos, ErroDadosEnderecoInvalidos, KeyError) as e:
            return Response(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logging.exception("Erro inesperado")
            return Response(content="Erro inesperado", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
