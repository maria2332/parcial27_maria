#Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:
#Borrar los elementos duplicados.
#Ordenar la lista de mayor a menor.
#Eliminar todos los números impares.
#Realizar una suma de todos los números que quedan.
#Añadir como primer elemento de la lista la suma realizada.
#Devolver la lista modificada.
#Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:

lista = [17, 24, 2, 13, 5, 5, 5, 13, 68]
print("Esta es la lista original: ", lista)

def modificar():
  lista1=list(set(lista))
  print("Lista sin elementos duplicados:", lista1)

  lista1=sorted(lista1, reverse=True)
  print("Lista ordenada de mayor a menor:", lista1)
  
  lista2=[]
  for n in lista1:
    if n % 2 == 0:
      lista2.append(n)
    else:
      pass

  print("Esta es la lista sin impares:" +     str(lista2))

  sumalista2= sum(lista2)
  print("La suma de los elementos de la lista que quedan:",           sumalista2)

  lista2.append(sumalista2)
  lista2=sorted(lista2, reverse=True)

  print("Comprobacion de la suma de todos los números a partir del segundo, concuerda con el primer número de la lista:",lista2)

  print("",lista2[0]==sum(lista2[1:]),"")

modificar()