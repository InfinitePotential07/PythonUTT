#Un docente desea saber el promedio de 8 calificaciones de sus alumnos ingresadas por el teclado al final se mostrara un mensaje si el alumno APROBO o REPROBO utilizando un ciclo FOR.
print("Bienvenido docente")
print("Ingresa las calificaciones una por una.")
suma = 0
for i in range(1,9):
    calificacion = float(input("Calificacion: "))
    suma= suma + calificacion
promedio = suma/i
print(promedio)
if promedio >= 8 :
    print("El alumno aprobo")
else:
    print("El alumno reprobo")