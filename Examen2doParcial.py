# 1.
def calificaciones():
    cant_calificaciones = int(input("Cuantas calificaciones quiere evaluar? "))
    while cant_calificaciones > 0:
        cantidad = cant_calificaciones
        return cantidad
Cant_Final = calificaciones()
print(Cant_Final)

def promedio(Cant_Final):
    suma = 0 
    for i in range (0,Cant_Final):
        calificacion=int(input("Ingrese calificacion "))
        while calificacion < 0 or calificacion > 100:
            calificacion = int(input("Ingresa ua calificacion dentro del rango: "))
        suma = suma + calificacion
    promedioFinal = suma / Cant_Final 
    i = i + 1
    if promedioFinal >= 70:
        print(promedioFinal)
        print("Aprobado")
    else:
        print(promedioFinal)
        print("Reprobado")
    return promedioFinal
promedio(Cant_Final)

# 2.
def pagoSueldo(horas_trabajadas):
    sueldo = horas_trabajadas * 120
    if horas_trabajadas > 40:
        print("Recibe un bono del 10%")
        bono = sueldo * 0.10
        print(bono)
        sueldo = sueldo + bono
    else:
        print("No recibe bono")
    return sueldo
sueldoFinal= pagoSueldo(horas_trabajadas=int(input("Cuantas horas trabajaste a la semana? ")))
print("El sueldo total a recibir es de ", sueldoFinal)



