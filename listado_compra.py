import csv
matriz=[]   # creo un listado
with open('archivos/Libro5.csv') as csv_file:
    lector = csv.reader(csv_file, delimiter=";")
    encabezado=next(lector) # leo en encabezado
    for linea in lector:
        matriz.append(linea)

#  0       |  1     | 2        | 3
#  --------------------------------------
#  nombre | precio | cantidad | subtotal
print(matriz)

# agregar una columna
for linea in matriz:
    subtotal=int(linea[1]) * int(linea[2])
    linea.append(subtotal) # se agrega la columna 3
    print(linea)

# sumar los valores
total=0
for linea in matriz:
    total = total + int(linea[3])

print(f"el total es {total}")

# transformar una columna
for linea in matriz:
    linea[0]=linea[0].upper() # convertir la primera columna en mayuscula

print(matriz)