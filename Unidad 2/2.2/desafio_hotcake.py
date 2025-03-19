def preparar_hotcake():
    return '🥞'


def ordenar_hotcake(num_hotcake):
    hotcake = [preparar_hotcake() for _ in range(num_hotcake)]

    return hotcake

hotcake_familia = ordenar_hotcake(int(input('Cuantos son en tu familia: ')))

print(hotcake_familia)
