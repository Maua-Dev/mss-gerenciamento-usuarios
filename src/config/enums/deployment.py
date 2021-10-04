from enum import Enum


class KEY(Enum):
    TIPO_DEPLOYMENT = 'tipo_deployment'
    TIPO_REPOSITORIO = 'tipo_repositorio'
    TIPO_CONTROLADOR = 'tipo_controlador'


class DEPLOYMENT(Enum):
    DEV = 'dev'
    PROD = 'prod'


class REPOSITORIO(Enum):
    MOCK = 'mock'


class CONTROLADOR(Enum):
    FASTAPI = 'fastapi'
