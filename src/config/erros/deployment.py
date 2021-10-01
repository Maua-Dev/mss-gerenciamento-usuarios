class ErroDeployment1(Exception):
    def __init__(self):
        super(ErroDeployment1, self).__init__('Erro de configuracao 1')


class ErroDeployment2(Exception):
    def __init__(self):
        super(ErroDeployment2, self).__init__('Erro de configuracao 2')
