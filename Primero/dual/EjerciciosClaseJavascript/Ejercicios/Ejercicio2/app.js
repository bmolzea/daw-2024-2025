const input = document.getElementById("nombre");
const parrafoSaludo = document.querySelector("#saludo");
const parrafoNavegador = document.querySelector("#nombreNavegador");

let nombreNavegador = localStorage.getItem("nombre");

if (nombreNavegador === null) {
    nombreNavegador = "ninguno";
}

parrafoNavegador.textContent = `Nombre por defecto: ${nombreNavegador}`;


function mostrarNombre() {
    let nombre = input.value;
    parrafoSaludo.innerText = "Hola, " + nombre + "!";

    localStorage.setItem("nombre", nombre);
    nombreNavegador = localStorage.getItem("nombre");
    parrafoNavegador.textContent = `Nombre por defecto: ${nombreNavegador}`;
}
