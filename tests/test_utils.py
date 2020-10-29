import pytest
import os, sys

BACKEND_DIR = os.getenv('ROOT_DIR')
if BACKEND_DIR not in sys.path:
    sys.path.append(BACKEND_DIR)

from backend.utils import success_response, error_response, sanitizeString
from app import app


# é necessário utilizar o contexto do app ao utilizar funções do flask
@pytest.fixture
def app_context():
    with app.app_context():
        yield


def test_sanitizeString():
    string = 'Olá Mundo!'
    sanitized = 'olamundo'
    assert sanitized == sanitizeString(string)


def test_success_response(app_context):
    data = {
        'test1': 123,
        'test2': 'testing',
        'test3': 123.123
    }
    expected1 = {
        'status': 'success'
    }
    expected1.update(data)
    expected2 = {'status': 'success'}
    expected3 = {'status': 'error'}
    assert expected1 == success_response(data).get_json()
    assert expected2 == success_response().get_json()
    assert expected3 != success_response().get_json()


def test_error_response(app_context):
    message = 'error message'
    expected1 = {
        'status': 'error',
        'message': message
    }
    expected2 = {
        'status': 'error', 
        'message': ''
    }
    expected3 = {'status': 'success'}
    assert expected1 == error_response(message).get_json()
    assert expected2 == error_response().get_json()
    assert expected3 != error_response().get_json()
