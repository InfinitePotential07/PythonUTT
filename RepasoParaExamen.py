#1. Realice un programa que solicite un número entero positivo. El programa deberá enviar el número como parámetro a una función que determine si es un número equilibrado. 
# La función deberá calcular la suma de sus dígitos utilizando un ciclo while y determinar mediante un if si la suma de los dígitos es mayor, menor o igual al último dígito del número. 
# La función deberá devolver mediante return el mensaje correspondiente de equilibrado.
def es_equilibrado(num):
    while num > 0:
        ultimo_digito = num % 10
        suma_digitos = 0
        temp_num = num // 10 
        while temp_num > 0:
            suma_digitos += temp_num % 10
            temp_num //= 10
        if suma_digitos > ultimo_digito:
            return "El número no es equilibrado: la suma de los dígitos es mayor que el último dígito."
        elif suma_digitos < ultimo_digito:
            return "El número no es equilibrado: la suma de los dígitos es menor que el último dígito."
        else:
            return "El número es equilibrado: la suma de los dígitos es igual al último dígito."
        
print(es_equilibrado(num=int(input("Ingrese un número entero positivo: "))))
    