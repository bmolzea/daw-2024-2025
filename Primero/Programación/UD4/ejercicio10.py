jugadores_barcelona = [
    "Marc-André ter Stegen", "Iñaki Peña", "Wojciech Szczęsny", "Ander Astralaga", "Diego Kochen",
    "Jules Koundé", "Alejandro Balde", "Iñigo Martínez", "Vitor Roque", "Sergi Roberto", "Jordi Alba",
    "Marcos Alonso", "Eric García", "Clément Lenglet", "Samuel Umtiti",
    "Sergio Busquets", "Frenkie de Jong", "Pedri", "Gavi", "Ilkay Gündogan", "Franck Kessié", "Miralem Pjanic", "Oriol Romeu",
    "Raphinha", "Ferran Torres", "Ansu Fati", "Lamine Yamal", "Robert Lewandowski", "Vitor Roque  Jr"
]

for jugador in jugadores_barcelona:
    n_letras = len(jugador)
    if jugador[0].lower() == jugador[n_letras-1]:
        print(jugador)