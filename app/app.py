from flask import Flask, render_template, request, session, jsonify
from pickleshare import *
from pymongo import MongoClient
from bson.json_util import dumps

from ejercicios.ordenacion import ordenacion_gnomo
from ejercicios.criba import criba
from ejercicios.regex import aplicar_regex

app = Flask(__name__, static_url_path='/static', template_folder='templates')
app.secret_key = b'wiutqwoirjksdfjsl'
db_pickleshare = PickleShareDB('./app/database')

client = MongoClient("mongo", 27017)
db = client.SampleCollections

# FIXME Y DE TO
# NO HACER ESTO EN LA VIDA REAL
PYTHONHASHSEED = 'fdsfsljfksljfklds39042i4'
# REPITO, QUE NO LO HAGAS
# QUE ES HORRIBLE
# NO TIENE SENTIDO
# LO HAGO PORQUE ES UNA PRÁCTICA DE JUGUETE
# QUE ESTÁ ALMACENADO ASÍ COMO ASÍ EN TEXTO PLANO.
# ESTO Y NADA ES LO MISMO

#
# ──────────────────────────────────────────────────────────── III ──────────
#   :::::: P R A C T I C A   3 : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────
#

@app.route('/mongo', methods=['GET', 'POST'])
def mongo():
    params = {}
    params['queue'] = session['queue']
    puchimones = db.samples_pokemon

    params["tipos"] = ['Bug 🐛', 'Dragon 🐉', 'Electric ⚡', 'Fighting 👊', 'Fire 🔥', 'Flying 🪶', 'Ghost 👻', 'Grass 🌿', 'Ground 🪱', 'Ice ❄️', 'Normal 💥', 'Poison ☠️', 'Psychic 🔮', 'Rock 🪨', 'Water 🌊']

    if request.method == 'POST':
        tipo      = request.form['pokemon_tipo'].split()[0]
        debilidad = request.form['pokemon_debilidad'].split()[0]

        params['tipo_seleccionado']      = request.form['pokemon_tipo']
        params['debilidad_seleccionada'] = request.form['pokemon_debilidad']

        parametros_busqueda = {}

        if tipo != 'Cualquiera':
            parametros_busqueda['type'] = tipo
        if debilidad != 'Cualquiera':
            parametros_busqueda['weaknesses'] = debilidad

        params['lista_pokemon'] = []
        for pokemon in puchimones.find(parametros_busqueda):
            params['lista_pokemon'].append(pokemon)

    return render_template('mongo.html', **params)


# ───────────────────────────────────────────────────────────────── API REST ─────
#  Método   URL          Descripción
#  GET      /pokemon     Pillar todos los Pokémon que contienen en el nombre algo (name_contains)
#  GET      /pokemon/N   Conseguir el pokémon con ID = N
#  POST     /pokemon     Crear pokémon
#  PUT      /pokemon/N   Actualizar info de ID = N
#  DELETE   /pokemon/N   Borrar pokémon con ID = N
# ────────────────────────────────────────────────────────────────────────────────

@app.route('/pokemon', methods=['GET'])
def return_pokemon():
    puchimones = db.samples_pokemon

    listado = []
    peticion = request.get_json()

    if peticion and 'name_contains' in peticion:
        nombre = peticion['name_contains']
        for pokemon in puchimones.find({"name": {'$regex' : nombre}}):
            json_str = dumps(pokemon)
            listado.append(json_str)
    else:
        for pokemon in puchimones.find():
            json_str = dumps(pokemon)
            listado.append(json_str)

    respuesta = jsonify(listado)
    respuesta.status_code = 200

    return respuesta


@app.route('/pokemon/<int:N>', methods=['GET'])
def return_specific_pokemon(N):
    puchimones = db.samples_pokemon
    pokemon = puchimones.find_one({"id": N})

    respuesta = jsonify(dumps(pokemon))
    respuesta.status_code = 200

    return respuesta


@app.route('/pokemon', methods=['POST'])
def create_pokemon():
    puchimones = db.samples_pokemon
    peticion = request.get_json()

    # Deberíamos sanear la petición. Deberíamos. O podría llegarnos el Pokémon Bobby Tables
    # https://xkcd.com/327/

    if 'id' in peticion:
        peticion['id'] = float(peticion['id'])

    respuesta = {"status_code": 200}

    if puchimones.find_one({'id': peticion['id']}):
        respuesta['status_code'] = 500
        respuesta['Error'] = "El Pokémon ya existía en la base de datos"
    else:
        puchimones.insert_one(peticion)

    return respuesta


@app.route('/pokemon/<int:N>', methods=['PUT'])
def update_pokemon(N):
    puchimones = db.samples_pokemon
    peticion = request.get_json()

    puchimones.update_one(
        {'id': N},
        {'$set': {
            "name" : peticion['name']
        }}
    )

    respuesta = jsonify(dumps(puchimones.find_one({'id': N})))
    respuesta.status_code = 200

    return respuesta


