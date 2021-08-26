from enum import Enum


class CONFIG(Enum):
    def __str__(self):
        return self.value

    NOME_ARQUIVO_CONFIG = 'config.json'

    TIPO_DEPLOYMENT = 'deployment_type'
    TIPO_REPOSITORIO = 'repository_type'
    TIPO_CONTROLADOR = 'controller_type'


class TIPO_DEPLOYMENT(Enum):
    def __str__(self):
        return self.value

    DEV = 'dev'
    PROD = 'prod'


class TIPO_REPOSITORIO(Enum):
    def __str__(self):
        return self.value

    MOCK = 'mock'


class TIPO_CONTROLADOR(Enum):
    def __str__(self):
        return self.value

    FASTAPI = 'fastapi'