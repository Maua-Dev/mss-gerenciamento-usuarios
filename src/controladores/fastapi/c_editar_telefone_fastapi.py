from fastapi import Response

from devmaua.src.models.usuario import Usuario
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.erros.erro_telefone import ErroDadosTelefoneInvalidos

from src.usecases.uc_editar_telefone import UCEditarTelefone

from src.interfaces.IRepoUsuario import IArmazenamento

from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroTelefoneInvalido
from src.usecases.erros.erros_uc_alteracao_info_cadastro import ErroUsuarioNaoExiste

from http import HTTPStatus
import logging


class ControllerHTTPEditarTelefoneFastAPI:
    repo: IArmazenamento
    uc: UCEditarTelefone

    def __init__(self, repo: IArmazenamento):
        self.repo = repo
        self.uc = UCEditarTelefone(self.repo)
    
    def __call__(self, body: dict):
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
            
            self.uc(usuario, telefone, body['tipo'], body['ddd'], body['numero'], body['prioridade'])

            return Response(content="Telefone editado com sucesso", status_code=HTTPStatus.OK)
        
        except ErroUsuarioNaoExiste as e:
            return Response(content=str(e), status_code=HTTPStatus.NOT_FOUND)
            
        except (ErroTelefoneInvalido, ErroDadosUsuarioInvalidos, ErroDadosTelefoneInvalidos, KeyError) as e:
            return Response(content=str(e), status_code=HTTPStatus.BAD_REQUEST)

        except Exception as e:
            logging.exception("Erro inesperado")
            return Response(content="Erro inesperado", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
