#1.Un inspector recibe un numero entero positivo, pero antes debe verificar la siguiente condicion el numero sera aceptado unicamente si todos sus dijitos son pares
# crea una funcion en python que reciba un numero y que devuelva TRUE si cumple con la condicion y FALSE si no la cumple.

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
    while altura <= altMax and altura > altMin:
        if altura <= altMax and altura > altMin:
            altura = altura / 2
            rebotes = rebotes + 1
        if altura < altMin:
            break
    return rebotes
rebotesTotales=(pelota(altMax=int(input("Cual es la altura maxima? ",)))(altMin=int(input("cual es la altura minima? "))))
print(rebotesTotales)
#4. Imaginense un candado que abre unicamente si cumple con las siguientes condiciones, tiene al menos 4 cifras, el primer digito es igual al ultimo, la suma de todos sus digitos es impar y por lo menod tiene un numero 7 dentro de sus digitos.
# desarrolla una funcion en python que devuelva TRUE si se puedo abrir el candado y FALSA si no se abrio.