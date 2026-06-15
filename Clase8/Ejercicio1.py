# Desarrolla  un programa en python utilizando el ciclo "while" simulando una cuenta bancaria, donde se mostrará un menú con un saldo inicial
# de 10k pesos, donde el usuario puede depositar, retirar consultar saldo y salir. Para finalizar se debe de mostrar numero de depositos
# realizados, numero de retiros realizados, total depositado y total retirado.
saldo = 10000
cantRetiros = 0
depTotal = 0
retTotal = 0
cantDepositos = 0
print("===== Bienvenido a tu banco UTT ===== \n 1. Retiro 2. Consulta 3. Deposito 4.Salir")
respuesta=int(input("Qué operacion deseas realizar? "))
while respuesta != 4:
    if respuesta == 1:
        retiro=int(input("Cuanto desea retirar?"))
        saldo = saldo - retiro
        cantRetiros = +1
        retTotal = retTotal + retiro
    if respuesta == 2:
        print("Su saldo es de : " ,saldo)
    if respuesta == 3:
        deposito=int(input("Cuanto desea depositar?"))
        saldo = saldo + deposito
        cantDepositos = +1
        depTotal = depTotal + deposito
    else:
        print("Ingrese una opción valida")
    print("1. Retiro 2. Consulta 3. Deposito 4.Salir")    
    respuesta=int(input("Desea realizar otra accion? "))
print("Resumen: \n Numero de depositos: " ,cantDepositos ,"\n Numero de retiros: " ,cantRetiros , "\n El total retirado es de: " ,retTotal ,"\n EL total depositado es de: " ,depTotal)