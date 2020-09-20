def getConfig():
    conf = {}

    mysql_config = {
        'MYSQL_HOST': 'localhost',
        'MYSQL_USER': 'root',
        'MYSQL_PASSWORD': 'jujuba',
        'MYSQL_DB': 'teste',
        'MYSQL_CURSORCLASS': 'DictCursor'
    }

    conf['SECRET_KEY'] = 'secret123'
    conf['SESSION_TYPE'] = 'filesystem'

    conf.update(mysql_config)

    return conf


CONFIG = getConfig()