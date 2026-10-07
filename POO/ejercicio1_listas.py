calificaciones = []

totalAlumnos = 10

calificacionAprobatoria = 70

calMax = 0
calMin = 9999999

while len(calificaciones) < totalAlumnos:
    cal = float(input(f"Ingresa la calificacion entre 0 y 100 "))
    if cal <= 100 and cal > 0:
        calificaciones.append(cal)
    else:
        "La calificación debe ser entre 0 y 100"

promedio = sum(calificaciones)/len(calificaciones)

for i in calificaciones:
    if i >= calMax:
        calMax = i
    elif i <= calMin:
        calMin = i


aprobados = 0 
for cal in calificaciones:
    if cal >= calificacionAprobatoria:
        aprobados +=1

print(f"Calificaciones: {calificaciones}")
print(f"Promedio grupal: {promedio}")
print(f"Calificación más alta: {calMax}")
print(f"Calificación más baja: {calMin}")
print(f"Alumnos aprobados: {aprobados} de {totalAlumnos}")
    

def leer_matriz(nombre, n):
    matriz = []
    for j in range(n):
        fila = []
        for k in range(n):
            fila.append(int(input(f"{nombre}[{j}][{k}]: ")))
        matriz.append(fila)
    return matriz


def sumar_matrices(a, b, n):
    resultado = []
    for j in range(n):
        fila = []
        for k in range(n):
            fila.append(a[j][k] + b[j][k])
        resultado.append(fila)
    return resultado


def mostrar_matriz(nombre, matriz):
    print(f"\nMatriz {nombre}:")
    for fila in matriz:
        print(fila)


n = int(input("Tamaño n de las matrices: "))

print("\nMatriz A:")
matriz_a = leer_matriz("A", n)

print("\nMatriz B:")
matriz_b = leer_matriz("B", n)

resultadoMatriz = sumar_matrices(matriz_a, matriz_b, n)

mostrar_matriz("A", matriz_a)
mostrar_matriz("B", matriz_b)
mostrar_matriz("Resultado (A + B)", resultadoMatriz)