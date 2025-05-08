const inputTarea = document.getElementById("nuevaTarea");
const listaTareas = document.getElementById("listaTareas");

function agregarTarea(){
    const texto = inputTarea.value.trim();

    if (texto === ""){
        return;
    }

    const li = document.createElement("li");
    li.classList.add("tarea");

    const span = document.createElement("span");
    span.textContent = texto;

    const btnEliminar = document.createElement("button");
    btnEliminar.textContent = "Eliminar";
    btnEliminar.classList.add("eliminar");
    btnEliminar.onclick = () => {
        li.remove();
    }

    li.appendChild(span);
    li.appendChild(btnEliminar);
    listaTareas.appendChild(li);

    inputTarea.value = "";
}