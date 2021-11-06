from unittest.mock import patch, Mock

import pytest
from fastapi import HTTPException

from src.controladores.fastapi.aluno.c_cadastrar_aluno import CCadastrarAluno
from src.usecases.aluno.uc_cadastrar_aluno import UCCadastrarAluno
import tests.mock_objetos as mo
from src.usecases.erros.erros_uc_aluno import ErroAlunoJaCadastrado
from src.usecases.erros.erros_usecase import ErroInesperado


class TestCCadastrarAluno:

    @patch.object(UCCadastrarAluno, '__call__')
    def testRespostaOK(self, mockCadastrar):

        c = CCadastrarAluno(Mock())(mo.mockAluno())

        assert c.body.decode() == "Aluno criado com sucesso"
        assert c.status_code == 200

        mockCadastrar.assert_called_once_with(mo.mockAluno())

    # Define erro generico - não é o teste
    def erroGenerico(self, mockCadastrar, erro, status):
        mockCadastrar.side_effect = erro

        with pytest.raises(HTTPException) as e:
            CCadastrarAluno(Mock())(mo.mockAluno())

        exc = e.value
        assert status == exc.status_code
        assert str(erro) == exc.detail


    @patch.object(UCCadastrarAluno, '__call__')
    def testErroGenerico(self, mockCadastrar):
        self.erroGenerico(mockCadastrar, ErroAlunoJaCadastrado(), 400)
        self.erroGenerico(mockCadastrar, ValueError(), 400)

    @patch.object(UCCadastrarAluno, '__call__')
    def testJogaErroInesperado(self, mockCadastrar):
        mockCadastrar.side_effect = Exception()

        with pytest.raises(HTTPException) as e:
            CCadastrarAluno(Mock())(mo.mockAluno())

        exc = e.value
        assert 500 == exc.status_code
        assert str(ErroInesperado()) == exc.detail

