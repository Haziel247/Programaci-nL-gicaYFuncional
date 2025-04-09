from functools import reduce
import customtkinter as ctk

#Lista de materias y aspectos al igual que para las calificaciones siendo globales para su llamado en otra funciones
materias = ["Matemáticas", "Física", "Programación"]
aspectos = ["Actividades", "Contenido", "Herramientas"]
calificaciones = {}
alumnos = []

#Se pide el numero de alumnos
def pedir_numero_alumnos():
    def aceptar_numero():
        numero_alumnos = int(entry_alumnos.get())
        ventana_numero_alumnos.destroy()
        ingresar_calificaciones(numero_alumnos)

    ventana_numero_alumnos = ctk.CTk()
    ctk.CTkLabel(ventana_numero_alumnos, text="¿Cuántos alumnos van a registrar calificaciones?").grid(row=0, column=0, pady=10)
    entry_alumnos = ctk.CTkEntry(ventana_numero_alumnos)
    entry_alumnos.grid(row=1, column=0, pady=10)
    button_aceptar = ctk.CTkButton(ventana_numero_alumnos, text="Aceptar", command=aceptar_numero)
    button_aceptar.grid(row=2, column=0, pady=10)

    ventana_numero_alumnos.mainloop()

#Se realiza la captura de las calificaciones, alumno por alumno
def ingresar_calificaciones(numero_alumnos):
    global alumnos
    #Funcion reduce para determinar que alumno es segun indice
    alumnos = reduce(lambda acc, i: acc + [f"Alumno {i+1}"], range(numero_alumnos), [])

    #Funcion para capturar las califiaciones de cada aspecto
    #Se implementa la interfaz a la vez que se hace la captura, una interfaz dinamica
    def capturar_calificaciones(alumno_index):
        if alumno_index < numero_alumnos:
            alumno = alumnos[alumno_index]
            ventana_calificaciones = ctk.CTk()

            ctk.CTkLabel(ventana_calificaciones, text=f"Calificaciones de {alumno}", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=len(aspectos)+1, pady=10)

            entradas_calificaciones = {}

            #Función recursiva para la creacion de los campos de calificaciones        
            def crear_entradas(materia_index, aspecto_index, fila):
                if materia_index < len(materias):
                    ctk.CTkLabel(ventana_calificaciones, text=materias[materia_index]).grid(row=fila, column=0)
                    if aspecto_index < len(aspectos):
                        ctk.CTkLabel(ventana_calificaciones, text=aspectos[aspecto_index]).grid(row=1, column=aspecto_index + 1)
                        materia = materias[materia_index]
                        aspecto = aspectos[aspecto_index]
                        key = (alumno, materia, aspecto)
                        entradas_calificaciones[key] = ctk.CTkEntry(ventana_calificaciones)
                        entradas_calificaciones[key].grid(row=fila, column=aspecto_index + 1, padx=5)
                        crear_entradas(materia_index, aspecto_index + 1, fila)
                    else:
                        crear_entradas(materia_index + 1, 0, fila + 1)

            crear_entradas(0, 0, 2)

            #En está función se emplea funcion recursiva para guardar los datos en una lista calificaciones
            def guardar_calificaciones():
                def guardar(materia_index, aspecto_index):
                    if materia_index < len(materias):
                        if aspecto_index < len(aspectos):
                            key = (alumno, materias[materia_index], aspectos[aspecto_index])
                            calificaciones[key] = entradas_calificaciones[key].get()
                            guardar(materia_index, aspecto_index + 1)
                        else:
                            guardar(materia_index + 1, 0)
                guardar(0, 0)
                ventana_calificaciones.destroy()
                #Vuelve a llamar a la funcion principal para la captura del siguiente alumno
                capturar_calificaciones(alumno_index + 1)

            ctk.CTkButton(ventana_calificaciones, text="Guardar Calificaciones", command=guardar_calificaciones).grid(row=3 + len(materias), column=0, columnspan=4, pady=10)
            ventana_calificaciones.mainloop()
        else: 
            #Cuando todos los alumnos capturaron se muestran los resultados
            mostrar_resultados()

    capturar_calificaciones(0)

