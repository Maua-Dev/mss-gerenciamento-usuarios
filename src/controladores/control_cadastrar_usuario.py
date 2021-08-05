from devmaua.src.models.usuario import Usuario
from devmaua.src.models.erros.erro_usuario import ErroDadosUsuarioInvalidos
from devmaua.src.models.usuario import Usuario
from fastapi import Response

from src.usecases.erros.erros_usecase import ErroUsuarioExiste
from src.usecases.uc_cadastrar_usuario import UCCadastrarUsuario


async def controlCadastrarUsuario(body, cadastrarUsuarioUC: UCCadastrarUsuario):

    try:
        usuario = Usuario.criarUsuarioPorDict(body)
        cadastrarUsuarioUC(usuario)
        response = Response(content="Usuario criado com sucesso", status_code=200)

    except ErroDadosUsuarioInvalidos:
        response = Response(content=ErroDadosUsuarioInvalidos(str(ErroDadosUsuarioInvalidos)), status_code=400)

    except ErroUsuarioExiste:
        response = Response(content=ErroDadosUsuarioInvalidos(str(ErroUsuarioExiste)), status_code=400)

    return response



