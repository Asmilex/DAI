from flask import Flask, render_template, request, flash, url_for, redirect, session

from ejercicios.ordenacion import ordenacion_gnomo
from ejercicios.criba import criba
from ejercicios.regex import aplicar_regex

app = Flask(__name__, static_url_path='/static', template_folder='templates')
app.secret_key = b'wiutqwoirjksdfjsl'



#
# ──────────────────────────────────────────────────────────────────────── II ──────────
#   :::::: S E G U N D A   P R A C T I C A : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────────
#

# Requerimientos:
#     - Barra de navegación: debe contener...
#         - Logo del sitio
#         - Nombre del sitio
#         - Enlaces a otras páginas
#         - Mini formulario con login
#     - Menú vertical
#     - Espacio para mostrar contenidos
#     - Pie de página

@app.route('/')
@app.route('/index')
def index():
    params = {}

    queue_reciente('index.html')
    params['queue'] = session['queue']
    params['username'] = session['username']

    return render_template('index.html', **params)

@app.route('/login', methods=['GET', 'POST'])
def login():
    params = {}
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'secret':
            error = 'F en el chat colega no te has loggeado correctamente'
        else:
            flash('Te has loggeado')
            params['username'] = request.form['username']
            session['username'] = params['username']

    queue_reciente('login')
    params['queue'] = session['queue']
    params['error'] = error

    return render_template('login.html', **params)

@app.route('/logout', methods=['GET'])
def logout():
    session['username'] = ''
    session['queue'] = []

    queue_reciente('logout')
    params = {}
    params['queue'] = session['queue']
    params['username'] = session['username']

    return render_template('index.html', **params)

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

    queue_reciente('ordenacion')
    params['queue'] = session['queue']
    params['username'] = session['username']
    return render_template("ordenacion.html", **params)


# ────────────────────────────────────────────────────────────────────────────────

@app.route('/criba/<int:n>')
def show_criba(n):
    queue_reciente('criba')
    return ', '.join(str(a) for a in criba(n))

# ────────────────────────────────────────────────────────────────────────────────

@app.route('/regex/<string:cadena>')
def show_regex(cadena):
    print(cadena)
    queue_reciente('regex')
    return aplicar_regex(cadena)


#
# ───────────────────────────────────────────────────────── TERCER EJERCICIO ─────
#

@app.errorhandler(404)
def page_not_found(e):
    queue_reciente('404 :(')
    return render_template('404.html'), 404

#
# ────────────────────────────────────────────────────────── EJERCICIO EXTRA ─────
#

@app.route('/svg_extra')
def show_svg_extra():
    queue_reciente('svg extra')
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