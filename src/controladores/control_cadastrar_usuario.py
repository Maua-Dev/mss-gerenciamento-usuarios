from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.usuario import Usuario
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from fastapi import Request, Response
from pydantic import ValidationError




from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario


async def controlCadastrarUsuario(body, cadastrarUsuarioUC: UCCadastrarUsuario):

    try:
        usuario = Usuario.criarUsuarioPorDict(body)
        cadastrarUsuarioUC(usuario)
        response = Response(content="Usuario criado com sucesso", status_code=200)

    except ErroDadosUsuarioInvalidos:
        response = Response(content=ErroDadosUsuarioInvalidos(str(ErroDadosUsuarioInvalidos)), status_code=400)

    return response