@app.route('/pokemon/<int:N>', methods=['DELETE'])
def delete_pokemon(N):
    puchimones = db.samples_pokemon
    estado = puchimones.delete_one({'id': N})

    respuesta = {}
    if estado.deleted_count > 0:
        respuesta['status_code'] = 200
    else:
        respuesta['status_code'] = 404

    return respuesta


#
# ──────────────────────────────────────────────────────────────────────── II ──────────
#   :::::: S E G U N D A   P R A C T I C A : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────────
#

@app.route('/')
@app.route('/index')
def index():
    params = {}

    if 'queue' in session and 'username' in session:
        params['queue'] = session['queue']
        params['username'] = session['username']

    return render_template('index.html', **params)

@app.route('/login', methods=['GET', 'POST'])
def login():
    params = {}
    error = None

    if request.method == 'POST':
        clave = 'users/' + request.form['username']

        if clave not in db_pickleshare:
            error = 'No existe el usuario en la base de datos'
        else:
            print(clave)
            print(db_pickleshare[clave])
            print(hash(request.form['password']))
            if db_pickleshare[clave]["password_cipher"] != hash(request.form['password']):
                error = 'Credenciales incorrectas'
            else:
                params['username'] = request.form['username']
                params['email'] = db_pickleshare[clave]['email']
                params['nombre'] = db_pickleshare[clave]['nombre']
                session['username'] = params['username']

    params['queue'] = session['queue']
    params['error'] = error

    return render_template('login.html', **params)


@app.route('/logout', methods=['GET'])
def logout():
    params = {}

    session['username'] = ''
    session['queue'] = []

    params['queue'] = session['queue']
    params['username'] = session['username']

    return render_template('index.html', **params)


@app.route('/register', methods=['GET', 'POST'])
def register():
    params = {}
    error = None

    password = request.form['password']
    username = request.form['username']

    if not username:
        error = 'El nombre de usuario está vacío'
    if not password:
        error = 'La contraseña está vacía'

    if username and password:
        db_pickleshare['users/' + username] = {
            "password_cipher": hash(password),
            "email": '',
            "nombre": ''
        }
        params['username'] = username
        session['username'] = username

    params['queue'] = session['queue']
    params['error'] = error

    return render_template('login.html', **params)


@app.route('/update_user', methods=['GET', 'POST'])
def update_user():
    params = {}

    username = session['username']
    clave = 'users/' + username

    db_pickleshare[clave]['email'] = request.form['email']
    db_pickleshare[clave]['nombre'] = request.form['nombre']

    params['queue'] = session['queue']

    params['username'] = username
    params['email'] = db_pickleshare[clave]['email']
    params['nombre'] = db_pickleshare[clave]['nombre']

    return render_template('login.html', **params)


@app.after_request
def almacenar_url(response):
    path = request.url[22:]

    if '.svg' not in path:
        queue_reciente(path)

    return response

#
# ──────────────────────────────────────────────────────────────────────── I ──────────
#   :::::: P R I M E R A   P R A C T I C A : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────────
#
#
# ───────────────────────────────────────────────────────── PRIMER EJERCICIO ─────
#

@app.route('/ordenacion', methods=['GET', 'POST'])
def ordenacion():
    params = {}

    if request.method == 'POST' and request.form['numeros']:
        lista = request.form['numeros'].split(" ")
        lista = [int(n) for n in lista]


        ordenacion_gnomo(lista)
        params['numeros'] = lista
        #return ' '.join(str(n) for n in lista)

    params['queue'] = session['queue']
    params['username'] = session['username']
    return render_template("ordenacion.html", **params)


# ────────────────────────────────────────────────────────────────────────────────

@app.route('/criba/<int:n>')
def show_criba(n):
    return ', '.join(str(a) for a in criba(n))

# ────────────────────────────────────────────────────────────────────────────────

@app.route('/regex/<string:cadena>')
def show_regex(cadena):
    print(cadena)
    return aplicar_regex(cadena)


#
# ───────────────────────────────────────────────────────── TERCER EJERCICIO ─────
#

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#
# ────────────────────────────────────────────────────────── EJERCICIO EXTRA ─────
#

@app.route('/svg_extra')
def show_svg_extra():
    return render_template('svg_extra.html')


# ────────────────────────────────────────────────────────────────────────────────

def queue_reciente(nuevo: str, n=3):
    """
    Asume que existe `session`
    """

    if 'queue' not in session or not session['queue']:
        session['queue'] = [' ']*3

    # Shift a la derecha
    ultimo = [session['queue'][-1]]
    session['queue'] = ultimo + session['queue'][:-1]
    session['queue'][0] = nuevo