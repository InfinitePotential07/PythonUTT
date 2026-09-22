class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula

    def estudiar(self):
        print(f"{self.nombre} está estudiando")

def main():
    E1=Estudiante("Juan", 20, "1234")
    E1.estudiar()
    E1.saludar()
    E1.nombre="juan carlos"
main()
