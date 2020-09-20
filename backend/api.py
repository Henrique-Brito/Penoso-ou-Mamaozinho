from backend import app, mysql	
from backend.utils import sanitizeString
    
from passlib.hash import sha256_crypt


def getDisciplinas():
    #create cursor
    cur = mysql.connection.cursor()

    query = """
        SELECT 
            id,
            nome,
            nome_limpo,
            num_mamao,
            num_penoso,
            num_comentarios
        FROM
            disciplinas_informacoes
    """ 

    _ = cur.execute(query)

    disciplinas = cur.fetchall()

    cur.close()

    sort_disciplinas = sorted(disciplinas, key=lambda x: x['nome_limpo'])

    return sort_disciplinas


def getDisciplina(id_disciplina):

    filtro_disciplina = f'WHERE id = {id_disciplina}' if id_disciplina else ''

    cur = mysql.connection.cursor()

    query = f"""
        SELECT 
            id,
            nome,
            nome_limpo,
            num_mamao,
            num_penoso,
            num_comentarios
        FROM
            disciplinas_informacoes
        { filtro_disciplina }
    """ 

    _ = cur.execute(query)

    disciplina = cur.fetchone()

    cur.close()

    return disciplina


def cadastroUsuario(data):
    name = data.get('name')
    email = data.get('email')
    username = data.get('username')
    picture = data.get('picture', '')
    password = sha256_crypt.encrypt(str(data.get('password')))

    # create a cursor to mysqldb
    cur = mysql.connection.cursor()

    # verifica se o username ja foi cadastrado
    result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

    if result > 0:
        return False, 'Username já cadastrado'

    # verifica se o username ja foi cadastrado
    result = cur.execute("SELECT * FROM users WHERE email = %s", [email])

    if result > 0:
        return False, 'Email já cadastrado'

    cur.execute(
        """
            INSERT INTO users(name, email, username, password, picture) 
                VALUES (%s, %s, %s, %s, %s)
        """, 
        (name, email, username, password, picture)
    )

    # commit changes to db
    mysql.connection.commit()

    # close connection to db
    cur.close()

    return True, None


def checkUsuario(username, passwordEntered):

    # create mysql cursor
    cur = mysql.connection.cursor()

    # get user by username
    result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

    if result > 0:
        # get stored hash
        data = cur.fetchone()
        correctPassword = data['password']

        # compare hash with entered hash
        if sha256_crypt.verify(passwordEntered, correctPassword):
            return True, data

    return False, None


def cadastroAvaliacaoDisciplina(categoria, id_disciplina, id_user):
    try:
        id_user = int(id_user)

        # create mysql cursor
        cur = mysql.connection.cursor()

        query = """
                SELECT * FROM (SELECT 
                        *
                    FROM
                        penoso 
                    UNION ALL SELECT 
                        *
                    FROM
                        mamao) AS x
                        
                    WHERE x.id_disciplina = %s AND x.id_user = %s
            """

        # get user by username
        result = cur.execute(query, [id_disciplina, id_user])

        if result > 0:
            return False, 'Voce ja avaliou essa disciplina'

        # adiciona voto de mamao ou penoso para a disiciplina
        cur.execute(
            f"""
                INSERT INTO {categoria}(id_disciplina, id_user) 
                    VALUES (%s, %s)
            """, 
            (id_disciplina, id_user)
        )

        mysql.connection.commit()
    
    except:
        return False, "Um ocorreu enquanto processava"

    return True, None
    

def cadastroAvaliacaoComentario(id_comentario, categoria, id_user):
    try:
        id_user = int(id_user)

        # create mysql cursor
        cur = mysql.connection.cursor()

        query = """
                SELECT * FROM avaliacoes_comentario
                    WHERE id_comentario = %s AND id_user = %s
            """

        # get user by username
        result = cur.execute(query, [id_comentario, id_user])

        if result > 0:
            return False, 'Voce ja avaliou essa disciplina'

        # adiciona voto de mamao ou penoso para a disiciplina
        cur.execute(
            f"""
                INSERT INTO {categoria}(id_comentario, id_user) 
                    VALUES (%s, %s)
            """, 
            (id_comentario, id_user)
        )

        mysql.connection.commit()
    
    except Exception as e:
        print(e)
        return False, "Um ocorreu enquanto processava"

    return True, None
    

