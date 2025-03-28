def cuadradoLista(arreglo):

    arreglo = list(filter(lambda x: x > 0 and isinstance(x, int), arreglo))
    print(arreglo)
    arreglo =  list(map(lambda x: x ** 2, arreglo))

    return arreglo

cuadradoEnteros = cuadradoLista([-3, 4.8, 5, 3, -3.2])
print(cuadradoEnteros)