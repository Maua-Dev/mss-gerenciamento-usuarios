from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.usuario import Usuario
from fastapi import Request, Response
from pydantic import ValidationError



from src.usecases.erros.erros_usecase import ErroDadosUsuarioInvalidos
from src.usecases.uc_cadastrar_usuario import CadastrarUsuario


async def cadastrarUsuario(body, cadastrarUsuarioUC: CadastrarUsuario):

    try:
        email = Email(email=body['contato']['emails'][0]['email'],
                      tipo=body['contato']['emails'][0]['tipo'],
                      prioridade=body['contato']['emails'][0]['prioridade'])

        end = Endereco(logradouro=body['contato']['enderecos'][0]['logradouro'],
                       numero=body['contato']['enderecos'][0]['numero'],
                       cep=body['contato']['enderecos'][0]['cep'],
                       tipo=body['contato']['enderecos'][0]['tipo'],
                       complemento=body['contato']['enderecos'][0]['complemento'])
        tel = Telefone(tipo=body['contato']['telefones'][0]['tipo'],
                       numero=body['contato']['telefones'][0]['numero'],
                       ddd=body['contato']['telefones'][0]['ddd'],
                       prioridade=body['contato']['telefones'][0]['prioridade'])
        contato = Contato(emails=[email],
                          telefones=[tel],
                          enderecos=[end])

        usuario = Usuario(nome=body['nome'],
                           contato=contato,
                           nascimento=body['nascimento'],
                           roles=body['roles'])

    except ValidationError:
        raise ErroDadosUsuarioInvalidos

    except KeyError:
        raise ErroDadosUsuarioInvalidos

    cadastrarUsuarioUC.cadastrar(usuario)

    return Response(content="Usuario criado com sucesso", status_code=200)



