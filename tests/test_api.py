import pytest
import os, sys

BACKEND_DIR = os.getenv('ROOT_DIR')
if BACKEND_DIR not in sys.path:
    sys.path.append(BACKEND_DIR)

from backend.api import getDisciplinas
from app import app


# é necessário utilizar o contexto do app ao utilizar funções do flask
@pytest.fixture
def mock_app():
    with app.app_context():
        yield


def test_getDisciplinas(mock_app):
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
    assert expected == getDisciplinas()
