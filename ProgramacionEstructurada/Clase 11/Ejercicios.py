#1.Un inspector recibe un numero entero positivo, pero antes debe verificar la siguiente condicion el numero sera aceptado unicamente si todos sus dijitos son pares.
#crea una funcion en python que reciba un numero y que devuelva TRUE si cumple con la condicion y FALSE si no la cumple.
def checkNum(num):
    if num == 0:
        return True
    while num > 0:
        digito = num % 10
        if digito % 2 != 0:
            return False
        num = int((num - digito) / 10)
    return True
validacion=(checkNum(int(input("Ingresa un numero entero positivo "))))
print(validacion)
#2. Imaginemos a un niño jugando en una escalera al dar el primer paso sube un escalon, al dar el segundo paso sube dos escalones, al dar el tercer paso vuelve a subir un escalon, al dar el cuarto paso sube de nuevo 2 escalones y asi sucesivamente
# desarrolle una funcon en pasos que reciba la cantdad de escalones a subir y devuelva cuantos pasos necesita el niño para superar el ultimo escalon.
def escaleras(cantEsc):
    pasos = 0
    numEsc = 0
    while numEsc < cantEsc:
        if pasos % 2 != 0:
            pasos = pasos + 1
            numEsc = numEsc + 1
        elif pasos % 2 == 0:
            pasos = pasos + 1
            numEsc = numEsc + 2
    return pasos
pasosTotales=(escaleras(cantEsc=int(input("Ingresa la cantidad de escaleras "))))
print("El niño dio un total de ", pasosTotales, " pasos.")
#3. Una pelota rebota varias veces, cada rebote alcanza exactamente la mitad de la altura anterior.
# desarrolle una funcion en python que reciba la altura inicial y la altura minima y debe devolver cuantos rebotes se realizaron hasta que la altura sea menor a la minima dada.
def pelota(altMax, altMin):
    rebotes = 0
    altura = altMax
    while altura > altMin:
        if altura > altMin:
            rebotes = rebotes + 1
            altura = altura / 2
    return rebotes
rebotesTotales=(pelota(altMax=int(input("Ingresa la altura maxima de la pelota en cm ")), altMin=int(input("Ingresa la altura minima de la pelota en cm"))))
print(rebotesTotales)
#4. Imaginense un candado que abre unicamente si cumple con las siguientes condiciones, tiene al menos 4 cifras, el primer digito es igual al ultimo, la suma de todos sus digitos es impar y por lo menod tiene un numero 7 dentro de sus digitos.
# desarrolla una funcion en python que devuelva TRUE si se puedo abrir el candado y FALSA si no se abrio.
def candado(dig1, dig2, dig3, dig4):
    if dig1 == dig4 and (dig1 + dig2 + dig3 + dig4) % 2 != 0 and (dig1 == 7 or dig2 == 7 or dig3 == 7 or dig4 == 7):
        return True
    else:
        return False
estado=(candado(dig1=int(input("Ingresa el primer digito del candado ")), dig2=int(input("Ingresa el segundo digito del candado ")), dig3=int(input("Ingresa el tercer digito del candado ")), dig4=int(input("Ingresa el cuarto digito del candado "))))
print("El candado se abrio: ", estado)