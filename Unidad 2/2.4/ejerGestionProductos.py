from functools import reduce

textos = [
    "Frijoles Refritos", 
    "Coca Cola", 
    "Zumo de Naranja", 
    "Café de Olla", 
    "Gorditas de Chicharrón", 
    "Huevos Motuleños"
    ]

#Ordenar alfabética
print("Ordenar alfabética:")
print(textos)
new_strings = textos.sort()
print(textos)
print()

#Nombres ordenados
nombresOrdenados = ','.join(new_strings)
print("Nombres ordenados: ", nombresOrdenados)

#Convertir cada nombre en un slug
slugs = list(map(lambda string: string.lower().replace(' ', '-'), new_strings))
print("Lista de los slugs: ", slugs)

