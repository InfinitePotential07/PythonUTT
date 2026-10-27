try:
    numero = int(input("Ingresa un numero: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except ValueError:
    print("Debes ingresar un numero valido")