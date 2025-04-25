from random import randint
from dataclasses import dataclass

@dataclass
class Config:
    idioma: str = "es"
    operaciones: tuple[str] = ("+", "-", "*")
    vidas: int = 3
    minimo: int = 0
    maximo: int = 10

def crear_cuenta(operadores: list[str], min: int, max: int) -> tuple:
    operando1 = randint(min, max)
    operando2 = randint(min, max)
    operador = operadores[randint(0, len(operadores)-1)]
    if operador == "+":
        resultado = operando1 + operando2
    elif operador == "-":
        resultado = operando1 - operando2
    elif operador == "*":
        resultado = operando1 * operando2
    
    return (resultado, f"{operando1} {operador} {operando2} = ? ")

def leer_config() -> Config:
    config = Config()
    with open("config.ini", "r", encoding="utf-8") as f:
        for linea in f:
            dupla = linea.split(":")
            clave = dupla[0]
            valor = dupla[1].strip()

            if clave == "language":
                config.idioma = valor
            elif clave == "operations":
                config.operaciones = tuple(valor.split(","))
            elif clave == "lives":
                config.vidas = int(valor)
            elif clave == "min":
                config.minimo = int(valor)
            elif clave == "max":
                config == int(valor)
            
    return config
            
textos = [
    [
        "Bienvenido al calculatrón",
        "Correcto!",
        "Has fallado!, el resultado correcta era: ",
        "Pierdes una vida, te quedan: "
    ],
    [
        "Welcome to calculatron",
        "Nice!",
        "You have failed!, the correct answer is: ",
        "You loose one life, you have: "
    ]
]

config = leer_config()
vidas = config.vidas

if config.idioma == "es":
    i_lang = 0
elif config.idioma == "en":
    i_lang = 1


print(textos[i_lang][0])
while vidas > 0:
    cuenta = crear_cuenta(config.operaciones, config.minimo, config.maximo)
    resultado_correcto = cuenta[0]
    resultado_usuario = int(input(cuenta[1]))
    
    if resultado_usuario == resultado_correcto:
        print(textos[i_lang][1])
    else:
        print(f"{textos[i_lang][2]} {resultado_correcto}")
        vidas -= 1
        print(f"{textos[i_lang][3]} {vidas}")

