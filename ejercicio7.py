def recorrido(lista):
    lista = []
    for i in lista:
        if i == i % 10 and i <200:
            i.append(lista)
        else:
            for i in lista:
             if i > 300:
              break
            else:
                return lista 

lista = [18, 50, 210, 80, 145, 333, 70, 30]
recorrido(lista)



