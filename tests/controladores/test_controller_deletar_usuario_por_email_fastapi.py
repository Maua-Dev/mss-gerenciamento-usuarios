from src.controladores.fastapi.control_deletar_usuario_por_email_fastapi import CDeletarUsuarioPorEmailFastAPI
from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario


from devmaua.src.models.usuario import Usuario


class TestControllerDeletarUsuarioPorEmailFastAPI():
    
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
        
    def mockRepositorioComUmUsuario(self) -> ArmazenamentoUsuarioVolatil:
        repositorio = ArmazenamentoUsuarioVolatil()
        cadastrador = UCCadastrarUsuario(repositorio)
        usuario = Usuario.criarUsuarioPorDict(self.mockDictUsuario())
        assert isinstance(usuario, Usuario)
        cadastrador(usuario)
        return repositorio
    
            
    def test_controller_deletar_usuario_por_email_fastapi(self):
        repoVolatil = self.mockRepositorioComUmUsuario()
        controllerDeletarUsuarioPorEmail = CDeletarUsuarioPorEmailFastAPI(repoVolatil)
        
        body = {
                    "email": "teste@teste.com"
               }
        
        response = controllerDeletarUsuarioPorEmail(body = body)
        assert response.status_code == 200
        assert repoVolatil.usuarioExistePorEmail("teste@teste.com") == False
        
    def test_erro_usuario_inexistente(self):
        repoVolatil = ArmazenamentoUsuarioVolatil()
        controllerDeletarUsuarioPorEmail = CDeletarUsuarioPorEmailFastAPI(repoVolatil)
        
        body = {
                    "email": "teste@teste.com"
               }
        response = controllerDeletarUsuarioPorEmail(body = body)
        assert response.body == b"<class 'src.usecases.erros.erros_uc_alteracao_info_cadastro.ErroUsuarioInvalido'>"
        assert response.status_code == 400