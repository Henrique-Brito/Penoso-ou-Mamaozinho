import os
from tests.config import CONFIG_TEST

def getConfig():
    conf = {}

    WINDOWS_HOST_IP = '192.168.208.1'

    mysql_config = {
        'MYSQL_HOST': WINDOWS_HOST_IP,
        'MYSQL_USER': 'root',
        'MYSQL_PASSWORD': 'jujuba',
        'MYSQL_DB': 'teste',
        'MYSQL_CURSORCLASS': 'DictCursor'
    }

    conf['SECRET_KEY'] = 'secret123'
    conf['SESSION_TYPE'] = 'filesystem'

    conf.update(mysql_config)

    return conf


CONFIG = CONFIG_TEST if os.getenv('TESTS_POM') == 'true' else getConfig()