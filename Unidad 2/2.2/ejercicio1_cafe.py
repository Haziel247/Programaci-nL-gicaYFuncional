def preparar_cafe():
    return 'cafe'

def ordenar_cafe(num_tazas):
    tazas_cafe = [preparar_cafe() for _ in range(num_tazas)]

    return tazas_cafe

cafe_para_grupoB = ordenar_cafe(10)

print(cafe_para_grupoB)