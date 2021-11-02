from unittest.mock import patch, Mock

import pytest
from fastapi import HTTPException

from src.controladores.fastapi.professor.c_cadastrar_professor import CCadastrarProfessor
import tests.mock_objetos as mo
from src.usecases.erros.erros_uc_professor import ErroProfessorJaCadastrado
from src.usecases.erros.erros_usecase import ErroInesperado
from src.usecases.professor.uc_cadastrar_professor import UCCadastrarProfessor


class TestCCadastrarProfessor:

    @patch.object(UCCadastrarProfessor, '__call__')
    def testRespostaOK(self, mockCadastrar):

        c = CCadastrarProfessor(Mock())(mo.mockProfessor())

        assert c.body.decode() == "Professor criado com sucesso"
        assert c.status_code == 200

        mockCadastrar.assert_called_once_with(mo.mockProfessor())

    # Define erro generico - não é o teste
    def erroGenerico(self, mockCadastrar, erro, status):
        mockCadastrar.side_effect = erro

        with pytest.raises(HTTPException) as e:
            CCadastrarProfessor(Mock())(Mock())

        exc = e.value
        assert status == exc.status_code
        assert str(erro) == exc.detail


    @patch.object(UCCadastrarProfessor, '__call__')
    def testErroGenerico(self, mockCadastrar):
        self.erroGenerico(mockCadastrar, ErroProfessorJaCadastrado(), 400)
        self.erroGenerico(mockCadastrar, ValueError(), 400)

    @patch.object(UCCadastrarProfessor, '__call__')
    def testJogaErroInesperado(self, mockCadastrar):
        mockCadastrar.side_effect = Exception()

        with pytest.raises(HTTPException) as e:
            CCadastrarProfessor(Mock())(Mock())

        exc = e.value
        assert 500 == exc.status_code
        assert str(ErroInesperado()) == exc.detail

