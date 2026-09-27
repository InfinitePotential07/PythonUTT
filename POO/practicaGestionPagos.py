class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = str(nombre)
        self.sueldo = float(sueldo)

    def informacion(self):
        return f"Nombre: {self.nombre} \nSueldo: ${self.sueldo:,.2f}"

    def mostrar_sueldo(self):
        return self.sueldo

class Vendedor(Empleado):
    def __init__(self, nombre, sueldo, meta_ventas, ventas_realizadas):
         super(). __init__(nombre, sueldo)
         self.meta_ventas = float(meta_ventas)
         self.ventas_realizadas = float(ventas_realizadas)

    def informacion(self):
        return print (f"{super().informacion()} \nMeta: ${self.meta_ventas:,.2f} \nVentas realizadas: ${self.ventas_realizadas:,.2f}")
        

    def sueldo(self):
        return super().sueldo()

    def calcular_sueldo(self):
        if self.ventas_realizadas >= self.meta_ventas:
            print(f"---Meta alcanzada--- \nSu sueldo total es de: ${self.sueldo * 1.10:,.2f}")
        else:
            print(f"---Meta no alcanzada--- \nSu sueldo total es de: ${self.sueldo}")
    
def main():
    empleado1 = Empleado("Pancho Perez", 14543.32)
    empleado1.informacion()
    print("-" * 50)
    vendedor1 = Vendedor("Avocado Haaz", 13312.23, 50000.00, 33600.00)
    vendedor1.informacion()
    vendedor1.calcular_sueldo()
    print("-" * 100)
    vendedor2 = Vendedor("Ulises Lopez", 45000, 15000, 35000)
    vendedor2.informacion()
    vendedor2.calcular_sueldo()
main()