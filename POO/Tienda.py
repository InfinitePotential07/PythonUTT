class Producto:
    #Punto 2. Atributo de clase
    iva = 0.08

    #Punto 1. El constructor con los atributos segun PEP 8
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio + (precio * Producto.iva)
        self.stock = stock

    #Punto 2. Reducir el stock
    def vender(self,cantidad):
        self.stock -= cantidad
        return self.stock

    #Punto 4. classmethod para crear producto
    @classmethod 
    def crear_desde_texto(cls, texto):
        n, p, s = texto.split(",")
        return cls(str(n), int(p), int(s))

    #Punto 3. Metodo estatico independiente de cualquier instancia
    @staticmethod
    def calcular_total(precio, cantidad):
        return (precio * cantidad) + (precio * Producto.iva)        
        

producto1=Producto("Vodka", 500, 100)
producto2=Producto("Asador", 1200, 54)
producto3=Producto("Comedor", 1750, 32)

print(producto1.nombre, producto1.precio, producto1.stock)
print(producto2.nombre, producto2.precio, producto2.stock)
print(producto3.nombre, producto3.precio, producto3.stock)

producto4 = Producto.crear_desde_texto("Espejo, 899, 14")
print(producto4.nombre, producto4.precio, producto4.stock)

total_compra = Producto.calcular_total(producto4.precio, 4)
print(f"4 unidades de {producto4.nombre} es un total de ${total_compra}")

stock_vendido = producto4.vender(4)
print(f"El stock restante de {producto4.nombre} es de {stock_vendido}")
