menu = 0
menu=(input("Que ejercicio quieres ejecutar? 1-7 "))
match menu:
    case "1":
        def saludar(nombre):
            print("Hola, ", nombre, " bienvenido a Python.")
        nombre = input("Ingresa tu nombre: ")
        saludar(nombre)
    case "2":
        def numeroMayor(num1, num2):
            if num1 > num2:
                return num1
            else:
                return num2
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        mayor = numeroMayor(num1, num2)
        print("El número mayor es: ", mayor)
    case "3":
        #Realizar una funcion que muestre por medio de un for una tabla de multiplicar del numero que el usuario ingrese.
        def tabla(num):
            print("Tabla de multiplicar del ", num)
            for i in range(1, 11):
                resultado = num * i
                print(num, " x ", i, " = ", resultado)
            tabla(num=int(input("Ingresa un número para mostrar su tabla de multiplicar: ")))
    case "4":
        #Realizar un programa que en base a 10 numeros, me diga cuantos fueron ingresados positivos y cuantos negativos.
        def negativosPositivos():
            positivos = 0
            negativos = 0
            for i in range(1,11):
                num=int(input("Ingresa un numero "))
                if num > 0:
                    positivos = positivos + 1
                    print(num)
                else:
                    negativos = negativos + 1
                    print(num)
            print("Numeros negativos = ", negativos, " numeros positivos = ", positivos)
        negativosPositivos()
    case "5":
        #Realizar un programa que en base a 10 numeros, me diga cuantos fueron ingresados pares y cuantos impares.
        def paresImpares():
            par = 0
            impar = 0
            for i in range(1,11):
                num=int(input("Ingresa un numero "))
                if num % 2 == 0 :
                    par = par + 1
                else:
                    impar = impar + 1
            print("Numeros pares = ", par, " numeros impares = ", impar)
        paresImpares()
    case "6":
        #Desarrollar un programa que en base a la compra de 1000 pesos hacia arriba haga un descuento del 5% 
        def compraOff(compra):
            if compra >= 1000:
                print("Aplica descuento del 5%")
                total = compra * 0.95
                print("Total a pagar: ", total)
            else:
                print("No aplica descuento")
                print("Total a pagar es de: ", compra)
        compraOff(compra=float(input("Cuanto compraste? ")))
    case "7":
        #Desarrollar un programa que muestre las calificiones de un alumno en base a reprobado, de panzazo, aprobado y excelente.
        def estadoAlumno():
            materias=int(input("Cuantas calificaciones ingresaras? "))
            for i in range (0,materias):
                grade=float(input("Ingresa la califcacion "))
                if grade >= 9:
                    print("El alumno tiene una calificacion excelente")
                elif grade >=8 and grade < 9:
                    print("El alumno está aprobado")
                elif grade >= 7 and grade < 8:
                    print("El alumno pasó de panzazo")
                else:
                    print("El alumno reprobó")
        estadoAlumno()    
