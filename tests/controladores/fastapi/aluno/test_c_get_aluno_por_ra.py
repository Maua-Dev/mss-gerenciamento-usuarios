from unittest.mock import patch, Mock

import pytest
from fastapi import HTTPException

from src.controladores.fastapi.aluno.c_get_aluno_por_ra import CGetAlunoPorRA
from src.usecases.aluno.uc_get_aluno_por_ra import UCGetAlunoPorRA
import tests.mock_objetos as mo
from src.usecases.erros.erros_uc_aluno import ErroAlunoNaoEncontrado
from src.usecases.erros.erros_usecase import ErroInesperado


class TestCGetAlunoPorRA:

    @patch.object(UCGetAlunoPorRA, '__call__')
    def testRespostaOK(self, mockGet):

        c = CGetAlunoPorRA(Mock())(mo.mockRA())

        assert c.body.decode() == "Email deletado com sucesso"
        assert c.status_code == 200

        mockGet.assert_called_once_with(mo.mockRA())

    # Define erro generico - não é o teste
    def erroGenerico(self, mockGet, erro, status):
        mockGet.side_effect = erro

        with pytest.raises(HTTPException) as e:
            CGetAlunoPorRA(Mock())(Mock())

        exc = e.value
        assert status == exc.status_code
        assert str(erro) == exc.detail


    @patch.object(UCGetAlunoPorRA, '__call__')
    def testErroGenerico(self, mockGet):
        self.erroGenerico(mockGet, ValueError(), 400)
        self.erroGenerico(mockGet, ErroAlunoNaoEncontrado(), 404)

    @patch.object(UCGetAlunoPorRA, '__call__')
    def testJogaErroInesperado(self, mockGet):
        mockGet.side_effect = Exception()

        with pytest.raises(HTTPException) as e:
            CGetAlunoPorRA(Mock())(Mock())

        exc = e.value
        assert 500 == exc.status_code
        assert str(ErroInesperado()) == exc.detail

