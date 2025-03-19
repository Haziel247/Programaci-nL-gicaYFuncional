def preparar_cafe(cafe):
    def americano():
        return 'Café americano'
    def olla():
        return 'Café olla'
    
    if cafe == 'americano':
        return americano()
    else:
        return olla()
    
def ordenar_cafe(funcion, num_tazas):
    tazas_cafe = [preparar_cafe(funcion) for _ in range(num_tazas)]

    return tazas_cafe

cafe_grupoA = ordenar_cafe('americano', int(input('Cuántos cafes: ')))

cafe_grupoB = ordenar_cafe('olla', int(input('Cuántos cafes: ')))

print('Cafes para el grupo A: ', cafe_grupoA)

print('Cafes para el grupo A: ', cafe_grupoB)