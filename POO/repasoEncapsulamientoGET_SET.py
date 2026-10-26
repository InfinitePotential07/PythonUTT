class Producto:
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self._precio_base = precio_base
        self.__descuento = 0.0
        
    def get_descuento(self):
        return self.__descuento
    
    def set_descuento(self, nuevo_descuento):
        if 0.0 <= nuevo_descuento <= 0.9:
            self.__descuento = nuevo_descuento
        else:
            raise ValueError("El descuento debe estar entre (0%) y (90%).")
        
    def precio_final(self):
        return self._precio_base * (1 - self.__descuento)

def main():
    prod2 = Producto("Telefono Premium", 800.00)
    prod2.set_descuento(0.20)
    print(f"Producto: {prod2.nombre}")
    print(f"Descuento aplicado: {prod2.get_descuento() * 100}%")
    print(f"Precio Final: ${prod2.precio_final()}")
main()