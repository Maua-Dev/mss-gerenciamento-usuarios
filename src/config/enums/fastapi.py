from enum import Enum


class KEY(Enum):
    PROTOCOLO = 'protocolo'
    HOST = 'host'
    PORTA = 'porta'
    ROOT = 'root'


class PROTOCOLO(Enum):
    HTTP = 'http'
    HTTPS = 'https'


class HOST(Enum):
    LOCALHOST = 'localhost'
    AWS = 'mr9ezzzhu1.execute-api.sa-east-1.amazonaws.com'


class PORTA(Enum):
    PADRAO = 80
    AWS = ''


class ROOT(Enum):
    PADRAO = '/'
    AWS = '/dev/{NOME_DO_MSS}/'
