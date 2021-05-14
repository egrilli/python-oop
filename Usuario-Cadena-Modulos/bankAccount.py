class BankAccount:
    def __init__(self,interes=0.01,saldo = 100):
        self.balance=saldo
        self.yield_interest=interes
    
    def deposit(self,monto,cliente,banco):
        self.balance+=monto
        print(f"Estimado {cliente} usted deposito  ${monto} al Banco {banco}")
        return self

    def withdraw(self, monto,cliente):
        if  self.balance > 0:
            self.balance-=monto
            print(f"Estimado {cliente} usted retiro ${monto}")
        else:
            self.balance-=5
            print(f"Esitmado {cliente} tiene fondos insuficientes: se cobra una tarifa de $ 5 por intento")
        return self
    
    def display_account_info(self,cliente,banco):
        (print(f"Estimado {cliente} Su saldo es ${self.balance} en el Banco {banco} "))
        return self

    def interes_cuenta(self,cliente):
        if self.balance>0:
            interesGenerado=(self.balance*self.yield_interest)
            self.balance+=interesGenerado
            print(f"Estimado {cliente}, Se genero ${interesGenerado} de interes y su nuevo saldo es ${self.balance}")
        else:
            print(f"Estimado {cliente}, no se generro interes debido a que su saldo es negativo y corresponde a ${self.balance}")
        return self

    def interes_actual(self,cliente):
        (print(f"Estimado {cliente} Su interes actual es  {self.yield_interest}"))
        return self

    def cambiar_tasa(self,interesNew,cliente,banco):
        self.yield_interest=interesNew
        print(f"Estimado {cliente} su nuevo interes es {self.yield_interest}% en el Banco {banco}")
        return self

    def transferir_dinero(self,monto,otro_usuario,cliente):
        self.withdraw(monto,cliente)
        otro_usuario.account.deposit(monto,otro_usuario.name)
        print(f"Estimado {cliente} Usted transfirio ${monto} al cliente {otro_usuario.name}")
    
        return self