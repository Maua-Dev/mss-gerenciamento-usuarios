from src.controladores.control_adicionar_email_fastapi import ControllerHTTPAdicionarEmailFastAPI
from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_adicionar_email import UCAdicionarEmail
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

from devmaua.src.models.usuario import Usuario


class TestControllerAdicionarEmailFastAPI():
    
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
    
            
    def test_controller_adicionar_email_fastapi(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        adicionarEmailUC = UCAdicionarEmail(repoVolatil)
        controllerAdicionarEmailFastAPI = ControllerHTTPAdicionarEmailFastAPI()
        
        usuario = self.mockDictUsuario()
        email = self.mockDictEmail()
        body = {
                "usuario": usuario,
                "email": email            
                }
        response = controllerAdicionarEmailFastAPI.adicionarEmail(body = body, adicionarEmailUC = adicionarEmailUC)

        assert response.status_code == 200
        
    def test_erro_usuario_inexistente(self):
        repoVolatil = ArmazenamentoUsuarioVolatil()
        adicionarEmailUC = UCAdicionarEmail(repoVolatil)
        controllerAdicionarEmailFastAPI = ControllerHTTPAdicionarEmailFastAPI()
        
        usuario = self.mockDictUsuario()
        email = self.mockDictEmail()
        body = {
                "usuario": usuario,
                "email": email            
                }
        response = controllerAdicionarEmailFastAPI.adicionarEmail(body = body, adicionarEmailUC = adicionarEmailUC)
        assert response.body == b"<class 'src.usecases.erros.erros_uc_alteracao_info_cadastro.ErroUsuarioInvalido'>"
        assert response.status_code == 400
        
    def test_erro_email_invalido(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        adicionarEmailUC = UCAdicionarEmail(repoVolatil)
        controllerAdicionarEmailFastAPI = ControllerHTTPAdicionarEmailFastAPI()
        
        usuario = self.mockDictUsuario()
        email = self.mockDictEmail()
        body = {
                "usuario": usuario,
                "email": {
                        "email": None,
                        "tipo": 2,
                        "prioridade": 2
                        }
           
                }
        response = controllerAdicionarEmailFastAPI.adicionarEmail(body = body, adicionarEmailUC = adicionarEmailUC)
        assert response.body == b"<class 'devmaua.src.models.erros.erro_email.ErroDadosEmailInvalidos'>"
        assert response.status_code == 400
        
    def test_erro_email_vazio(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        adicionarEmailUC = UCAdicionarEmail(repoVolatil)
        controllerAdicionarEmailFastAPI = ControllerHTTPAdicionarEmailFastAPI()
        
        usuario = self.mockDictUsuario()
        email = self.mockDictEmail()
        body = {
                "usuario": usuario,
                "email": None
                }
        response = controllerAdicionarEmailFastAPI.adicionarEmail(body = body, adicionarEmailUC = adicionarEmailUC)
        assert response.body == b"<class 'devmaua.src.models.erros.erro_email.ErroDadosEmailInvalidos'>"
        assert response.status_code == 400
        
    def test_erro_usuario_vazio(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        adicionarEmailUC = UCAdicionarEmail(repoVolatil)
        controllerAdicionarEmailFastAPI = ControllerHTTPAdicionarEmailFastAPI()
        
        usuario = self.mockDictUsuario()
        email = self.mockDictEmail()
        body = {
                "usuario": None,
                "email": {
                        "email": None,
                        "tipo": 2,
                        "prioridade": 2
                        }
                }
        response = controllerAdicionarEmailFastAPI.adicionarEmail(body = body, adicionarEmailUC = adicionarEmailUC)
        assert response.body == b"<class 'devmaua.src.models.erros.erro_usuario.ErroDadosUsuarioInvalidos'>"
        assert response.status_code == 400