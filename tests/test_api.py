import pytest
import os, sys

BACKEND_DIR = os.getenv('ROOT_DIR')
if BACKEND_DIR not in sys.path:
    sys.path.append(BACKEND_DIR)

from tests.mock import MockApi
from backend.api import getDisciplinas
from app import app


# é necessário utilizar o contexto do app ao utilizar funções do flask
@pytest.fixture
def app_context():
    with app.app_context():
        yield


def test_getDisciplinas(app_context):
    expected = MockApi.getDisciplinas
    assert expected == getDisciplinas()
