import json
from unittest.mock import patch, Mock

import pytest
from fastapi import HTTPException

from src.controladores.fastapi.professor.c_get_professor_por_id import CGetProfessorPorID
import tests.mock_objetos as mo
from src.usecases.erros.erros_uc_professor import ErroProfessorNaoEncontrado
from src.usecases.erros.erros_usecase import ErroInesperado
from src.usecases.professor.uc_get_professor_por_id import UCGetProfessorPorID


class TestCGetProfessorPorID:

    @patch.object(UCGetProfessorPorID, '__call__')
    def testRespostaOK(self, mockGet):
        mockGet.return_value = mo.mockProfessor()

        res = CGetProfessorPorID(Mock())(mo.mockId())

        j = json.loads(res.body)

        assert j["ID"] == mo.mockProfessor().ID and j["nome"] == mo.mockProfessor().nome
        assert res.status_code == 200

        mockGet.assert_called_once_with(mo.mockId())

    # Define erro generico - não é o teste
    def erroGenerico(self, mockGet, erro, status):
        mockGet.side_effect = erro

        with pytest.raises(HTTPException) as e:
            CGetProfessorPorID(Mock())(Mock())

        exc = e.value
        assert status == exc.status_code
        assert str(erro) == exc.detail


    @patch.object(UCGetProfessorPorID, '__call__')
    def testErroGenerico(self, mockGet):
        self.erroGenerico(mockGet, ValueError(), 400)
        self.erroGenerico(mockGet, ErroProfessorNaoEncontrado(), 404)

    @patch.object(UCGetProfessorPorID, '__call__')
    def testJogaErroInesperado(self, mockGet):
        mockGet.side_effect = Exception()

        with pytest.raises(HTTPException) as e:
            CGetProfessorPorID(Mock())(Mock())

        exc = e.value
        assert 500 == exc.status_code
        assert str(ErroInesperado()) == exc.detail

