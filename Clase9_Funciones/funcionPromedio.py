def saludar():
    print("Miguel Ulises Lopez Teran. Tu edad es de 24 años.")
saludar()

def saludar1(nombre,edad):
    print("Hola ", nombre, ". Tu edad es ", edad)
saludar1("Miguel Ulises Lopez Teran", "24")

def promedio(gd1,gd2,gd3):
    total = (gd1+gd2+gd3)/3
    return total
print(promedio(9,8,10))

def areaTri(h,w):
    area = (w*h)/2
    return area
print("El area del triangulo es: ",areaTri(6,9))
print(promedio(9,8,10))

def areaTri(h,w):
    area = (w*h)/2
    return area
print("El area del triangulo es: ",areaTri(h=int(input("Ingresa la altura ")),w=int(input("Ingresa la base "))))

#Desarrollar una función que imprima o devuelva el mayor de dos numeros
def numMay(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2
print("El numero mas grande es ",numMay(6,9))
