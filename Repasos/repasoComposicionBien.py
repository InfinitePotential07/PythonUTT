class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
            self.__nombre = nuevo_nombre

    def get_precio(self):
            return self.__precio

    def set_precio(self, nuevo_precio):
            self.__precio = nuevo_precio

    def __str__(self):
        return f"{self.__nombre} - {self.__precio}"

class Tienda:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__productos = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_productos(self):
        return self.__productos

    def set_productos(self, nuevos_productos):
        if isinstance(nuevos_productos, list):
            self.__productos = nuevos_productos
        else:
            print("Error: debe ser una lista")

    def agregar_producto(self, nombre, precio):
        producto = Producto(nombre, precio)
        self.__productos.append(producto)

    def mostrar_productos(self):
        print(f"Tienda: {self.__nombre}")
        for i, producto in enumerate(self.__productos, start = 1):
            print(f"{i}. {producto}")

    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                return producto
        else:
            return None

    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto is not None:
            self.__productos.remove(producto)
        else:
            print("Error: el producto no existe")
def main():

    tienda1 = Tienda("Abarrotes El Mike")

    tienda1.agregar_producto("Queso de abeja", 80)
    tienda1.agregar_producto("Masa para tostadas", 55)
    tienda1.agregar_producto("Agua en polvo", 20)

    tienda1.mostrar_productos()

main()