import csv
listado=[]   # creo un listado
with open('archivos/actor.csv') as csv_file:   # leo el archivo actor.csv (y el archivo lo voy a manejar csv_file)
    lector = csv.reader(csv_file, delimiter=",")
    encabezado = next(lector)  # leer el encabezado
    for linea in lector:
        listado.append(linea)
# linea de interrupcion (continua con F9)
print(listado)
