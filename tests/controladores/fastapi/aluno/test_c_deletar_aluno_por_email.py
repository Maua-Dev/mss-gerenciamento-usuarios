from unittest.mock import patch, Mock

import pytest
from fastapi import HTTPException

from src.controladores.fastapi.aluno.c_deletar_aluno_por_email import CDeletarAlunoPorEmail
import tests.mock_objetos as mo
from src.usecases.aluno.uc_deletar_aluno_por_email import UCDeletarAlunoPorEmail
from src.usecases.erros.erros_uc_aluno import ErroEmailInvalido
from src.usecases.erros.erros_usecase import ErroInesperado


class TestCDeletarAlunoPorEmail:

    @patch.object(UCDeletarAlunoPorEmail, '__call__')
    def testRespostaOK(self, mockDeletar):
        email = mo.mockEmail().email
        c = CDeletarAlunoPorEmail(Mock())(email)

        assert "Email deletado com sucesso" == c.body.decode()
        assert 200 == c.status_code

        mockDeletar.assert_called_once_with(email)

    @patch.object(UCDeletarAlunoPorEmail, '__call__')
    def testErroEmailInvalido(self, mockDeletar):
        mockDeletar.side_effect = ErroEmailInvalido()

        with pytest.raises(HTTPException) as e:
            CDeletarAlunoPorEmail(Mock())(Mock())

        exc = e.value
        assert 400 == exc.status_code
        assert str(ErroEmailInvalido()) == exc.detail

    @patch.object(UCDeletarAlunoPorEmail, '__call__')
    def testJogaErroInesperado(self, mockDeletar):
        mockDeletar.side_effect = Exception()

        with pytest.raises(HTTPException) as e:
            CDeletarAlunoPorEmail(Mock())(Mock())

        exc = e.value
        assert 500 == exc.status_code
        assert str(ErroInesperado()) == exc.detail
