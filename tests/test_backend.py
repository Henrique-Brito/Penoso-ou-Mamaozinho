import pytest
import requests
import subprocess
from time import sleep


HOST = 'localhost'
PORT = '9999'

"""
    Deve-se iniciar um servidor com a configuracao de testes para
    testar esse trecho
"""


def test_apiDisciplinas():
    expected = [
        {
            "id": 1,
            "nome": "Disciplina A",
            "nome_limpo": "disciplinaa",
            "num_mamao": 0,
            "num_penoso": 1,
            "num_comentarios": 0
        },
        {
            "id": 2,
            "nome": "Disciplina B",
            "nome_limpo": "disciplinab",
            "num_mamao": 0,
            "num_penoso": 1,
            "num_comentarios": 0
        },
        {
            "id": 3,
            "nome": "Disciplina C",
            "nome_limpo": "disciplinac",
            "num_mamao": 0,
            "num_penoso": 1,
            "num_comentarios": 0
        }
    ]

    r = requests.get(f'http://{HOST}:{PORT}/api/disciplinas')

    assert expected == r.json()