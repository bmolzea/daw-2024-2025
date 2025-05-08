const input = document.getElementById("nombre");
const parrafoSaludo = document.querySelector("#saludo");

function mostrarNombre() {
    let nombre = input.value
    parrafoSaludo.innerText = "Hola, " + nombre + "!";
  }
  