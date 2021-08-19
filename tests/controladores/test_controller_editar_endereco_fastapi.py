from src.controladores.fastapi.control_editar_endereco_fastapi import ControllerHTTPEditarEnderecoFastAPI
from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_editar_endereco import UCEditarEndereco
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

from devmaua.src.models.usuario import Usuario


class TestControllerEditarEnderecoFastAPI():
    
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
        
    def mockDictEndereco(self):
        return {
                        "logradouro": "rua de tal",
                        "numero": 20,
                        "cep": "00000-000",
                        "complemento": None,
                        "tipo": 1
                    }
    
    def mockRepositorioComUmUsuario(self) -> ArmazenamentoUsuarioVolatil:
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(repositorio)
        usuario = Usuario.criarUsuarioPorDict(self.mockDictUsuario())
        assert isinstance(usuario, Usuario)
        cadastrador(usuario)
        return repositorio
    
            
    def test_controller_editar_endereco_fastapi(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        editarEnderecoUC = UCEditarEndereco(repoVolatil)
        controllerEditarEnderecoFastAPI = ControllerHTTPEditarEnderecoFastAPI()
        
        usuarioDict = self.mockDictUsuario()
        enderecoDict = self.mockDictEndereco()
        body = {
                "usuario": usuarioDict,
                "endereco": enderecoDict,
                "logradouro": "rua nova",
                "numero": 201,
                "cep": "00000-021",
                "complemento": "Atras de outra rua",
                "tipo": 2
            }
        response = controllerEditarEnderecoFastAPI(body = body, editarEnderecoUC = editarEnderecoUC)
        
        assert response.status_code == 200