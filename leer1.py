import csv
listado=[]   # creo un listado
with open('archivos/actor.csv') as csv_file:   # leo el archivo actor.csv (y el archivo lo voy a manejar csv_file)
    lector = csv.reader(csv_file, delimiter=",")
    encabezado = next(lector)  # leer el encabezado
    for linea in lector:
        dic={
            "actor_id":float(linea[0]),
            "first_name":linea[1],
            "last_name": linea[2],
            "last_update": linea[3]
        }
        listado.append(dic)

print(listado)
