#reduce
from functools import reduce

#Lista de jugadores
jugadores = [
    {"nombre":"brandon","edad":23},
    {"nombre":"Angel","edad":22},
    {"nombre":"Armando","edad":21},
    {"nombre":"Alex","edad":21} 
]

#usar reduce para obtener la suma de las edades de los jugadores
suma_edades = reduce(lambda acumulador, jugador: acumulador + jugador ["edad"], jugadores, 0)
print(suma_edades)