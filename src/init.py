from src.config.proj_config import ProjConfig
from src.config.erros.deployment import *
from src.config.enums.deployment import *
from src.repositorios.mock.armazenamento_aluno_volatil import ArmazenamentoAlunoVolatil
from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.fabricas.controladores.fastapi.fabrica_controlador_fastapi import FabricaControladorFastapi


class Init:
    def __call__(
            self,
            tipo_repo: REPOSITORIO = ProjConfig.getDeployment()[KEY.TIPO_REPOSITORIO.value],
            tipo_ctrl: CONTROLADOR = ProjConfig.getDeployment()[KEY.TIPO_CONTROLADOR.value]
    ):
        # Instanciando tipo de REPOSITORIO
        if tipo_repo == REPOSITORIO.MOCK.value:
            repoUsuario = ArmazenamentoUsuarioVolatil()
            repoAluno = ArmazenamentoAlunoVolatil()
        else:
            raise ErroDeployment1()

        # Instanciando tipo de CONTROLER
        if tipo_ctrl == CONTROLADOR.FASTAPI.value:
            ctrl = FabricaControladorFastapi(repoUsuario, repoAluno)
        else:
            raise ErroDeployment2()

        return repoUsuario, repoAluno, ctrl
