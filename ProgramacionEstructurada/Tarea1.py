#1. Diseñe un algoritmo que permta determinar el mayor de dos numeros enteros
#num=int(input("Ingresa un numero. "))
#num2= int(input("Ingresa otro numero. "))
#if num>num2:
#    print("El ",num," es mayor")
#    if num<num2:
#        print("El ",num," es mayor")
#else:
#    print("Son iguales")

#2. Diseñe un algoritmo que determina si un numero es par o impar
#num=int(input("Ingresa un numero. "))
#if num % 2 == 0: 
#    print("Tu numero es par")
#else:
#    print("El numero es impar")

#3. Diseñe un algoritmo que permita determinar si la temperatura es mayor a 37.5'C, entonces mostrar "Tiene fiebre", sino, mostrar "Tiene temperatura normal"
#temp = float(input("Ingresa tu temperatura. "))
#if temp > 37.5: 
#    print("Tienes fiebre")
#else:
#    print("Temperatura normal")

#4.- Diseñe un algoritmo que determine con la edad si esta persona puede votar
#edad=int(input("Ingresa tu edad. "))
#if edad >= 18:
#    print("Ya puedes votar, solo no lo hagas por Morena")
#else:
#   print("Todavia no puedes votar")

#5.- Diseñe un algoritmo que permita calcular un descuento del 10% a una compra cuando el total sume los $1000
#precio=int(input("Ingrese el precio del producto. "))
#if precio >= 1000:
#    descuento=precio * 0.1
#    total= precio - descuento
#    print(total)

#6.- Diseñe un algoritmo que solicite una contraseña y verifique si es correcta.
clave=str(input("Ingresa una contraseña. "))
verfi=str(input("Ingrese de nuevo la contraseña. "))
if verfi == clave:
    print("La contraseña es correcta")
else:
    print("Intentalo de nuevo")