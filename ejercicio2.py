import csv

ventas=[]

with open('archivos/Superstore-Sales.csv') as archivocsv:
    lector = csv.reader(archivocsv, delimiter=",")
    encabezado=next(lector)
    for filacsv in lector:
        ventas.append(filacsv)

# print(ventas)

# sumar todas las cantidades de ventas
total=0
for venta in ventas:
    total=total+int( venta[4])  # 4: order quantity

print(f"el total es {total}")

# sumar la cantidad de ordenes para un filtro determinado
total=0
totalotro=0

for venta in ventas:
    if venta[7]=='Regular Air':  # agrego una condicion (== es igualdad)
        total=total+int( venta[4])  # 4: order quantity
    else:
        totalotro=totalotro+int(venta[4])


print(f"el total para regular air es {total}, y el total para otros es {totalotro}")

# contar (cuantas ventas para regular air)

contador=0
contador_else=0
for venta in ventas:
    if venta[7]=='Regular Air':
        contador=contador+1
    else:
        contador_else=contador_else+1

print(f"La cantidad (conteo) de regular air es {contador}, y los otros casos es {contador_else}")

# obtener el promedio
total=0
totalotro=0
contador=0
contador_else=0

for venta in ventas:
    if venta[7]=='Regular Air':  # agrego una condicion (== es igualdad)
        total=total+int( venta[4])  # 4: order quantity
        contador=contador+1
    else:
        totalotro=totalotro+int(venta[4])
        contador_else=contador_else+1

promedio=total/contador
promedio_else=totalotro/contador_else

print(f"El promedio es {promedio} y para otros es {promedio_else}")