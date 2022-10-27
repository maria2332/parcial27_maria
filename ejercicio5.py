#Crea un script llamado descomposicion.py que realice las siguientes tareas:
#Debe tomar 1 argumento que será un número entero positivo.
#En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
#El objetivo del script es descomponer el número en unidades, decenas, centenas, miles... tal que por ejemplo si se introduce el número 3287:


import sys

def descomposicion():
    print("Introduce un número entero positivo de 4 cifras")

    numero = input("Tu número: ")
    if len(numero) != 4:
        print("Tu número no es válido, debe contener 4 dígitos")
    else:
        for i in range(3, -1, -1):
            res = numero[i]
            if i == 0:
                n ="1000"
                m = n.replace("1", res)
                print(m)
            elif i == 1:
                n ="0100"
                m = n.replace("1", res)
                print(m)
            elif i == 2:
                n ="0010"
                m = n.replace("1", res)
                print(m)
            elif i == 3:
                n ="0001"
                m = n.replace("1", res)
                print(m)

descomposicion()
