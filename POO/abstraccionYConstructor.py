class Alumno:
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.materias = []

    def inscribir_materia(self, materia):
        self.materias.append(materia)

    def imprimir_ficha(self):
        print(f"{self.nombre} - {self.carrera} ({len(self.materias)} materias)")

def main():
    a1 = Alumno("Ana Lopez", "20231045", "Ing. en Sistemas")
    a2 = Alumno("Luis Marín", "20231046", "Mecatónica")
    a1.inscribir_materia("POO")
    a1.inscribir_materia("BD")
    a1.imprimir_ficha()

main()
class Vehiculo:
    def __init__(self, marca, modelo, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad += incremento

auto1 = Vehiculo("Nissan", "Versa")
auto2 = Vehiculo("Mazda", "CX-5", 20)
auto1.acelerar(15)
print(auto1.velocidad)