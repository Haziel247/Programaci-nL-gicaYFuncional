from functools import reduce


#Lista Ventas
ventasD1 = [1500, 2500, 3200, 4500, 6000, 1200, 8000]

#Función reduce() imprimiendo el promedio de las ventas
promPorDia = round((reduce(lambda promedio, venta: promedio + venta, ventasD1, 0))/len(ventasD1), 2)
print("Promedio de las ventas por día: ", (promPorDia), " MXN")

print()
#Función map() imprimiendo el cambio de moneda
cambioDolar = list(map(lambda venta: round(venta/20.46, 2), ventasD1))
print("Cambio de moneda de las ventas: ", cambioDolar)

print()
#Función filter() imprimiendo las ventas mayores a 150 dolares
ventMayor = list(filter(lambda venta: venta > 150, cambioDolar))
print("Ventas mayoes a 150 dolares: ", ventMayor)

print()
#Función map() del resultado de filter() imprimiendo el promedio de las ventas mayores a 150 dolares
promVentMayor = round((reduce(lambda promedio, venta: promedio + venta, ventMayor, 0))/len(ventasD1), 2)
print("Promedio de las ventas que solo son mayores a 150 dolares: ", promVentMayor)