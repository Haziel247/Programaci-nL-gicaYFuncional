multiplicar = lambda x, y: x * y
print(multiplicar(3, 4))

print('--------------------------------------------')

alumnos = [("Carlos", 85), ("Ana", 92), ("Luis", 78)]

alumnos_ordenados = sorted(alumnos, key=lambda x: x[1], reverse=True)

print(alumnos_ordenados)