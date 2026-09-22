"""class CuentaBancaria():
    def __init__(self, titular, num_cuenta, saldo, tasa_interes):
        self.titular = titular
        self.num_cuenta = num_cuenta
        self.__saldo = saldo
        self.tasa_interes = tasa_interes
        
    def get_saldo(self):
        return self.__saldo
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Deposito por ${monto} realizado con exito")
            print(f"Saldo actual: ${self.__saldo}")
        else:
            print("Error: monto no valido, debe ser positivo")
            
    def retirar(self, monto):
        if monto < self.__saldo:
            self.__saldo -= monto
            print(f"El retiro de ${monto} fue existoso")
            print(f"Saldo actual: ${self.__saldo}")
        
        
def main():
    cuenta1 = CuentaBancaria("Ulises Lopez", "0325109794", 15000.0, 0.04)
    print(f"Saldo: ${cuenta1.get_saldo()}")
    cuenta1.depositar(670.0)
    print(f"Saldo: ${cuenta1.get_saldo()}")
    cuenta1.retirar(670.0)
    print(f"Saldo: ${cuenta1.get_saldo()}")
main()"""

class TarjetaMetro():
    def __init__(self, codigo_tarjeta, usuario, saldo, tarifa_viaje):
        self.codigo_tarjeta = codigo_tarjeta
        self.usuario = usuario
        self.__saldo = saldo
        self.tarifa_viaje = tarifa_viaje
        
    def get_saldo(self):
        return self.__saldo
    
    def recargar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print("f Recarga de ${monto} realizada con exito.")
            print("f Saldo actual ${self.__saldo}")
            
    def pagar_viaje(self):
        if self.__saldo >= TarjetaMetro.tarifa_viaje:
            self.__saldo -= TarjetaMetro.tarifa_viaje
            print("f Pago realizado con exito por ${TarjetaMetro.tarifa_viaje}")
        
def main():
    user1 = TarjetaMetro("124223", "Ulises Lopez", 25.0, 15.0)
    user1.tarifa_viaje()
    print("f Saldo {user1.get_saldo()}")
main()