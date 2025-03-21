def aplicar_operacion(operacion, a, b):
    return operacion(a, b)

def sumar(x, y):
    return x + y

resultado = aplicar_operacion(sumar, 3, 5)  
print(resultado)

print('--------------------------------------------')

def operar(f, x, y):
    return f(x, y)

def multiplicar(a, b):
    return a * b

print(operar(multiplicar, 4, 5))