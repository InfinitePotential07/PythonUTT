menu = 0
menu=(input("Que ejercicio quieres ejecutar? 1-10 "))
match menu:
    case "1":
        #1. Promedio y clasificación de calificaciones
        suma = 0
        promedio = 0
        cant=int(input("Cuantas calificaciones vas a ingresar? "))
        for i in range (0,cant):
            grade=int(input("Ingresa la calificacion "))
            suma = suma + grade
        promedio = suma / cant
        if promedio == 10:
            print("El promedio final es de ",promedio," EXCELENTE")
        elif promedio >= 9:
            print("El promedio final es de ",promedio, " BUENA") 
        elif promedio >=8:
            print("El promedio final es de ",promedio," SUFICIENTE")
        elif promedio <8:
            print("El promedio final es de ",promedio," NO ACREDITADA") 
    case "2":
        #2. Conteo de números pares e impares
        pares=0
        impares=0
        cant=int(input("Cuantos numeros deseas ingresar? "))
        for i in range (0,cant):
            num=int(input("Ingresa el numero "))
            if num % 2 == 0:
                print("El numero es par")
                pares = pares + 1
            else:
                print("El numero es impar")
                impares=impares + 1
        print("Hay ", pares," par/pares y ",impares ," impar/impares")
    case "3":
        #3. Control de asistencia semanal
        asisTotal=int(input("Cuantas asistencia tuvo en la semana? "))
        if asisTotal < 4:
            print("No cuanta con la asistencia minima. Reprobado")
        else:
            print("Asistencia suficiente. Aprobado")
    case "4":
        #4. Ventas diarias
        