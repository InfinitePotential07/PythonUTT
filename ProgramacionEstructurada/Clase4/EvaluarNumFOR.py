#El programa debe solicitar un numero entero positivo que indique cuantos valores se van a evaluar posteriormente, en cada iteracion se evaluara si es positivo, 0, par o impar.
cant = int(input("Cuantos numeros quieres evaluar? "))
for i in range (0,cant):
    num=int(input("Ingresa el numero: "))
    if num > 0:
        print("El numero " ,num ," es positivo")
        if num % 2 == 0:
            print("El numero es par")
        else:
            print("Es impar")
    elif num == 0:
        print("El numero es 0")
    else:
        print("Numero no valido")

