const inputTarea = document.getElementById("nuevaTarea");
const listaTareas = document.getElementById("listaTareas");

function agregarTarea() {
  const texto = inputTarea.value.trim();

  if (texto === "") return;

  // Crear elementos
  const li = document.createElement("li");
  li.classList.add("tarea");

  const span = document.createElement("span");
  span.innerText = texto;

  const btnEliminar = document.createElement("button");
  btnEliminar.innerText = "Eliminar";
  btnEliminar.classList.add("eliminar");
  btnEliminar.onclick = () => li.remove();

  // Agregar elementos al li y luego al ul
  li.appendChild(span);
  li.appendChild(btnEliminar);
  listaTareas.appendChild(li);

  // Limpiar el input
  inputTarea.value = "";
}