def cadastroDisciplina(nome, penoso_mamao, id_user):
    try:
        nome_limpo = ' '.join([sanitizeString(x) for x in nome.split(' ')])
        id_user = int(id_user)
        print("foi")
        # create mysql cursor
        cur = mysql.connection.cursor()

        # get user by username
        result = cur.execute("SELECT * FROM disciplinas WHERE nome_limpo = %s", [nome_limpo])

        if result > 0:
            return False, 'Disciplina ja cadastrada'


        cur.execute(
            """
                INSERT INTO disciplinas(id_user, nome, nome_limpo) 
                    VALUES (%s, %s, %s)
            """, 
            (id_user, nome, nome_limpo)
        )

        mysql.connection.commit()

        insertion = cur.execute("SELECT * FROM disciplinas WHERE nome_limpo = %s", [nome_limpo])
        data = cur.fetchone()
        id_disciplina = data['id']

    except Exception as e:
        print(e)
        return False, "ocorreu um erro enquanto processava"
    
    return cadastroAvaliacaoDisciplina(penoso_mamao, id_disciplina, id_user)


def cadastroComentario(id_user, id_disciplina, texto):
    try:
        id_user = int(id_user)

        # create mysql cursor
        cur = mysql.connection.cursor()

        cur.execute(
            """
                INSERT INTO comentario(id_user, id_disciplina, texto) 
                    VALUES (%s, %s, %s)
            """, 
            (id_user, id_disciplina, texto)
        )

        mysql.connection.commit()

    except:
        return False, "ocorreu um erro enquanto processava"
    
    return True, None


def cadastroLink(id_user, id_disciplina, titulo, link):
    try:
        id_user = int(id_user)

        # create mysql cursor
        cur = mysql.connection.cursor()

        cur.execute(
            """
                INSERT INTO links(id_user, id_disciplina, titulo, link) 
                    VALUES (%s, %s, %s, %s)
            """, 
            (id_user, id_disciplina, titulo, link)
        )

        mysql.connection.commit()

    except:
        return False, "ocorreu um erro enquanto processava"
    
    return True, None


def getComentarios(id_disciplina=None):
    # create mysql cursor
    cur = mysql.connection.cursor()

    filter_disciplina = f'WHERE id_disciplina = {id_disciplina}' if id_disciplina else ''

    query = f"""
        SELECT 
            c.id AS id_comentario,
            MIN(texto) AS texto,
            MIN(picture) AS picture,
            MIN(username) AS username,
            COUNT(g.id) AS num_gostei,
            COUNT(n.id) AS num_nao_gostei
        FROM
            teste.comentario AS c
                INNER JOIN
            users AS u ON c.id_user = u.id
                LEFT JOIN
            gostei AS g ON c.id = g.id_comentario
                LEFT JOIN
            nao_gostei AS n ON c.id = n.id_comentario
        {filter_disciplina}
        GROUP BY c.id;
    """

    _ = cur.execute(query)

    comentarios = cur.fetchall()

    cur.close()

    return comentarios


def getLinks(id_disciplina=None):
    # create mysql cursor
    cur = mysql.connection.cursor()

    filter_disciplina = f'WHERE id_disciplina = {id_disciplina}' if id_disciplina else ''

    query = f"""
        SELECT 
            l.id AS id_link,
            MIN(titulo) AS titulo,
            MIN(link) AS link,
            MIN(picture) AS picture,
            MIN(username) AS username
        FROM
            teste.links AS l
                INNER JOIN
            users AS u ON l.id_user = u.id
        {filter_disciplina}
        GROUP BY l.id;
    """

    _ = cur.execute(query)

    links = cur.fetchall()

    cur.close()

    return links


def getTopDisciplinas(n, categoria):

    TIPOS = ['mamao', 'penoso']


    # create mysql cursor
    cur = mysql.connection.cursor()

    query = f"""
        SELECT 
            id,
            nome,
            num_mamao,
            num_penoso,
            num_comentarios
        FROM
            disciplinas_informacoes
    """

    _ = cur.execute(query)

    disciplinas_informacoes = cur.fetchall()

    cur.close()
    
    if categoria not in TIPOS:
        return {}

    for disciplina in disciplinas_informacoes:
        disciplina['razao'] = disciplina[f'num_mamao']/(disciplina['num_mamao']+disciplina['num_penoso'])
        disciplina['num_votos'] = disciplina['num_mamao']+disciplina['num_penoso']

    reverse = True if categoria == 'mamao' else False

    sort_disciplinas = sorted(disciplinas_informacoes, key=lambda x: x['razao'], reverse=reverse)

    size = min(n, len(sort_disciplinas))

    return sort_disciplinas[:size]
