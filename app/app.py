from flask import Flask, render_template, request, flash, url_for, redirect, session
from pickleshare import *

from ejercicios.ordenacion import ordenacion_gnomo
from ejercicios.criba import criba
from ejercicios.regex import aplicar_regex

app = Flask(__name__, static_url_path='/static', template_folder='templates')
app.secret_key = b'wiutqwoirjksdfjsl'
db = PickleShareDB('./app/database')

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
# ──────────────────────────────────────────────────────────────────────── II ──────────
#   :::::: S E G U N D A   P R A C T I C A : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────────
#

@app.route('/')
@app.route('/index')
def index():
    params = {}

    params['queue'] = session['queue']
    params['username'] = session['username']

    return render_template('index.html', **params)

@app.route('/login', methods=['GET', 'POST'])
def login():
    params = {}
    error = None

    if request.method == 'POST':
        clave = 'users/' + request.form['username']

        if clave not in db:
            error = 'No existe el usuario en la base de datos'
        else:
            print(clave)
            print(db[clave])
            print(hash(request.form['password']))
            if db[clave]["password_cipher"] != hash(request.form['password']):
                error = 'Credenciales incorrectas'
            else:
                params['username'] = request.form['username']
                params['email'] = db[clave]['email']
                params['nombre'] = db[clave]['nombre']
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
        db['users/' + username] = {
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

    db[clave]['email'] = request.form['email']
    db[clave]['nombre'] = request.form['nombre']

    params['queue'] = session['queue']

    params['username'] = username
    params['email'] = db[clave]['email']
    params['nombre'] = db[clave]['nombre']

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