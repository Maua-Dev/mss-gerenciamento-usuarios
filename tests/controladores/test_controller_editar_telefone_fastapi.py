from src.controladores.control_editar_telefone_fastapi import ControllerHTTPEditarTelefoneFastAPI
from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_editar_telefone import UCEditarTelefone
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

from devmaua.src.models.usuario import Usuario


class TestControllerEditarTelefoneFastAPI():
    
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
                    "tipo": 2,
                    "numero": "99999-9999",
                    "ddd": 11,
                    "prioridade": 3
                }
    
    def mockRepositorioComUmUsuario(self) -> ArmazenamentoUsuarioVolatil:
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(repositorio)
        usuario = Usuario.criarUsuarioPorDict(self.mockDictUsuario())
        assert isinstance(usuario, Usuario)
        cadastrador(usuario)
        return repositorio
    
            
    def test_controller_editar_telefone_fastapi(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        editarTelefoneUC = UCEditarTelefone(repoVolatil)
        controllerEditarTelefoneFastAPI = ControllerHTTPEditarTelefoneFastAPI()
        
        usuarioDict = self.mockDictUsuario()
        telefoneDict = self.mockDictTelefone()
        body = {
                "usuario": usuarioDict,
                "telefone": telefoneDict,
                "tipo": 3,
                "ddd": 12,
                "numero": '99999-8888',
                "prioridade": 3
            }
        response = controllerEditarTelefoneFastAPI.editarTelefone(body = body, editarTelefoneUC = editarTelefoneUC)
        
        assert response.status_code == 200