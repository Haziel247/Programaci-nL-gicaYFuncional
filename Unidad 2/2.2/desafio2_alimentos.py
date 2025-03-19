def preparar_alimento_p():
    return '🍕'

def preparar_alimento_h():
    return '🍔'

def preparar_alimento_hotdog():
    return '🌭'

def ordenar_alimento(funcion, num_alimento):
    alimentos = [funcion() for _ in range(num_alimento)]
    alimentos.append(bonus(num_alimento))
    return alimentos

def bonus(num_alimento):
    if num_alimento > 2:
        return 'Coca gratis🥤'
    else:
        return ''

grupoA = ordenar_alimento(preparar_alimento_p, 5)
grupoB = ordenar_alimento(preparar_alimento_h, 3)
grupoC = ordenar_alimento(preparar_alimento_hotdog, 1)

print(grupoA, '\n', grupoB, '\n', grupoC)