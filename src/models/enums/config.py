from enum import Enum


class CONFIG(Enum):
    def __str__(self):
        return self.value

    NOME_ARQUIVO_CONFIG = 'config.json'
    CAMINHO_CONFIG_CONTROLLER = 'controladores/fastapi/config.json'

    TIPO_DEPLOYMENT = 'deployment_type'
    TIPO_REPOSITORIO = 'repository_type'
    TIPO_CONTROLADOR = 'controller_type'
    MSS = 'mss'
    PORTA = 'porta'
    HOST = 'host'
    PROTOCOLO = 'protocolo'

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

class PORTA(Enum):
    def __str__(self):
        return self.value

    PADRAO = 80
    DEV = 8080

class HOST(Enum):
    def __str__(self):
        return self.value

    LOCALHOST = 'localhost'

class PROTOCOLO(Enum):
    def __str__(self):
        return self.value

    HTTP = 'http'