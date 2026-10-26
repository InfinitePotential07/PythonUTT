class CPU:
    def _init_(self, modelo, velocidad):
        self.modelo = modelo
        self.velocidad = velocidad

    def obtener_descripcion(self):
        return f"CPU: {self.modelo}. {self.velocidad} GHz.)"
    
class RAM:
    def _init_(self, capacidad, modelo):
        self.capacidad = capacidad
        self.modelo = modelo

    def obtener_descripcion(self):
        return f"RAM: {self.capacidad} GB {self.modelo}."

class DiscoDuro:
    def _init_(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

    def obtener_descripcion(self):
        return f"Almacenamiento: {self.capacidad} GB {self.tipo}"

class Computadora:
    def _init_(self, marca, modelo, CPU, RAM, DiscoDuro):
        self.marca = marca
        self.modelo = modelo
        self.CPU = CPU
        self.RAM = RAM
        self.DiscoDuro = DiscoDuro

    def mostrar_configuracion(self):
            print(f" CONFIGURACIÓN DEL SISTEMA: {self.marca} {self.modelo}")
            print(f" {self.CPU.obtener_descripcion()}")
            print(f" {self.RAM.obtener_descripcion()}")
            print(f" {self.DiscoDuro.obtener_descripcion()}")

def main():
    mi_cpu = CPU(modelo="Intel Core i9", velocidad=3.4)
    mi_ram = RAM(capacidad=32, modelo="DDR5")
    mi_disco = DiscoDuro(capacidad=1000, tipo="SSD NVMe M.2")
    mi_pc = Computadora(marca="DELL", modelo="CELERION", CPU=mi_cpu, RAM=mi_ram, DiscoDuro=mi_disco)
    mi_pc.mostrar_configuracion()
main()