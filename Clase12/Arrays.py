"""# Un arreglo unidimensional (una fila de datos)
notas = [90, 85, 100, 78]

# Acceder al primer elemento (recuerda que empieza en 0)
print(notas[0])  # Resultado: 90

# Agregar un nuevo elemento al final
notas.append(92)
print(notas)  # Resultado: [90, 85, 100, 78, 92]

import array as arr

# La 'i' significa que este arreglo SOLO aceptará números enteros (integers)
numeros = arr.array('i', [10, 20, 30, 40])

# Acceder a un elemento es igual que en las listas
print(numeros[2])  # Resultado: 30

# Si intentas hacer esto, dará error porque no es un entero:
# numeros.append("Hola")

import numpy as np

# Creamos una matriz de 2 filas y 3 columnas
# Fila 1: [1, 2, 3]  |  Fila 2: [4, 5, 6]
matriz = np.array([[1, 2, 3], [4, 5, 6]])

# Ver la matriz completa
print(matriz)
# Resultado:
# [[1 2 3]
#  [4 5 6]]

# Acceder a un dato específico: matriz[fila, columna]
# Queremos el número en la fila 1, columna 2 (contando desde 0)
print(matriz[1, 2])  # Resultado: 6

# 1. Escribir en el archivo (Modo 'w' de Write)
with open("saludo.txt", "w") as archivo:
    archivo.write("¡Hola! Este es un archivo creado desde Python.")

# 2. Leer el archivo (Modo 'r' de Read)
with open("saludo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)  # Imprime: ¡Hola! Este es un archivo creado desde Python.

import os

# 1. Crear una carpeta llamada 'MisDocumentos'
os.mkdir("MisDocumentos")

# 2. Listar y mostrar en pantalla todo lo que hay en la carpeta actual
elementos = os.listdir(".")
print("Archivos y carpetas actuales:", elementos)
# Verás en la lista tu archivo 'saludo.txt' y la carpeta 'MisDocumentos'


# Añadimos una línea al archivo que ya teníamos (o se crea si no existe)
with open("diario.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Hoy aprendí a manejar archivos en Python.\n")

# Si corres este código varias veces, verás cómo se van acumulando las líneas."""