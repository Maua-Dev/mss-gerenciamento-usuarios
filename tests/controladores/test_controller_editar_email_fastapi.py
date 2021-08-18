from src.controladores.control_editar_email_fastapi import ControllerHTTPEditarEmailFastAPI
from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_editar_email import UCEditarEmail
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

from devmaua.src.models.usuario import Usuario


class TestControllerEditarEmailFastAPI():
    
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
                    },
                    {
                        "email": "novo@email.com",
                        "tipo": 2,
                        "prioridade": 2
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
        
    def mockDictEmail(self):
        return {
                "email": "novo@email.com",
                "tipo": 2,
                "prioridade": 2
                }
    
    def mockRepositorioComUmUsuario(self) -> ArmazenamentoUsuarioVolatil:
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(repositorio)
        usuario = Usuario.criarUsuarioPorDict(self.mockDictUsuario())
        assert isinstance(usuario, Usuario)
        cadastrador(usuario)
        return repositorio
    
            
    def test_controller_editar_email_fastapi(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        editarEmailUC = UCEditarEmail(repoVolatil)
        controllerEditarEmailFastAPI = ControllerHTTPEditarEmailFastAPI()
        
        usuarioDict = self.mockDictUsuario()
        emailDict = self.mockDictEmail()
        body = {
                "usuario": usuarioDict,
                "email": emailDict,
                "emailNovo": "email@editado.br",
                "tipo": 3,
                "prioridade": 3
                }
        response = controllerEditarEmailFastAPI(body = body, editarEmailUC = editarEmailUC)

        assert response.status_code == 200