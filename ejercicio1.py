import csv

clientes=[]  # matriz

with open('archivos/clientes.csv') as csv_file:
    lector = csv.reader(csv_file, delimiter=";")
    encabezado=next(lector)
    for cliente in lector:
        clientes.append(cliente)

print(clientes)

# sumar los valores
total=0
for cliente in clientes:
    total=total+int(cliente[1])

print(f"El total es :{total}")