from unittest.mock import patch, Mock

import pytest
from fastapi import HTTPException

import tests.mock_objetos as mo
from src.controladores.fastapi.professor.c_deletar_professor_por_email import CDeletarProfessorPorEmail
from src.usecases.erros.erros_usecase import ErroInesperado, ErroEmailInvalido
from src.usecases.professor.uc_deletar_professor_por_email import UCDeletarProfessorPorEmail


class TestCDeletarProfessorPorEmail:

    @patch.object(UCDeletarProfessorPorEmail, '__call__')
    def testRespostaOK(self, mockDeletar):
        email = mo.mockEmail().email
        c = CDeletarProfessorPorEmail(Mock())(email)

        assert "Professor deletado com sucesso" == c.body.decode()
        assert 200 == c.status_code

        mockDeletar.assert_called_once_with(email)

    @patch.object(UCDeletarProfessorPorEmail, '__call__')
    def testErroEmailInvalido(self, mockDeletar):
        mockDeletar.side_effect = ErroEmailInvalido()

        with pytest.raises(HTTPException) as e:
            CDeletarProfessorPorEmail(Mock())(Mock())

        exc = e.value
        assert 400 == exc.status_code
        assert str(ErroEmailInvalido()) == exc.detail

    @patch.object(UCDeletarProfessorPorEmail, '__call__')
    def testJogaErroInesperado(self, mockDeletar):
        mockDeletar.side_effect = Exception()

        with pytest.raises(HTTPException) as e:
            CDeletarProfessorPorEmail(Mock())(Mock())

        exc = e.value
        assert 500 == exc.status_code
        assert str(ErroInesperado()) == exc.detail
