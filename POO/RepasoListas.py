mi_lista = []

#Lista con valores
numero = [10, 20, 30, 40, 50]
nombres = ["Ana", "Luis", "Maria"]
mixta = [1, "hola", 3.14, True] #Tipos mixtos
print(nombres[2])

frutas=["Manzana", "pera", "uva", "kiwi", "mango"]
print(frutas[0])   # -> manzana    (primer elemento)
print(frutas[2])   # -> uva
print(frutas[-1])  # -> mango      (ultimo elemento)
print(frutas[-2])  # -> kiwi

#Slicing (rebanado)
print(frutas[1:4])  # -> ["pera", "uva", "kiwi"]
print(frutas[:3])   # -> ["manzana", "pera", "uva"]


# - Modificar elemento -
nums = [10, 20, 30]
nums[1] = 99
print(nums)

# - Agregar elemento -
nums.append(40)
nums.insert(0, 5)
print(nums) # [5, 10, 99, 30, 40]

# - Eliminar elementos -
nums.remove(99)        # por valor

ultimo = nums.pop()     # extrae el ultimo

# - Longitud y pertenencia -
print(len(nums))   # 3
print(30 in nums)  # True
print(99 in nums)  # False

# - FOR clasico - 
calificaciones = [85, 92, 78, 95, 88]

for cal in calificaciones:
    print(f"Calificaciones: {cal}")

# Con enumerate (indice + valor)
for i, cal in enumerate(calificaciones):
    print(f"Alumno {i+1}: {cal}")

# - While + indice
precios =[150, 230, 95, 400, 75]
i = 0

"""while i < len(precios):
    print(f"Precio: ${precios[i]}")"""


# Crear matriz 3x3 
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[1][2])      # -> 6 (fila 1, col 2)

#Recorrer todos los elementos
for fila in matriz:
    for elem in fila:
        print(elem, end=" ")