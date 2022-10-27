# Crea un Script llamado recorrido.py que realice las siguientes funciones:
#Recorre el listado del ejemplo y realiza las siguientes operaciones: [18, 50, 210, 80, 145, 333, 70, 30]
#Imprimr el número en caso de que sea múltiplo de 10 y menor que 200

def recorrido(lista):
    lista = []
    for i in lista:
        if i % 10 == 0 and i <200:
            lista.append(i)
    print(lista)
        

lista = [18, 50, 210, 80, 145, 333, 70, 30]
recorrido(lista)



