def getConfigTests():
    conf = {}

    WINDOWS_HOST_IP = '192.168.208.1'

    mysql_config = {
        'MYSQL_HOST': WINDOWS_HOST_IP,
        'MYSQL_USER': 'root',
        'MYSQL_PASSWORD': 'jujuba',
        'MYSQL_DB': 'teste_db',
        'MYSQL_CURSORCLASS': 'DictCursor'
    }

    conf['SECRET_KEY'] = 'secret123'
    conf['SESSION_TYPE'] = 'filesystem'

    conf.update(mysql_config)

    return conf


CONFIG_TEST = getConfigTests()