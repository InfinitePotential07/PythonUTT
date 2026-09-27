class TarjetaCafe:
    def __init__ (self, nombre_cliente, codigo_tarjeta):
        self.nombre_cliente = nombre_cliente
        self.codigo_tarjeta = codigo_tarjeta
        self.__sellos = 0       #Fuera de los parametros
        self.__cafes_gratis = 0 #porque nadie puede crear una tarjeta con sellos ni cafes acumulados

    def get_sellos(self):
        return self.__sellos
    def set_sellos(self):
        self.__sellos += 1
    def del_sellos(self):
        self.__sellos = 0
    def menos_sello(self):
        self.__sellos -= 1

    def get_cafes_gratis(self):
        return self.__cafes_gratis
    def set_cafes_gratis(self):
        self.__cafes_gratis += 1
    def del_cafes_gratis(self):
        self.__cafes_gratis -= 1
    
    def comprar_cafe(self):
        self.set_sellos()
        if self.get_sellos() < 5:
            print(f"Llevas {self.get_sellos()}/5 sellos.")
        elif self.get_sellos() >= 5:
            self.del_sellos()
            self.set_cafes_gratis()
            print("Conseguiste un cafe gratis")

    def canjear_cafe_gratis(self):
        if self.get_cafes_gratis() > 0:
            self.del_cafes_gratis()
            print("Has canjeado un café gratis")
        else:
            print("No tienes cafés gratis para canjear")

    def regalar_sello(self, otra_tarjeta):
        if self.get_sellos() > 0 and otra_tarjeta.get_sellos() < 5:
            self.menos_sello()
            otra_tarjeta.set_sellos()
            print(f"Regalo exitoso {otra_tarjeta.nombre_cliente} ahora tiene {otra_tarjeta.get_sellos()}")
            if otra_tarjeta.get_sellos() >= 5:
                otra_tarjeta.del_sellos()
                otra_tarjeta.set_cafes_gratis()
                print("Conseguiste un cafe gratis")
        else:
            print("No tienes sellos para dar")

class TarjetaCafeVIP(TarjetaCafe):
    def __init__(self, nombre_cliente, codigo_tarjeta, nivel_vip):
        super().__init__(nombre_cliente, codigo_tarjeta)
        self.nivel_vip = nivel_vip

    def comprar_cafe(self):
        self.set_sellos()
        if self.get_sellos() < 3:
            print(f"Llevas {self.get_sellos()}/3 sellos.")
        elif self.get_sellos() >= 3:
            self.del_sellos()
            self.set_cafes_gratis()
            print("Conseguiste un cafe gratis")

    def beneficio_vip(self):
        print(f"Como cliente {self.nivel_vip}, tienes envio gratis en tus compras de café en grano.")



def main():
    tarjeta1 = TarjetaCafe("Ana Gómez", "CAF001")
    tarjeta2 = TarjetaCafe("Pedro Ruiz", "CAF002")

    print(f"--- {tarjeta1.nombre_cliente} compra 5 cafés seguidos ---")
    tarjeta1.comprar_cafe()
    tarjeta1.comprar_cafe()
    tarjeta1.comprar_cafe()
    tarjeta1.comprar_cafe()
    tarjeta1.comprar_cafe()  # en la 5ta debería ganar un café gratis
    print(f"Sellos actuales: {tarjeta1.get_sellos()}")
    print(f"Cafés gratis actuales: {tarjeta1.get_cafes_gratis()}")
    print("-" * 50)

    print(f"--- {tarjeta1.nombre_cliente} canjea su café gratis ---")
    tarjeta1.canjear_cafe_gratis()
    print(f"Cafés gratis actuales: {tarjeta1.get_cafes_gratis()}")
    print("-" * 50)

    print(f"--- {tarjeta1.nombre_cliente} intenta canjear otro (debería fallar) ---")
    tarjeta1.canjear_cafe_gratis()
    print("-" * 50)

    print(f"--- {tarjeta2.nombre_cliente} compra 3 cafés ---")
    tarjeta2.comprar_cafe()
    tarjeta2.comprar_cafe()
    tarjeta2.comprar_cafe()
    print(f"Sellos de {tarjeta2.nombre_cliente}: {tarjeta2.get_sellos()}")
    print("-" * 50)

    print(f"--- {tarjeta1.nombre_cliente} le regala un sello a {tarjeta2.nombre_cliente} (caso exitoso) ---")
    tarjeta1.comprar_cafe()  # le damos 1 sello a tarjeta1 para que tenga con qué regalar
    print(f"Sellos de {tarjeta1.nombre_cliente} antes de regalar: {tarjeta1.get_sellos()}")
    tarjeta1.regalar_sello(tarjeta2)
    print(f"Sellos de {tarjeta1.nombre_cliente}: {tarjeta1.get_sellos()}")
    print(f"Sellos de {tarjeta2.nombre_cliente}: {tarjeta2.get_sellos()}")
    print("-" * 50)

    print(f"--- {tarjeta2.nombre_cliente} intenta regalar un sello sin tener (caso fallido) ---")
    tarjeta2.del_sellos()  # forzamos que se quede en 0 sellos
    tarjeta2.regalar_sello(tarjeta1)
    print("-" * 50)

    print(f"--- Probamos que el regalo también puede completar los 5 sellos ---")
    tarjeta3 = TarjetaCafe("Luis Mena", "CAF003")
    tarjeta4 = TarjetaCafe("Sofía Reyes", "CAF004")
    tarjeta3.comprar_cafe()
    tarjeta4.comprar_cafe()
    tarjeta4.comprar_cafe()
    tarjeta4.comprar_cafe()
    tarjeta4.comprar_cafe()  # tarjeta4 queda con 4 sellos
    print(f"Sellos de {tarjeta4.nombre_cliente} antes del regalo: {tarjeta4.get_sellos()}")
    tarjeta3.regalar_sello(tarjeta4)  # este regalo debería completar los 5 y dar café gratis
    print(f"Sellos de {tarjeta4.nombre_cliente} después: {tarjeta4.get_sellos()}")
    print(f"Cafés gratis de {tarjeta4.nombre_cliente}: {tarjeta4.get_cafes_gratis()}")
    print("-" * 100)

    tarjetavip1 = TarjetaCafeVIP("Hermenegildo Zegna", "CAF005VIP", "Oro")
    tarjetavip1.comprar_cafe()
    tarjetavip1.comprar_cafe()
    tarjetavip1.comprar_cafe()
    tarjetavip1.beneficio_vip()
main()