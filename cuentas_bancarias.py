class Cuenta:
    def __init__(self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo

    # agregar fondos a la cuenta
    def depositar(self, monto):
        self.saldo += monto

    # retirar fondos de la cuenta 
    # (solo si el saldo es suficiente para cubrir la cantidad solicitada)
    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            print("No es posible retirar fondos. Saldo insuficiente.")
            return False

    # obtener el saldo actual de la cuenta
    def obtener_saldo(self):
        return self.saldo

'''
Estas son las operaciones básicas aplicables a una cuenta bancaria. 
Dependiendo de los requisitos específicos del sistema, podrían agregarse más métodos
o atributos a la clase Cuenta. Por ejemplo, se podrían añadir métodos para calcular 
intereses, consultar el historial de transacciones, etc.
'''