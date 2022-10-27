# *Convertir la variable "var_1" en todas las letras mayúsculas y en minúsculas (var_1 = "Módulo 1 de Python ")
#*Consulta el tamaño o la longitud de la variable "var_1" y calcula la división de ese numero entre "7" redondeado a 4 decimales
#*Realiza una función llamada funcion1  que calcule siguiente operación para que el resultado final sea igual a cero (0) //12 - (4 * 2) - (2 + 2)
#*Realiza una función llamada funcion2 para que calcule la siguiente operación para que el resultado final sea igual a catorce ope
#*Realiza una función llamda funcion3 para pedir al usuario que introduzca su edad, y después imprimir en la pantalla si es meyor de edad o no

def mayusculas(var_1):
    var_1 = [x.upper() for x in var_1]
    print(var_1)
    print(len(var_1))
    numero = (len(var_1) / 7)
    print(round(numero,4))
var_1 = ["Módulo 1 de Python "]
mayusculas(var_1)
    


def funcion1():
    operacion = 12 - (4 * 2) - (2 + 2)
    print(operacion)

funcion1()



def funcion2():
    op = (14)// 12 - 4 * (2 - 2) + 2
    print(op + 11)
funcion2()



def funcion3():
    edad = int(input("Introduzca su edad: "))
    if edad < 18 :
        print("su edad es:", edad,"Es menor de edad")
    else: 
        print("su edad es:", edad,"Es mayor de edad")
    print (edad)
funcion3()