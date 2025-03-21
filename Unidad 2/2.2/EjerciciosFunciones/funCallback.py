def preparar_cafes(cafe, num_tazas):
    return cafe(num_tazas)
    
def americano(num_tazas):
    mensaje = str(num_tazas) + ' Café americano'
    return mensaje

def olla(num_tazas):
    mensaje = str(num_tazas) + ' Café de olla'
    return mensaje
    
print(preparar_cafes(americano, 3))

print('--------------------------------------------')

def ejecutar_proceso(callback):
    print("Procesando datos...")
    callback()

def mostrar_resultados():
    print("Datos procesados correctamente")

ejecutar_proceso(mostrar_resultados)