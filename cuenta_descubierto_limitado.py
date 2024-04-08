'''
Ahora, al inicializar una cuenta, podemos especificar un límite de descubierto opcional.
En el método retirar, verificamos si el saldo más el límite de descubierto es suficiente
para cubrir el monto solicitado. Si es así, permitimos la retirada incluso si el saldo
real es insuficiente. Esta implementación permite a los clientes realizar retiros incluso
si su saldo actual es insuficiente, hasta el límite de descubierto autorizado.
'''

class Cuenta:
    def __init__(self, numero_cuenta, titular, saldo, limite_descubierto=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo
        self.limite_descubierto = limite_descubierto

    def depositar(self, monto):
        self.saldo += monto

    # Ahora se comprueba si el saldo es suficiente o si el saldo mas el limite descubierto
    # lo es. Si es así, se podrá retirar la cantidad solicitada.
    def retirar(self, monto):
        if self.saldo >= monto or self.saldo + self.limite_descubierto >= monto:
            self.saldo -= monto
            return True
        else:
            print("No es posible retirar fondos. Saldo insuficiente.")
            return False

    def obtener_saldo(self):
        return self.saldo
