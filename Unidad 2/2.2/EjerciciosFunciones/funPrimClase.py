def saludar():
    return 'Hola mundo'

mensaje = saludar

def login():
    return 'Se ha verificado correctamente'

status = login()

print('Estatus de verificación: ', status)
print('-------------------------------------------------')
print(mensaje())