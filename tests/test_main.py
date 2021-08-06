from fastapi.testclient import TestClient
from devmaua.src import models

from src.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    
def test_adicionar_email():
    response = client.post("/email", 
                          json = {
                                    "usuario": {
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
                                            },
                                    "email": {
                                            "email": "novo@email.com",
                                            "tipo": 2,
                                            "prioridade": 2
                                            }
                                })
    assert response.status_code == 200
