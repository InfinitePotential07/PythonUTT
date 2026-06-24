#1. Operación matemática simple
def sumar(a, b):
    return a + b

# Guardamos el resultado en 'resultado' para usarlo después
resultado = sumar(5, 3)
print(resultado)  # Muestra 8

#2. Procesar texto
def saludar(nombre):
    return "Hola, " + nombre + "!"

mensaje = saludar("Ulises")
print(mensaje)  # Muestra: Hola, Ulises!

#3. Devolver un valor booleano
def es_par(numero):
    return numero % 2 == 0

print(es_par(4))  # Muestra: True
print(es_par(7))  # Muestra: False

#4. return para salir antes de la función
def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    
    return a / b

print(dividir(10, 0))  # Muestra el aviso y frena ahí
print(dividir(10, 2))  # Muestra 5.0

#5. Devolver múltiples valores
def obtener_min_y_max(lista):
    return min(lista), max(lista)

minimo, maximo = obtener_min_y_max([5, 2, 9, 1])
print("El menor es:", minimo)  # Muestra 1
print("El mayor es:", maximo)  # Muestra 9