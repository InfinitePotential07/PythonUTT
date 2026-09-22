class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    def calcular_pago(self):
        return 0

class EmpleadoPlanta(Empleado):
    def calcular_pago(self):        # Sobreescribe el método
        return 12000

class EmpleadoHonorarios(Empleado):
    def calcular_pago(self):        # Comportamiento distinto
        return 350 * 20
def main():
    for e in [EmpleadoPlanta("Ana"), EmpleadoHonorarios("Luis")]:
        print(e.nombre, e.calcular_pago()) # Mismo método, distinto resultado
main()