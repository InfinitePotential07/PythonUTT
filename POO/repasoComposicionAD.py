#Ejercicio 1. Computadora
class CPU:
    def __init__(self, nombre, nucleos, velocidad):
        self.nombre = nombre
        self.nucleos = nucleos
        self.velocidad = velocidad
    def procesar(self):
        return "Procesando..."

class RAM:
    def __init__(self, capacidad_gb):
        self.capacidad_gb = capacidad_gb

    def cargar(self, programa):
        return f"Cargando {programa} en la RAM."

class Disco:
    def __init__(self, capacidad_gb):
        self.capacidad_gb = capacidad_gb

    def guardar(self, dato):
        return f"Guardando {dato} en el disco."

class Computadora:
    def __init__(self):
        self.cpu = CPU("AMD Ryzen 9 5600x",8, 5.5)
        self.ram = RAM(32)
        self.disco = Disco(2000)

    def ejecutar_programa(self, nombre):
        print(self.ram.cargar("Minecraft"))
        print(self.cpu.procesar())
        print(self.disco.guardar("Minecraft"))

def main():

    pc = Computadora()
    pc.ejecutar_programa("Chrome")
main()

    