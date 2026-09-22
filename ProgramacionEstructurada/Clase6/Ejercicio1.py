#Acumulador condicionado con reinicio. Al insertar por el usuario 10 valores, si es numero positivo se sumará,
#si es numero negativo se restará y si es 0 se va a reiniciar. 
#Al final se va a mostrar el valor final del acumulador.
print("Ingresa 10 valores")
suma = 0
for i in range (0,10):
    num=int(input())
    if num >0:
        print("Numero positivo")
        suma = suma + num
    elif num < 0:
        print("Numero negativo")
        suma = suma + num
    elif num == 0:
        suma = 0
print("El resultado total es de: ",suma)
