asignatura_VIII = ["Progrmacion lógica"]

def n_asignatura(lista):
    asign_nueva = input("Escribe una asignatura o exit para salir: ")
    if asign_nueva == "exit":
        return lista
    return n_asignatura(lista + [asign_nueva])

nueva_lista = n_asignatura(asignatura_VIII)
print (asignatura_VIII)
print(nueva_lista)