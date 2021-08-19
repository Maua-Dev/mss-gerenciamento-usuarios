from src.controladores.fastapi.control_adicionar_endereco_fastapi import ControllerHTTPAdicionarEnderecoFastAPI
from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_adicionar_endereco import UCAdicionarEndereco
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

from devmaua.src.models.usuario import Usuario


class TestControllerAdicionarEnderecoFastAPI():
    
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
                    "logradouro": "rua nova",
                    "numero": 201,
                    "cep": "00000-021",
                    "complemento": "Atras de outra rua",
                    "tipo": 2
                }
    
    def mockRepositorioComUmUsuario(self) -> ArmazenamentoUsuarioVolatil:
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(repositorio)
        usuario = Usuario.criarUsuarioPorDict(self.mockDictUsuario())
        assert isinstance(usuario, Usuario)
        cadastrador(usuario)
        return repositorio
    
            
    def test_controller_adicionar_endereco_fastapi(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        adicionarEnderecoUC = UCAdicionarEndereco(repoVolatil)
        controllerAdicionarEnderecoFastAPI = ControllerHTTPAdicionarEnderecoFastAPI()
        
        usuario = self.mockDictUsuario()
        endereco = self.mockDictEndereco()
        body = {
                "usuario": usuario,
                "endereco": endereco            
                }
        response = controllerAdicionarEnderecoFastAPI(body = body, adicionarEnderecoUC = adicionarEnderecoUC)

        assert response.status_code == 200
        
    def test_erro_usuario_inexistente(self):
        repoVolatil = ArmazenamentoUsuarioVolatil()
        adicionarEnderecoUC = UCAdicionarEndereco(repoVolatil)
        controllerAdicionarEnderecoFastAPI = ControllerHTTPAdicionarEnderecoFastAPI()
        
        usuario = self.mockDictUsuario()
        endereco = self.mockDictEndereco()
        body = {
                "usuario": usuario,
                "endereco": endereco            
                }
        response = controllerAdicionarEnderecoFastAPI(body = body, adicionarEnderecoUC = adicionarEnderecoUC)
        assert response.body == b"<class 'src.usecases.erros.erros_uc_alteracao_info_cadastro.ErroUsuarioInvalido'>"
        assert response.status_code == 400
        
    def test_erro_endereco_vazio(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        adicionarEnderecoUC = UCAdicionarEndereco(repoVolatil)
        controllerAdicionarEnderecoFastAPI = ControllerHTTPAdicionarEnderecoFastAPI()
        
        usuario = self.mockDictUsuario()
        endereco = self.mockDictEndereco()
        body = {
                "usuario": usuario,
                "endereco": None            
                }
        response = controllerAdicionarEnderecoFastAPI(body = body, adicionarEnderecoUC = adicionarEnderecoUC)
        assert response.body == b"<class 'devmaua.src.models.erros.erro_endereco.ErroDadosEnderecoInvalidos'>"
        assert response.status_code == 400
        
    def test_erro_usuario_vazio(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        adicionarEnderecoUC = UCAdicionarEndereco(repoVolatil)
        controllerAdicionarEnderecoFastAPI = ControllerHTTPAdicionarEnderecoFastAPI()
        
        usuario = self.mockDictUsuario()
        endereco = self.mockDictEndereco()
        body = {
                "usuario": None,
                "endereco": endereco            
                }
        response = controllerAdicionarEnderecoFastAPI(body = body, adicionarEnderecoUC = adicionarEnderecoUC)
        assert response.body == b"<class 'devmaua.src.models.erros.erro_usuario.ErroDadosUsuarioInvalidos'>"
        assert response.status_code == 400