# MSS - Gerenciamento de usuários.
[![codecov](https://codecov.io/gh/Maua-Dev/mss-gerenciamento-usuarios/branch/main/graph/badge.svg?token=SZ815UNBXK)](https://codecov.io/gh/Maua-Dev/mss-gerenciamento-usuarios)


MSS para gerenciamento de usuários cadastrados.

# Instalação

Comece ao clonar o repositório do modo que achar mais adequado.

### Criar um ambiente virtual python:
    py -m venv venv

### Ativar ambiente virtual (*windows*)
    venv\Scripts\activate

### Criar Conda Env:
    conda env create -f environment.yml
    conda activate maua-dev-env

# Uso:

### Desenvolvimento com Docker Composer

Para construir a imagem:

    docker-compose build

Para subir o container:

    docker-compose up

### Iniciar server
    uvicorn src.main:app --reload

### Rodar testes
    pytest

# Autores
## Grupo Backend (Ordem alfabetica):
    Bruna Galastri Guedes
    Bruno Vilardi Bueno
    Felipe Giusti
    Fernando Oliveira
    Nathan Brito da Silva
    Renan Reschke
    Vitor Martin

# Contribuições
Sendo um projeto fechado para alunos da faculdade Mauá, apenas os alunos podem contribuir para o projeto. 
Para mudanças, edições e outros, ver a seção de Issues e procurar a atividade designada a você.

# Licença
No momento, não há licença. 

