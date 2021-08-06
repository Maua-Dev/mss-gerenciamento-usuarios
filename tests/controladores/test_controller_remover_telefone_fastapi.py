from src.controladores.control_remover_telefone_fastapi import ControllerHTTPRemoverTelefoneFastAPI
from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_remover_telefone import UCRemoverTelefone
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

from devmaua.src.models.usuario import Usuario


class TestControllerRemoverTelefoneFastAPI():
    
    def mockDictUsuario(self):
        return {
            "nome": "Jorge Do Teste",
            "contato": {
                "telefones": [
                    {
                        "tipo": 2,
                        "numero": "99999-9999",
                        "ddd": 11,
                        "prioridade": 3
                    },
                    {
                        "tipo":3,
                        "numero":"8888-8888",
                        "ddd":13,
                        "prioridade":2
                    }
                ],
                "emails": [
                    {
                        "email": "teste@teste.com",
                        "tipo": 1,
                        "prioridade": 1
                    }
    
                ],
                "enderecos": [
                    {
                        "logradouro": "rua de tal",
                        "numero": 20,
                        "cep": "00000-000",
                        "complemento": None,
                        "tipo": 1
                    }
                ]
            },
            "nascimento": "1999-02-23",
            "roles": [
                9
            ]
        }
        
    def mockDictTelefone(self):
        return {
                "tipo":3,
                "numero":"8888-8888",
                "ddd":13,
                "prioridade":2
                }
    
    def mockRepositorioComUmUsuario(self) -> ArmazenamentoUsuarioVolatil:
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(repositorio)
        usuario = Usuario.criarUsuarioPorDict(self.mockDictUsuario())
        assert isinstance(usuario, Usuario)
        cadastrador(usuario)
        return repositorio
    
            
    def test_controller_remover_telefone_fastapi(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        removerTelefoneUC = UCRemoverTelefone(repoVolatil)
        controllerRemoverTelefoneFastAPI = ControllerHTTPRemoverTelefoneFastAPI()
        
        usuarioDict = self.mockDictUsuario()
        telefoneDict = self.mockDictTelefone()
        body = {
                "usuario": usuarioDict,
                "telefone": telefoneDict         
                }
        response = controllerRemoverTelefoneFastAPI.removerTelefone(body = body, removerTelefoneUC = removerTelefoneUC)

        assert response.status_code == 200