#mapear datos
#Lista de jugadores
jugadores = [
    {"nombre":"brandon","edad":22},
    {"nombre":"Angel","edad":22},
    {"nombre":"Armando","edad":21},
    {"nombre":"Alex","edad":21} 
]

#usar map para extraer los nombres de los jugadores
nombre_jugadores = list(map(lambda jugador: jugador["nombre"], jugadores))
print(nombre_jugadores)
