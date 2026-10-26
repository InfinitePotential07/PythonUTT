class Producto:
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self._precio_base = precio_base
        self.__descuento = 0.0 #este atributo descuento no es necesario ponerlo en el constructor cuando esa variable siempre tendra el  mismo valor
    @property
    def descuento(self):
        return self.__descuento
    @descuento.setter
    def descuento(self, nuevo_descuento):
        if 0.0 <= nuevo_descuento <= 0.9:
            self.__descuento = nuevo_descuento
        else:
            raise ValueError("El descuento debe estar entre (0%) y (90%).")
    @property
    def precio_final(self):
        return self._precio_base * (1 - self.__descuento)

def main():
    prod2 = Producto("Telefono Premium", 800.0)
    prod2.descuento = 0.20
    print(f"Producto: {prod2.nombre}")
    print(f"Descuento aplicado: {prod2.descuento * 100}%")
    print(f"Precio Final: ${prod2.precio_final}")
main()

