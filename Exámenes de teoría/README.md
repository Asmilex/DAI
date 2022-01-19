# Preguntas de teoría

## Febrero de 2016

### 1. ¿Para qué sirve jQuery? ¿Cómo es la sintáxis de una función de jQuery? Pon un ejmplo de función que afecte a todos los elemntos de un HTML con atributo `class="a"` y otro ejemplo que afecte al elemento `<div id="2"></div>`

jQuery es una librería ligera de Javascript para seleccionar y manipular elementos HTML y CSS, modificar el DOM, crear animaciones, y usar AJAX de forma sencilla.

La sintaxis de una función de jQuery es la siguiente:

```
$(selector).function(argumentos);
```

Dependiendo de lo que pongamos en `selector`, tomaremos diferentes elementos de un documento. Por ejemplo, si escribimos lo siguiente, estaremos seleccionando todos los atributos con class `a`:

```javascript
$(".a");
```

Y si lo que buscamos es que se seleccionen aquellos elementos div que tengan el atributo `id` con valor `2`, podemos escribir lo siguiente:

```javascript
$("div[2]");
```


### 2. ¿Cuál es la diferencia en el envío de una llamada de parámetros GET y otra POST de HTTP?

La llamada GET se utiliza para pedir datos de un recurso específico.

Por ejemplo, si queremos obtener una lista de usuarios de una API, podemos hacer una llamada GET a la URL `http://api.com/users` y obtener una lista de usuarios. Si quisiéramos especificar algunos parámetros en particular, podríamos hacer una llamada GET a la URL `http://api.com/users?name=juan&lastname=perez`, donde `name` y `lastname` son los parámetros que queremos enviar.

Los métodos POST se usan para crear recursos en la URL especificada. Los datos enviados al servidor se almacenan en el cuerpo de la petición HTTP.

En el ejemplo de antes, si quisiéramos crear un usuario, podríamos hacer una llamada POST a la URL `http://api.com/users` y enviar los datos del usuario en el cuerpo de la petición.

