from unittest.mock import patch, Mock

import pytest
from fastapi import HTTPException

import tests.mock_objetos as mo
from src.controladores.fastapi.professor.c_editar_professor import CEditarProfessor
from src.usecases.erros.erros_uc_professor import ErroProfessorNaoEncontrado
from src.usecases.erros.erros_usecase import ErroInesperado
from src.usecases.professor.uc_editar_professor import UCEditarProfessor


class TestCEditarProfessor:

    @patch.object(UCEditarProfessor, '__call__')
    def testRespostaOK(self, mockEditar):

        p = mo.mockProfessor()
        c = CEditarProfessor(Mock())(p)

        assert "Professor editado com sucesso" == c.body.decode()
        assert 200 == c.status_code

        mockEditar.assert_called_once_with(p)


    # Define erro generico - não é o teste
    def erroGenerico(self, mockGet, erro, status):
        mockGet.side_effect = erro

        with pytest.raises(HTTPException) as e:
            CEditarProfessor(Mock())(Mock())

        exc = e.value
        assert status == exc.status_code
        assert str(erro) == exc.detail

    @patch.object(UCEditarProfessor, '__call__')
    def testErroGenerico(self, mockEditar):
        self.erroGenerico(mockEditar, ValueError(), 400)
        self.erroGenerico(mockEditar, ErroProfessorNaoEncontrado(), 404)

    @patch.object(UCEditarProfessor, '__call__')
    def testJogaErroInesperado(self, mockEditar):
        mockEditar.side_effect = Exception()

        with pytest.raises(HTTPException) as e:
            CEditarProfessor(Mock())(Mock())

        exc = e.value
        assert 500 == exc.status_code
        assert str(ErroInesperado()) == exc.detail

