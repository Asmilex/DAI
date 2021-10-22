from flask import Flask, render_template, request, flash, url_for, redirect

from ejercicios.ordenacion import ordenacion_gnomo
from ejercicios.criba import criba
from ejercicios.regex import aplicar_regex

app = Flask(__name__, static_url_path='/static', template_folder='templates')


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
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('Te has loggeado')
            return redirect(url_for('index'))

    return render_template('login.html', error=error)




#
# ──────────────────────────────────────────────────────────────────────── I ──────────
#   :::::: P R I M E R A   P R A C T I C A : :  :   :    :     :        :          :
# ──────────────────────────────────────────────────────────────────────────────────
#
#
# ───────────────────────────────────────────────────────── PRIMER EJERCICIO ─────
#

@app.route('/ordenacion/<string:numeros>')
def show_ordenacion(numeros):
    lista = numeros.split(",")
    for i in range(len(lista)):
        lista[i] = int(lista[i])

    ordenacion_gnomo(lista)
    return ', '.join(str(n) for n in lista)

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