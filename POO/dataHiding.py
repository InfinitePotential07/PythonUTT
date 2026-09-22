class Cuenta:
    def __init__(self):
        self.__saldo = 0 #Privado
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
    @property
    def saldo(self): #Getter
        return self.__saldo
def main():
        c1=Cuenta()
        c1.depositar(300)
        print(c1.saldo)
main()


class Persona:
    def __init__(self, nombre, edad):
          self.__nombre = nombre #Atributo privado
          self.edad = edad
    #Getter: se utliza el decorador @property
    @property
    def nombre(self):
         return self.__nombre
    #Setter: Se utiliza @nombre.setter
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 0:
              self.__nombre = nuevo_nombre
        else:
             print("El nombre no puede ester vacio.")
#Uso
def main():
    persona1= Persona("Ana", 28)
#Llama automaticamente al Getter
    print(persona1.nombre) #Imprime: Ana
    #Llama automaticamente al ,Setter y valida el dato
    persona1.nombre= "Maria"
    print(persona1.nombre) #Imprime: Maria
main()


