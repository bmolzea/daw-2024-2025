function tick(){
    reloj.innerText = new Date().toLocaleTimeString()
}

let reloj = document.getElementById("relojCliente")
let intervalId = window.setInterval(tick, 500)

