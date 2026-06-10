""""num = 0
while num < 10:
    print(f"El numero es {num}!")
    num = num + 1

palabra_secreta = "python"
counter = 0

while True:
    palabra = input("Ingresa la palabra secreta: ").lower()
    counter = counter + 1
    if palabra == palabra_secreta:
        break
    if palabra != palabra_secreta and counter > 7: 
        break

#1 Contador regresivo
contador = 5
print("Iniciando cuenta regresiva")
while contador > 0:
    print(contador)
    contador -= 1 #restar 1 de manera mas corta
print("¡Despegue viejon!🚀")

#2 Validar una entrada del usuario
pswd_correcto = "python123"
intento = ""
while intento != pswd_correcto:
    intento = input("Ingresa la contraseña: ")
print("Acceso concedido. Bienvenido señór mio")

#3 Preguntar hasta que digas "si"
respuesta = "no"

while respuesta == "no":
    respuesta = input("¿Ya merito llegamos 🫏? (sí/no): ")

print("Ok, me detengo. ¡Adiós!")

#4 Aplaudiendo con energia
energia = 3

while energia > 0:
    print("¡CLAP! 👏")
    energia -= 1

print("Te cansaste. Fin del juego.")"""

#1 Cajero automatico
while True:
    pin = input("Ingresa tu PIN de 4 digitos: ")
    if pin == "1234":
        print("PIN correcto. Entrando a la Deep Web")
        break 
#2 Lanzar un dado hasta que salga un 6
import random

while True:
    dado = random.randint(1, 6) #Esto ayuda a generar un numero random
    print(f"Salió un: {dado}")
    
    if dado == 6:
        print("¡Ganaste! Salió el 6.")
        break

#3 Sumar numeros hasta que pongas un 0
total = 0

while True:
    num = int(input("Introduce un número para sumar (0 para terminar): "))
    if num == 0:
        break  # Si es cero, se acaba el ciclo
    total = total + num
    print(f"Suma actual: {total}")

print(f"Juego terminado. El total final es: {total}")

#4 Confirmacion de la salida de un juego
while True:
    print("Jugando partida épica")
    #Simulamos que el usuario intenta salir
    seguro = input("¿Seguro que quieres salir del juego? (si/no): ")
    if seguro == "si":
        print("Guardando partida... Adios.")
        break