class BankAccount:
    def __init__(self,interes=0.01,saldo = 0):
        self.account_balance=saldo
        self.yield_interest=interes
    
    def deposit(self,monto):
        self.account_balance+=monto
        print(f'Usted deposito {monto}')
        return self

    def withdraw(self, monto):
        if  self.account_balance > 0:
            self.account_balance-=monto
            print(f'Usted retiro {monto}')
        else:
            self.account_balance-=5
            print("Fondos insuficientes: se cobra una tarifa de $ 5 por intento")
        return self
    
    def display_account_info(self):
        (print(f'Su saldo es ${self.account_balance}'))
        return self

    def interes_cuenta(self):
        if self.account_balance>0:
            interesGenerado=(self.account_balance*self.yield_interest)
            self.account_balance+=interesGenerado
            print(f'Se genero ${interesGenerado} de interes y su nuevo saldo es ${self.account_balance}')
        else:
            print(f"No se generro interes debido a que su saldo es negativo y corresponde a ${self.account_balance}")
        return self

    def interes_actual(self):
        (print(f'Su interes acutal es  {self.yield_interest}'))
        return self


eduardo=BankAccount(0.4,5)
eduardo.display_account_info().deposit(200).interes_cuenta().withdraw(8).interes_cuenta().display_account_info().withdraw(400).withdraw(5).display_account_info().interes_cuenta()




