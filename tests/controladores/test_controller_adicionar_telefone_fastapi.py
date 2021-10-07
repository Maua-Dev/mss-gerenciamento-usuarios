from src.controladores.fastapi.c_adicionar_telefone_fastapi import ControllerHTTPAdicionarTelefoneFastAPI
from src.repositorios.mock.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario

from devmaua.src.models.usuario import Usuario


class TestControllerAdicionarTelefoneFastAPI():
    
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
    
            
    def test_controller_adicionar_telefone_fastapi(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        controllerAdicionarTelefoneFastAPI = ControllerHTTPAdicionarTelefoneFastAPI(repoVolatil)
        
        usuario = self.mockDictUsuario()
        telefone = self.mockDictTelefone()
        body = {
                "usuario": usuario,
                "telefone": telefone            
                }
        response = controllerAdicionarTelefoneFastAPI(body = body)

        assert response.status_code == 200
        
    def test_erro_usuario_inexistente(self):
        repoVolatil = ArmazenamentoUsuarioVolatil()
        controllerAdicionarTelefoneFastAPI = ControllerHTTPAdicionarTelefoneFastAPI(repoVolatil)
        
        usuario = self.mockDictUsuario()
        telefone = self.mockDictTelefone()
        body = {
                "usuario": usuario,
                "telefone": telefone            
                }
        response = controllerAdicionarTelefoneFastAPI(body = body)
        assert response.body == b"<class 'src.usecases.erros.erros_uc_alteracao_info_cadastro.ErroUsuarioInvalido'>"
        assert response.status_code == 400
        
    def test_erro_telefone_invalido(self):
        repoVolatil = ArmazenamentoUsuarioVolatil()
        controllerAdicionarTelefoneFastAPI = ControllerHTTPAdicionarTelefoneFastAPI(repoVolatil)
        
        usuario = self.mockDictUsuario()
        telefone = self.mockDictTelefone()
        body = {
                "usuario": usuario,
                "telefone": None            
                }
        response = controllerAdicionarTelefoneFastAPI(body = body)
        
        assert response.body == b"<class 'devmaua.src.models.erros.erro_telefone.ErroDadosTelefoneInvalidos'>"
        assert response.status_code == 400
        
    def test_erro_telefone_vazio(self):
        repoVolatil = ArmazenamentoUsuarioVolatil()
        controllerAdicionarTelefoneFastAPI = ControllerHTTPAdicionarTelefoneFastAPI(repoVolatil)
        
        usuario = self.mockDictUsuario()
        telefone = self.mockDictTelefone()
        body = {
                "usuario": usuario,
                "telefone": None            
                }
        response = controllerAdicionarTelefoneFastAPI(body = body)
        assert response.body == b"<class 'devmaua.src.models.erros.erro_telefone.ErroDadosTelefoneInvalidos'>"
        assert response.status_code == 400
        
    def test_erro_usuario_vazio(self):
        repoVolatil = ArmazenamentoUsuarioVolatil()
        controllerAdicionarTelefoneFastAPI = ControllerHTTPAdicionarTelefoneFastAPI(repoVolatil)
        
        usuario = self.mockDictUsuario()
        telefone = self.mockDictTelefone()
        body = {
                "usuario": None,
                "telefone": telefone            
                }
        response = controllerAdicionarTelefoneFastAPI(body = body)
        assert response.body == b"<class 'devmaua.src.models.erros.erro_usuario.ErroDadosUsuarioInvalidos'>"
        assert response.status_code == 400