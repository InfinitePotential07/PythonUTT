class CuentaBancaria:
    def __init__(self, titular, numero_cuenta, saldo, tasa_interes):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.__saldo = saldo
        self.tasa_interes = tasa_interes

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso de ${monto}. Saldo actual: ${self.__saldo}")
        else:
            print(f"Error: El monto debe ser positivo.")

    def retirar(self, monto):
        if monto <= 0:
            print(f"Error: El monto a debe ser positivo.")
        elif monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso de ${monto}. Saldo actual: ${self.__saldo}")
        else:
            print(f"Error: Fondos insuficientes ${monto}. Saldo disponible: ${self.__saldo}")

    def calcular_interes(self):
        interes = self.__saldo * self.tasa_interes
        self.__saldo += interes
        print(f"Interés de ${interes} aplicado. Saldo actual: ${self.__saldo}")


    def transferir(self, cuenta_destino, monto):
        if monto <= 0:
            print("El monto debe ser positivo")
        elif monto<self.__saldo:
            self.retirar(monto)
            print(f"Tranferencia de ${monto} a la cuenta {cuenta_destino.numero_cuenta}")
            
            cuenta_destino.depositar(monto)
            print("Transferercia completa")
        else: 
            print("Transferencia cancelada")



def main():
    cuenta1 = CuentaBancaria("Luis Acosta", "0325109794", 1500.0, 0.05)
    cuenta2 = CuentaBancaria("Kim Lopez", "0325105534", 3000.0, 0.03)
    cuenta3 = CuentaBancaria("Ismael Haaz", "0325106642", 500.0, 0.04)

    print(f"Cuenta 1: {cuenta1.titular}")
    print(f"Número de cuenta: {cuenta1.numero_cuenta}")
    print(f"Saldo inicial: ${cuenta1.obtener_saldo()}")
    cuenta1.depositar(500.0)
    cuenta1.calcular_interes()
    print(f"Saldo final: ${cuenta1.obtener_saldo()}")
    print("-----------------------------------------")

    print(f"Cuenta 2: {cuenta2.titular}")
    print(f"Número de cuenta: {cuenta2.numero_cuenta}")
    print(f"Saldo inicial: ${cuenta2.obtener_saldo()}")
    cuenta2.retirar(1000.0)
    cuenta2.depositar(-200.0)
    print(f"Saldo final: ${cuenta2.obtener_saldo()}")
    print("-----------------------------------------")

    print(f"Cuenta 3: {cuenta3.titular}")
    print(f"Número de cuenta: {cuenta3.numero_cuenta}")
    print(f"Saldo inicial: ${cuenta3.obtener_saldo()}")
    cuenta3.retirar(800.0)
    cuenta3.calcular_interes()
    print(f"Saldo final: ${cuenta3.obtener_saldo()}")
    print("-----------------------------------------")

    print(f"Saldo actual de la cuenta 1 ${cuenta1.obtener_saldo()}")
    print(f"Saldo actual de la cuenta 2 ${cuenta2.obtener_saldo()}")
    cuenta1.transferir(cuenta2, 750.0)
    print(f"Saldo actual de la cuenta 1 ${cuenta1.obtener_saldo()}")
    print(f"Saldo actual de la cuenta 2 ${cuenta2.obtener_saldo()}")


main()