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
        ventaAlta = 2000
        ventaBaja = 0
        ventaNormal = 1000
        cantVA = 0
        cantVB = 0
        cantVN = 0
        dias=int(input("Cuantos dias deseas ingresar? "))
        for i in range (0,dias):
            print("Cuanto vendiste el dia ", i+1 ," ?")
            ventasDia=int(input())
            if ventasDia >= ventaAlta:
                print("Excelente dia de ventas")
                cantVA = cantVA + 1
            elif ventasDia >= ventaNormal:
                print("Dia de ventas normal")
                cantVN = cantVN + 1
            elif ventasDia >= ventaBaja:
                print("Dia de ventas bajo")
                cantVB = cantVB + 1
            else:
                print("Malisimo dia de ventas")
        print("Tuviste ", cantVA," dia/s de ventas altas, ",cantVN," dia/s de ventas normales y ",cantVB," dia/s de ventas bajas")
    case "5":
        #5. Evaluación de temperaturas
        tempAlta = 40
        tempNormal = 37.5
        tempBaja = 35
        cantAlta = 0
        cantBaja = 0
        cantTemp=int(input("A cuantas personas revisaste hoy?"))
        for i in range(0,cantTemp):
           temp=float(input("Cual es la temperatura de la persona? "))
           if temp >= tempAlta:
               print("La persona tiene temperatura alta")
               cantAlta = cantAlta + 1
           elif temp >= tempNormal:
               print("La persona tiene temperatura normal")
           else:
               print("La persona tiene hipotermia")
               cantBaja = cantBaja + 1
        print("De las ", cantTemp," personas que revisaste, " ,cantAlta ," tienen temperatura alta y " ,cantBaja ," tienen hipotermia")
    case "6":
        #6. Cajero automático básico
          saldo = 10000
          print("Bienvenido al cajero UTTVA")
          monto=int(input("Cuanto desea retirar?"))
          if monto ==saldo:
              print("Retiro exitoso y justo, su nuevo saldo es de ", saldo - monto)
          elif monto < saldo:
              print ("Aun le queda saldo, su nuevo saldo es de ", saldo - monto)
          else:
              print("Saldo insuficiente, su saldo actual es de ", saldo)
          
    case "7":
        #7. Clasificación de edades
        menor = 0
        mayor = 0
        tercera = 0
        cantPer=int(input("Cuantas personas quieres ingresar? "))
        for i in range(0,cantPer):
            edad=int(input("Cuantos años tiene la persona? "))
            if edad < 18:
                print("La persona es menor de edad")
                menor = menor + 1
            elif edad >= 18 and edad < 60:
                print("La persona es mayor de edad")
                mayor = mayor + 1
            elif edad >= 60:
                print("La persona es adulto mayor")
                tercera = tercera + 1
        print("De las " ,cantPer ," personas registradas, " ,menor ," son menores de edad, " ,mayor ," son mayores de edad y " ,tercera ," son adultos mayores")
    case "8":
        #8. Evaluación de desempeño laboral
        excelente = 10
        bueno = 9
        aceptable = 8
        deficiente = 7
        cantExcelente = 0
        cantBueno = 0
        cantAceptable = 0
        cantDeficiente = 0
        cantEmp=int(input("Cuantos empleados tienes? "))
        for i in range(0,cantEmp):
            calif=int(input("Cual es la calificacion del empleado? "))
            if calif >= excelente:
                print("El empleado tiene un desempeño excelente")
                cantExcelente = cantExcelente + 1
            elif calif >= bueno:
                print("El empleado tiene un desempeño bueno")
                cantBueno = cantBueno + 1
            elif calif >= aceptable:
                print("El empleado tiene un desempeño aceptable")
                cantAceptable = cantAceptable + 1
            elif calif <= deficiente:
                print("El empleado tiene un desempeño deficiente")   
                cantDeficiente = cantDeficiente + 1
        print("De los ", cantEmp ," empleados, ", cantExcelente ," tienen un desempeño excelente, ", cantBueno ," tienen un desempeño bueno, ", cantAceptable ," tienen un desempeño aceptable y " ,cantDeficiente ," tienen un desempeño deficiente")
    case "9":
        #9. Control de inventario
        brownies = 15
        reposicion = 0
        cantRevisado=int(input("Cuantas veces revisaste los brownies?"))
        for i in range (0,cantRevisado):
            checkBrownies=int(input("Cuantos brownies quedan?"))
            if checkBrownies >= brownies:
                print("Hay stock suficiente")
            elif checkBrownies < brownies and checkBrownies > 8:
                print("Hay stock bajo, considera surtir mas")
                reposicion = reposicion + 1
            else:
                print("No hay stock, ve a surtir ya")
                reposicion = reposicion + 1
        print("Revisaste el inventario ", cantRevisado ," veces, y tuviste que surtir ", reposicion ," veces")
    case "10":
        #10. Horas trabajadas
        jornada = 8
        media = 4
        diasCompletos = 0
        diasMedios = 0
        diasIncompletos = 0
        dias=int(input("Cuantos dias trabajo el empleado?"))
        for i in range(0,dias):
            horas=int(input("Cuantos horas trabajo el dia ", i+1 ,"? "))
            if horas >= jornada:
                print("El empleado hizo su jornada completa")
                diasCompletos = diasCompletos + 1
            elif horas >= media:
                print("El empleado trabajó medio dia")
                diasMedios = diasMedios + 1
            else:
                print("El empleado trabajó un dia incompleto")
                diasIncompletos = diasIncompletos + 1
        print("De todos los dias que trabajo el empleado, ", diasCompletos ," fueron jornadas completas, ", diasMedios ," fueron medios dias y ", diasIncompletos ," fueron dias incompletos")    
    case _:
        print("Opcion no valida, por favor ingresa un numero del 1 al 10")