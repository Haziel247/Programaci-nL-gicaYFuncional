#diltrar datos
#Lista de jugadores
jugadores = [
    {"nombre":"brandon","edad":23},
    {"nombre":"Angel","edad":22},
    {"nombre":"Armando","edad":21},
    {"nombre":"Alex","edad":21} 
]

#usar map para extraer los nombres de los jugadores
edad_jugadores = list(filter(lambda jugador: jugador["edad"] > 21, jugadores)) #propiedad edad
print(edad_jugadores)