Échale un vistazo a la pregunta del [siguiente examen](#3-y-una-llamada-post-con-los-mismos-parámetros) para comprobar cómo se haría.


### 3. ¿Cómo se llama en Django el archivo donde están teste tipo de instrucciones? ¿Para qué sirven? Explicar con detalle qué signiifca cada parte de cada argumento de la llamada.

> `url(r'^bar/(?P<nombre_slug>[\w\-]+)/$', views.bar, name='bar')`

Este archivo se encuentra en `urls.py`. Sirve para especificar cuáles son los puntos de entrada del frontend, y cuáles son las vistas que se van a ejecutar. Se encuentran especificadas en el array `urlpatterns`.

Esta, en específico, es una expresión regular que captura todas aquellas que empiezan con `/bar/`, y terminan con /. Además, tienen en mitad de la URL que captura un ? seguido de P. Esto nos indica que se capturará una variable llamada, `nombre_slug`. Esta es una una serie de caracteres en `[a-zA-Z0-9_]` seguido de un `-`. Por ejemplo, `url/bar/18a234-298zAg`.

Para finalizar, se ejecuta la vista `bar` que se encuentra en `views.py`, y se le pasa como argumento el nombre de la variable `nombre_slug`.


### 4. ¿Cuáles son las funciones de una librería como Boostrap?

Este tipo de frameworks simplifica el diseño del CSS del frontend. Incluyen una colección de utilidades y variables que permiten colocar elementos complejos, situar elementos en la página para que queden legibles en todos los navegadores, y que cambie adecuadamente con el tamaño del dispositivo. En esencia, diseño *responsive*.

Una de las utilidades que incluyen suelen ser un sistema de *grids*, que facilita la colocación de elementos en la página.

Hay muchas famosas. Por ejemplo, la ya mencionada Bootstrap, Materialize, Tailwind...


### 5. ¿Qué es un ORM? En Django, ¿cómo se llama el archivo relacionado con el ORM?

Los *Object Relational Mapping* (ORM) simplifican el diseño de la base de datos. Su principal misión es transmitir información entre la base de datos y el modelo de la aplicación. Abstraen las consultas SQL (o noSQL, si lo permite la librería) haciéndolas más sencillas para los programadores.

Por ejemplo, en vez de escribir `SELECT * FROM users WHERE id = 1`, podemos escribir `User.objects.get(id=1)`.

Algunas de las funciones que suelen implementar son filtros, queries para seleccionar todos los elementos de una base de datos, para eliminar.

En Django, se definen los modelos en el archivo `models.py`. Un ejemplo sería:

```python
from django.db import models

class Musico(models.Model):
    nombre         = models.CharField(max_length=50)
    genero_musical = models.CharField(max_length=50)
    instrument     = models.CharField(max_length=100)

class Album(models.Model):
    musico            = models.ForeignKey(Musico, on_delete=models.CASCADE)
    titulo            = models.CharField(max_length=100)
    fecha_lanzamiento = models.DateField()
    likes             = models.IntegerField()
```

Y una consulta sería `Musico.objects.filter(name="Juan")`.


### 6. ¿Qué tiene de especial una llamada AJAX?

La principal característica de AJAX es que sus llamadas son asíncronas. Esto significa que no se bloquea la página, y se puede continuar con otras tareas. Cuando AJAX haya terminado su procedimiento, el contenido se actualizará.

Es importante diseñar las funciones para respetar la asincronía. Esto significa que, si estamos esperando a algún recurso, debemos esperar a que se complete la petición para poder usarlo.


### 7. ¿Qué harías para darle a tu aplicación la capacidad de cambiar de lengua?

Para conseguir que la aplicación cambie de lengua, deberíamos utilizar algún programa de localización (l10n) o internalización (i18n). Esto nos permite cambiar el idioma de la aplicación dependiendo de las necesidades de cada usuario.

Por ejemplo, gettext en Python. Se escribe la aplicación en un idioma (generalmente inglés), se extraen las plantillas de traducción (archivos `.po`), se rellenan, y se complilan a un archivo `.mo`.


### 8. Comenta los cambios que has hecho para el despliegue de la aplicación de Django

(No hemos hecho esto. Aún así, si quieres responder a esta pregunta, mira la [checklist de Django](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/)).


### 9. ¿Qué diferencias has encontrado entre los frameworks "Flask" y "Django"?

Ambos son frameworks de Python. La principal diferencia es que Flask es un microframework. Es más sencillo empezar a programar. Las URLs se definen con decoradores. A partir de ahí, no tiene demasiadas restricciones. Todo se encapsula en un objeto, que suele denominarse `app`.

Django, sin embargo, es una bestia diferente. Su estructura es mucho más rígida. Implementa middlewares, ORMs, urls, seguridad, autenticación, diferentes bases de datos... De entrada, te pide que aprendas su estructura. Sin embargo, una vez lo haces, facilita enormemente el desarrollo del stack.

Para un proyecto a gran escala, Django es una opción mejor. Si lo que buscas es algo casero, Flask parece más intuitivo a priori.

(Si quieres expandir la respuesta, [mira este blog](https://www.codecademy.com/resources/blog/flask-vs-django/))


### 10. A grandes rasgos: ¿cómo crees que funciona intermanente la autenticación de Django?

(No tengo nada claro ésta. Supongo que habrá una especie de demonio por encima que vigile que tengas permisos para acceder a un recurso. O quizás un servicio middleware que intercepte la petición, comprobando que se cumple lo requerido. Necesitarás un token para afirmar que eres quien dices ser, y dependiendo del nivel de acceso que tengas, te permitirá acceder a unas cosas u otras. Cómo lo haga internamente sepa dios).


## ¿Enero 2018?

### 1. ¿Para qué sirve jQuery? ¿Cómo es la sintaxis de una función? Ejemplo que afecte a todos los párrafos de un documento con class = "a" y otro a una imagen con id = "mi_imagen"

[Ver este examen](#1-para-qué-sirve-jquery-cómo-es-la-sintáxis-de-una-función-de-jquery-pon-un-ejmplo-de-función-que-afecte-a-todos-los-elemntos-de-un-html-con-atributo-classa-y-otro-ejemplo-que-afecte-al-elemento-div-id2div)

La imagen se puede obtener con `$("img[mi_imagen]"`.

### 2. ¿Cómo sería la URL de una petición GET al servidor 'pepito.com' por el puerto 80, con la ruta 'restaurantes/lista' y con los parámetros `orden = descendiente` y `todos = si`?

`pepito.com/restaurantes/lista?orden=descendiente&todos=si`.

### 3. ¿Y una llamada POST con los mismos parámetros?

```
POST /restaurantes/lista HTTP/1.1
Host: pepito.com
Content-Type: application/json

{
    "orden": "descendiente",
    "todos": "si"
}
```

### 4. ¿Cuál es la utilidad habitual de los verbos HTTP en una API REST?

GET: conseguir un recurso. Idempotente y seguro.
PUT: actualizar un recurso. Es idempotente, pero cambia el estado del URI.
POST: crear un recurso. No es idempotente ni seguro.
DELETE: eliminar un recurso. Es idempotente, pero no seguro.


### 5. Explica cómo actualizar con AJAX una página web (por ejemplo, al pulsar el botón de mostrar más info de la página).

La estructura general suele ser la siguiente:

1. Crea el elemento de la vista correspondiente. En este caso, el botón
2. Haz que el elemento llame a Javascript cuando se ejecute. Para un botón, podemos usar `onclick=funcion()`. Otra opción es tener disparados que vigilen el estado del elemento.
3. Deja que AJAX haga su magia. Si puedes usar algo como jQuery para simplificar las llamadas, mejor.
4. Cuando el recurso esté listo, actualiza la parte relevante de la vista.

```html
<button onclick="mostrar_mas_info()">Mostrar más info</button>"
<p id="mas-info" hidden>Mucho texto</p>
```

```javascript
function mostrar_mas_info() {
    $.ajax({
        url: ...,
        success: function(data) {
            $("#mas-info").show();
        }
    })
}
```

### 6. Explica las diferencias entre una base de datos SQL y una base de datos NoSQL.

Una base de datos SQL permite manipular datos en una base relacional. Esto se realiza mediante un lenguaje de consultas. En este caso, SQL.

A diferencia de éstas, NoSQL no utiliza base de datos relacionales, sino alguna basada en grafos, documentos, pares clave-valor o similares. Estas surgiendo a raíz de la necesidad de tener datos no estructurados, en parte debido a la gran cantidad de datos diversos que se manejan en el campo del big data. Uno de estos sistemas de bases de datos no relacionales es MongoDB.

Tienen la ventaja de que escalan fácilmente, permiten modelos de datos más flexibles y esquemas dinámicos para datos no estructurados. A diferencia de los de SQL, escalan horizontalmente.


### 7. ¿Cómo funcionan y para qué sirven las sesiones?

Puesto que HTTP es stateless, no es posible saber qué es lo que un usuario hizo en la aplicación con anterioridad. Las sesiones permiten a los servidores mantener información sobre los usuarios que acceden a una aplicación. Asociando cookies con un token a un registro en el servidor, se mantiene información de la conexión. Así, se conoce quién es el usuario que está accediendo en cada momento.

[Imagen ilustrativa de cómo funciona](http://machinesaredigging.com/blog-mad/wp-content/uploads/2013/10/how_does_a_session_work.jpg)


### 8. ¿Qué es el MVC? ¿Cómo está reflejado en Django?

MVC es un patrón de diseño que separa la vista, el modelo y el controlador.

- La vista es la parte que se le muestra a los usuarios. Acepta y muestra datos.
- El modelo es el funcionamiento interno de la aplicación. Ocupa la parte central del procesamiento. Almacena también los datos.
- El controlador prepara la información para comunicarla entre ambas partes.

Django no adopta fielmente el patrón MVC. Implementa un patrón diferente llamado [MTV (Model, Template and View)](https://data-flair.training/blogs/django-mtv-architecture/).
