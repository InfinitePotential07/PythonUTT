class Empleado:
    def __init__(self, nombre, apellido, edad, salario=3600):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)
        self.salario = salario

    def aumento_salario(self):
        if self.edad > 40:
            self.salario = self.salario*1.35
            print("Recibiste un aumento")
        else:
            print("No recibiste aumento")
        return self.salario
        
    def informacion(self):
        print(self.nombre)
        print(self.apellido)
        print(self.edad)
        print(self.aumento_salario())
def main():
    empleado1 = Empleado("Luis", "Acosta", 40)
    empleado2 = Empleado("Napoleon", "Perez", 53)
    empleado1.informacion()
    empleado2.informacion()

    empleado1.edad=44
    empleado1.informacion()
main()


