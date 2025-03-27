#Ejemplo 1
variable_global = 10

def aumentar_variable ():
    return variable_global + 1

print(aumentar_variable())

#Ejemplo 2
def contar_palabras(texto):
    return len(texto.split())

oracion = "El tema de hoy es la inmutabilidad en Python"
print(contar_palabras(oracion))

#Ejamplo 3
contador_global = 0

def contar_palabras_no_funcional(texto):
    global contador_global
    contador_global = len(texto.split())

texto_ejemplo = "Este es un ejemplo"
contar_palabras_no_funcional(texto_ejemplo)
print(contador_global)

contar_palabras_no_funcional("Otro texto de ejemplo")
print(contador_global)