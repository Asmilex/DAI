function cargar_pokemon() {
  $.ajax({
    url: "http://192.168.1.45:5000/pokemon",
    type: "GET",
    dataType: "json",

    success: function(data) {
      //console.log(data);
      mostrar(data);
    }
  });
}

function mostrar(data) {
  $.each(data, function(key, value) {
    elemento = JSON.parse(value)
    $("tbody").append(`<tr>
    <td>${elemento['num']}</td>
    <td>${elemento['name']}</td>
    <td><img src=${elemento['img']} alt="Imagen de ${elemento['name']}" /></td>
    <td>${elemento['type']}</td>
    <td>${elemento['weaknesses']}</td>
    </tr>`
      )
  });
}


$(document).ready(function(){
  cargar_pokemon()
})