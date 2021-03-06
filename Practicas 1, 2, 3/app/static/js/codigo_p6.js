function cargar_pokemon() {
  $.ajax({
    url: "/pokemon",
    type: "GET",
    dataType: "json",

    success: function(data) {
      mostrar(data);
    }
  });

  //$.ajax({
  //  url: "/pokemon/1",
  //  type: "GET",
  //  dataType: "json",
  //success: function(data) {
  //    console.log(data);
  //  }
  //});
}

function anadir_pokemon() {
  const id_input = document.getElementById("id_pokemon")
  const nombre_input = document.getElementById("nombre_pokemon")
  const tipo_input = document.getElementById("tipo_pokemon")
  const debilidad_input = document.getElementById("debilidades_pokemon")
  const imagen_input = document.getElementById("imagen_pokemon")

  const pokemon = {
    // Get the value inside the input field
    id        : parseFloat(id_input.value.trim()),
    num       : id_input.value.trim(),
    name      : nombre_input.value.trim(),
    type      : tipo_input.value.trim().split(",")[0] ? tipo_input.value.trim().split(",")          : ["unknown"],
    weaknesses: debilidad_input.value.trim().split(",")[0] ? debilidad_input.value.trim().split(","): ["unknown"],
    img       : imagen_input.value.trim()? imagen_input.value.trim()                                : "https://via.placeholder.com/150"
  }

  $.ajax({
    // Insert the pokemon in the database
    'url': "/pokemon",
    'method': "POST",
    'processData': false,
    'contentType': 'application/json',
    'data': JSON.stringify(pokemon),
    'dataType': "json",

    // When it's completed, call cargar_pokemon
    success: function(data) {
      cargar_pokemon()
      // Clean the input fields
      id_input.value = ""
      nombre_input.value = ""
      tipo_input.value = ""
      debilidad_input.value = ""
      imagen_input.value = ""
    }
  })
}

function editar_pokemon() {
  const id_input = document.getElementById("edit_id_pokemon")
  const nombre_input = document.getElementById("edit_nombre_pokemon")
  const tipo_input = document.getElementById("edit_tipo_pokemon")
  const debilidad_input = document.getElementById("edit_debilidades_pokemon")
  const imagen_input = document.getElementById("edit_imagen_pokemon")

  const id = id_input.value.trim()

  const pokemon = {
    // Get the value inside the input field
    name      : nombre_input.value.trim()? nombre_input.value.trim()                                : undefined,
    type      : tipo_input.value.trim().split(",")[0] ? tipo_input.value.trim().split(",")          : undefined,
    weaknesses: debilidad_input.value.trim().split(",")[0] ? debilidad_input.value.trim().split(","): undefined,
    img       : imagen_input.value.trim()? imagen_input.value.trim()                                : undefined
  }

  $.ajax({
    'url': "/pokemon/" + id,
    'method': "PUT",
    'processData': false,
    'contentType': 'application/json',
    'data': JSON.stringify(pokemon),
    'dataType': "json",

    success: function(data) {
      cargar_pokemon()
      // Clean the input fields
      id_input.value = ""
      nombre_input.value = ""
      tipo_input.value = ""
      debilidad_input.value = ""
      imagen_input.value = ""
    }
  })
}

function delete_pokemon() {
  const id_input = document.getElementById("delete_id_pokemon")
  const id = id_input.value.trim()

  $.ajax({
    'url': "/pokemon/" + id,
    'method': "DELETE",
    'processData': false,

    success: function(data) {
      cargar_pokemon()
      // Clean the input fields
      id_input.value = ""
    }
  })

}

function mostrar(data) {
  $("tbody").empty();
  $.each(data, function(key, value) {
    elemento = JSON.parse(value)

    $("tbody").append(
      `<tr>
      <td>${elemento['num']}</td>
      <td>${elemento['name']}</td>
      <td><img src=${elemento['img']} alt="Imagen de ${elemento['name']}" /></td>
      <td>${elemento['type']}</td>
      <td>${elemento['weaknesses']}</td>
      <td>
        <button
          type="button"
          class="btn btn-info"
          data-toggle="modal"
          data-target="#editPokemonModal"
          data-identificador="${elemento['num']}"
          data-nombre="${elemento['name']}"
          data-tipo="${elemento['type']}"
          data-debilidades="${elemento['weaknesses']}"
          data-imagen="${elemento['img']}"
        >
          Editar
        </button>

        <button
          type="button"
          class="btn btn-danger"
          data-toggle="modal"
          data-target="#deletePokemonModal"
          data-identificador="${elemento['num']}"
        >
          Borrar
        </button>
      </td>
      </tr>`
    )
  });
}

// ????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????

function cambiar_zoom(constante) {
  zoom_actual = parseFloat(getComputedStyle(document.body).getPropertyValue('zoom'))

  zoom_nuevo = zoom_actual + constante
  zoom_nuevo = zoom_nuevo < 0.25? 0.25 : zoom_nuevo
  zoom_nuevo = zoom_nuevo >   50? 50   : zoom_nuevo

  document.body.style.setProperty('zoom', zoom_actual + constante);

  // window.dispatchEvent(new KeyboardEvent('keydown', {
  //   key: "+",
  //   ctrlKey: true
  // }))
}

$(document).ready(function(){
  cargar_pokemon()
})