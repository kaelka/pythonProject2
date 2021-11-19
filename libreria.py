def valida_natural():
    num = int(input("introdueix un nombre: "))
    while num<1:
        num = int(input("introdueix un nombre: "))
    return num

#tabla de multiplicacion#
def tabla():
    num = int(input("Introdueix el nombre del qual vols generar la taula: "))
    for i in range(0,11):
        print(num, "x", i, "=", num * i)