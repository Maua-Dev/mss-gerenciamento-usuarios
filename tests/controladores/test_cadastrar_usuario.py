import json

import requests.models
from devmaua.src.enum.roles import Roles
from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.usuario import Usuario
from fastapi.testclient import TestClient
from devmaua.src import models

from src.controladores.control_cadastrar_usuario import controlCadastrarUsuario
from src.main import app
from src.repositorios.volatil.armazenamento_usuario_volatil import ArmazenamentoUsuarioVolatil
from src.usecases.erros.erros_usecase import ErroDadosUsuarioInvalidos
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario


class TestControllerCadastrarUsuario():
    controlador = controlCadastrarUsuario
    repoVolatil = ArmazenamentoUsuarioVolatil()
    cadastrarUsuarioUC = UCCadastrarUsuario(repoVolatil)

    def mockUsuario(self):
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

    def test_controller_cadastrar_usuario(self):
        usuario = self.mockUsuario()
        response = controlCadastrarUsuario(body=usuario, cadastrarUsuarioUC=self.cadastrarUsuarioUC)

        assert response.status_code == 200

    def test_controller_cadastrar_sem_nome(self):
        usuario = self.mockUsuario()
        usuario['nome'] = None
        response = controlCadastrarUsuario(body=usuario, cadastrarUsuarioUC=self.cadastrarUsuarioUC)

        assert response.status_code == 400

