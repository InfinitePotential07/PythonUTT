"""class Empleado:
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    def calcular_pago(self):
        return self.salario_base


class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super(). __init__(nombre, salario_base) #Reutiliza el padre
        self.bono = bono

    def calcular_pago(self):                       #Sobreescribe
        return super().calcular_pago() + self.bono # y reutiliza """

class Nadador:
    def nadar(self):
        print("Nadando")

class Corredor:
    def correr(self):
        print("Corriendo")

class Triatleta(Nadador, Corredor): #Hereda ambas
    def competir(self):
        self.nadar()
        self.correr()

atleta = Triatleta()
atleta.competir() #Nadando / Corriendo

print(Triatleta.__mro__) #Orden de busqueda de métodos


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_perfil(self):
        return f"Nombre: {self.nombre} \nEdad: {self.edad} años"

class Trabajador:
    def __init__(self, salario_base):
        self.salario_base = salario_base

    def calcular_pago(self, bonos = 0):
        return self.salario_base + bonos

class Profesor(Persona, Trabajador):
    def __init__(self, nombre, edad, salario_base, cubiculo):
        Persona.__init__(self, nombre, edad)
        Trabajador.__init__(self, salario_base)
        self.cubiculo = cubiculo

    def generar_reporte_nomina(self):
        perfil = self.mostrar_perfil()
        pago_total = self.calcular_pago(bonos = 150)

        return f"{perfil} \nCubiculo: {self.cubiculo} \nPago neto: ${pago_total}"

def main():
    profesor_poo = Profesor("Dra. Martinez", 42, 2500.0, "Docencia 1 - 204")
    print(profesor_poo.generar_reporte_nomina())
main()
        