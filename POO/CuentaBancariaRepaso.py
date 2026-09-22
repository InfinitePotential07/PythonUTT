class CuentaBancaria():
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
    print("-" * 200)
main()

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
            print(f"Recarga de ${monto} realizada con exito.")
            
    def pagar_viaje(self):
        if self.tarifa_viaje <= self.__saldo:
            self.__saldo -= self.tarifa_viaje
            print(f"El pago de ${self.tarifa_viaje} se ha realizado con exito \nSu saldo actual es de ${self.__saldo} \nFeliz viaje!")
        else:
            print("Fondos insuficientes. \nRealize una recarga.")
        
def main():
    user1 = TarjetaMetro("124223", "Ulises Lopez", 25.0, 15.0)
    print(f"El saldo de {user1.usuario} es de ${user1.get_saldo()}")
    user1.recargar(30)
    print(f"El saldo de {user1.usuario} es de ${user1.get_saldo()}")
    user1.pagar_viaje()
    print(f"El saldo de {user1.usuario} es de ${user1.get_saldo()}")
    print("-" * 50)
    
    user2 = TarjetaMetro("454223", "Kim De la torre", 100.0, 16.0)
    print(f"El saldo de {user2.usuario} es de ${user2.get_saldo()}")
    user2.recargar(26.0)
    print(f"El saldo de {user2.usuario} es de ${user2.get_saldo()}")
    user2.pagar_viaje()
    print(f"El saldo de {user2.usuario} es de ${user2.get_saldo()}")
main()