#Desarrollar en Python un programa utilzando el ciclo while que simule el acceso de un sistema. donde el usuario tiene que ingresar un pin
# o contrana de 4 digitos teniendo un maximo de 5 intentos, despues de esos 5 intentos aparecera un mensaje de cuenta bloqueada. 
# Para finalizar se mostrara cuantos intentos se realizaron y el estado de la cuenta.
pin=1535
intentos = 5
total = 5
while intentos <= 5:
    intentoPin=int(input("Ingresa el PIN "))
    intentos=intentos-1
    if intentoPin != pin and intentos > 0:
        print("PIN incorrecto \n Intenta de nuevo")
        
    elif intentos == 0: 
        print("Cuenta bloqueda")
    else:
        print("Acceso permitido")
        print("Intentos usados " ,(total-intentos))