def metricas(alumno):
    total_calificaciones = 0
    num_calificaciones = 0

    #Función recursiva para calcular 
    def calcular_fila(materia_index, aspecto_index):
        nonlocal total_calificaciones, num_calificaciones
        if materia_index < len(materias):
            if aspecto_index < len(aspectos):
                key = (alumno, materias[materia_index], aspectos[aspecto_index])
                if key in calificaciones:
                    try:
                        total_calificaciones += float(calificaciones[key])
                        num_calificaciones += 1
                    except ValueError:
                        pass
                calcular_fila(materia_index, aspecto_index + 1)
            else:
                calcular_fila(materia_index + 1, 0)
        # <-- Aquí se agrega un "else" vacío para terminar la recursión
        else:
            return

    calcular_fila(0, 0)

    #Se retornan el promedio, total y el mejor y,  peor alumno en promedio
    promedio = total_calificaciones / num_calificaciones if num_calificaciones > 0 else 0
    return promedio, total_calificaciones

def mejor_peor():
    #El mejor y peor alumno usando map
    lista = list(map(lambda a: (a, *metricas(a)), alumnos))
    mejor = max(lista, key=lambda x: x[1], default=None)
    peor = min(lista, key=lambda x: x[1], default=None)
    return mejor, peor

def mostrar_resultados():
    ventana_resultados = ctk.CTk()

    seleccion = ctk.StringVar(value="Alumno 1")
    menu_alumnos = ctk.CTkOptionMenu(ventana_resultados, variable=seleccion, values=alumnos)
    menu_alumnos.grid(row=0, column=0, pady=10)

    def mostrar_calificaciones():
        alumno_seleccionado = seleccion.get()

        def mostrar_fila(materia_index, fila):
            if materia_index < len(materias):
                materia = materias[materia_index]
                ctk.CTkLabel(ventana_resultados, text=materias[materia_index]).grid(row=fila, column=0)
                def mostrar_aspecto(index):
                    if index < len(aspectos):
                        ctk.CTkLabel(ventana_resultados, text=aspectos[index]).grid(row=2, column=index + 1,padx=5)
                        key = (alumno_seleccionado, materia, aspectos[index])
                        valor = calificaciones.get(key, "N/A")
                        ctk.CTkLabel(ventana_resultados, text=valor).grid(row=fila, column=index + 1)
                        mostrar_aspecto(index + 1)
                mostrar_aspecto(0)
                mostrar_fila(materia_index + 1, fila + 1)

        mostrar_fila(0, 5)

        promedio, total = metricas(alumno_seleccionado)
        mejor, peor = mejor_peor()
        
        ctk.CTkLabel(ventana_resultados, text=f"Promedio de {alumno_seleccionado}: {promedio:.2f}", font=("Arial", 14, "bold")).grid(row=11, column=0, columnspan=4, pady=5)
        ctk.CTkLabel(ventana_resultados, text=f"Total de calificaciones de {alumno_seleccionado}: {total:.2f}", font=("Arial", 14, "bold")).grid(row=12, column=0, columnspan=4, pady=5)
        if mejor:
            ctk.CTkLabel(ventana_resultados, text=f"Mejor {mejor[0]}: con promedio de {mejor[1]:.2f}", text_color="green").grid(row=13, column=0, columnspan=4, pady=5)
        if peor:
            ctk.CTkLabel(ventana_resultados, text=f"Peor {peor[0]}: con promedio de {peor[1]:.2f}", text_color="red").grid(row=14, column=0, columnspan=4, pady=5)

    ctk.CTkButton(ventana_resultados, text="Mostrar Calificaciones y Promedio", command=mostrar_calificaciones).grid(row=1, column=0, pady=10)

    ventana_resultados.mainloop()

pedir_numero_alumnos()
