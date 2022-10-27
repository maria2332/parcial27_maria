def pedir_numero():
    num = input("Tu número: ")
    if len(num) != 4:
        print("Tu número no es válido")
        return str(num)

def descomposicion(numero):
    contador = 0
    while True:
        for digito in numero:
            contador+=1
            print((digito.ljust(int(contador), '0')).zfill(len(numero)), )
        if contador >= len(numero):
            break

descomposicion(pedir_numero()[::-1])
