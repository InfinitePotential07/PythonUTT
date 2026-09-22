def saludar():
    print("Hola mundo, bienvenido a Python")

saludar()

def despedirse():
    print("Hasta luego")
despedirse()

#Funcion con parametros, argumentos de entrada y sin retorno.
def saludar1(nombre):
    print("Hola", nombre)

saludar1("Ana")

def mostrar_edad(edad):
    print("Tu edad es: ", edad)
mostrar_edad("20")

def mostrar_ciudad(ciudad):
    print("Vives en ", ciudad)
mostrar_ciudad("Tijuana")

#Funciones con paratmetros, argumentos de entrada y con retorno:

def suma1(a,b):
    resultado= a+b
    return resultado
print(suma1(5,6))

def suma(a,b):
    resultado = a+b
    return resultado
resultado_suma = suma(5,3)
print(resultado_suma)

