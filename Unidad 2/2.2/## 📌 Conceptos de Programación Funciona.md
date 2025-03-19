## 📌 Conceptos de Programación Funcional en Python  

### **1️⃣ Devoluciones de llamada (Callbacks)**  
- Son funciones que se **pasan como argumento** a otra función para ser ejecutadas más tarde.  
- Se utilizan comúnmente en programación funcional y en eventos asíncronos.  

🔹 Ejemplo en Python:  
```python
def operar(n1, n2, funcion):
    return funcion(n1, n2)

def suma(a, b): # Función de primer orden
    return a + b

def resta(a, b):
    return a - b

resultado = operar(5, 3, suma)  # Pasamos la función suma como argumento
print(resultado)

'''
Un callback es una función que se pasa a otra función como argumento y se espera que sea llamada dentro de esa función

'''

```
### **2️⃣ Funciones de primera clase** 

En **Python**, las funciones son objetos de **primera clase**, lo que significa que se pueden:  
✅ Asignase a variables 
✅ Pasarse como argumentos a otras funciones  
✅ Devolver desde una función  

🔹 Ejemplo en Python:
```python
def saludo():
    return "¡Hola!"

mi_variable = saludo  # Asignamos la función a una variable
print(mi_variable())  # Llamamos a la función a través de la variable
```

### **3️⃣ Funciones de orden superior**

Las **funciones de orden superior** en **Python** son aquellas que:  
✅ Reciben una función como argumento o  
✅ Devuelven una función como resultado  

🔹 Ejemplo en Python: 
```python
def elegir_operacion(operacion): # Función de orden superior
    def multiplicar(x):
        return x * 2
    def dividir(x):
        return x / 2
    
    if operacion == "multiplicar":
        return multiplicar  # Retornamos la función sin ejecutarla
    else:
        return dividir

doble = elegir_operacion("multiplicar")  # Devuelve la función multiplicar
print(doble(10))
divide2 = elegir_operacion("dividir")  # Devuelve la función dividir
print(divide2(10))
```

#🔸 elegir_operacion es una función de orden superior porque devuelve una función en lugar de un valor normal.


### **4️⃣ Funciones lambda** 

Las **funciones lambda** en **Python** son funciones **anónimas y pequeñas** que:  
✅ Pueden pasarse como argumentos sin necesidad de definirlas antes 
✅ Se utilizan cuando la función es simple y solo se necesita en un lugar 

🔹 Ejemplo en Python: 
```python
doble = lambda x: x * 2
print(doble(5))  # Salida: 10


numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros)) 
print(dobles)  # Salida: [2, 4, 6, 8]
```

**map**( ) es una función de orden superior que aplica una función a cada elemento de una lista.
**list**( ) convierte el resultado en una lista.
**lambda** x: x * 2 es la función que se aplica a cada elemento de la lista.