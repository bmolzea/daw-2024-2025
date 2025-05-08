const input = document.getElementById("nombre");
const parrafoSaludo = document.querySelector("#saludo");

function mostrarNombre(){
  const nombre = input.value.trim();
  if (nombre) {
    parrafoSaludo.innerText = nombre ;
  } else {
    parrafoSaludo.innerText = "";
  }
}


input.addEventListener("input", mostrarNombre);
