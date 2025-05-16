const selectColor = document.getElementById("colorSelector");
const colorInfo = document.getElementById("colorInfo");
const body = document.body;

function cambiarColor() {
    const colorSeleccionado = selectColor.value;

    body.style.backgroundColor = colorSeleccionado;

    colorInfo.innerText = "Color seleccionado: " + colorSeleccionado;
}