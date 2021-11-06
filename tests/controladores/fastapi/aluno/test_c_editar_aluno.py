from unittest.mock import patch, Mock

import pytest
from fastapi import HTTPException

from src.controladores.fastapi.aluno.c_editar_aluno import CEditarAluno
from src.usecases.aluno.uc_editar_aluno import UCEditarAluno
import tests.mock_objetos as mo
from src.usecases.erros.erros_uc_aluno import ErroAlunoNaoEncontrado
from src.usecases.erros.erros_usecase import ErroInesperado


class TestCEditarAluno:

    @patch.object(UCEditarAluno, '__call__')
    def testRespostaOK(self, mockEditar):

        a = mo.mockAluno()
        c = CEditarAluno(Mock())(a)

        assert "Aluno editado com sucesso" == c.body.decode()
        assert 200 == c.status_code

        mockEditar.assert_called_once_with(a)


    # Define erro generico - não é o teste
    def erroGenerico(self, mockGet, erro, status):
        mockGet.side_effect = erro

        with pytest.raises(HTTPException) as e:
            CEditarAluno(Mock())(Mock())

        exc = e.value
        assert status == exc.status_code
        assert str(erro) == exc.detail


    @patch.object(UCEditarAluno, '__call__')
    def testErroGenerico(self, mockEditar):
        self.erroGenerico(mockEditar, ValueError(), 400)
        self.erroGenerico(mockEditar, ErroAlunoNaoEncontrado(), 404)

    @patch.object(UCEditarAluno, '__call__')
    def testJogaErroInesperado(self, mockEditar):
        mockEditar.side_effect = Exception()

        with pytest.raises(HTTPException) as e:
            CEditarAluno(Mock())(Mock())

        exc = e.value
        assert 500 == exc.status_code
        assert str(ErroInesperado()) == exc.detail

