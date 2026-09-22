#edad = int(input("Ingresa tu edad. "))

#if edad >= 18:
    #print("Eres mayor de edad.")
#else:
    #print("Todavia eres ilegal")#



#########################################

#for i in range(1,11):
    #print(i)

#########################################

#num = int(input("Ingresa un numero. "))
#for i in range(1,11):
    #result = i * num
    #print(num ," x ", i, " = ", result)\

# Escriba un programa que muestre los numero pares del 1 al 20

for i in range(1,21):
    if i % 2 == 0:
        print(i)

# Ingrese los datos de 5 calificaciones una por una y el programa debe calcular el promedio utilizando el FOR 
suma=0
promedio=0
for i in range(1,6):
    calificacion = float(input("Ingresa la calificaion "))
    suma = (suma + calificacion)
promedio = (suma / i)
print("Tu promedio es: ", promedio)

# Realice un programa que muestre en pantalla los numeros del 1 al 10 de forma descentende 
num = 10
for i in range(1,11):
    print(num)
    num = num - 1

