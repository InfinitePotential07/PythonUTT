mayor = 0
menor = 9999999
num=0
for i in range(0,5):
    num=int(input("Ingresar numero: "))
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
        
print("El numero mayor es: ",mayor ," y el numero menor es: ",menor)