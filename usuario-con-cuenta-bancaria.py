#EDUARDO POR FAVOR NO MODIFICAR ESTO 
#COPIARE Y PEGAR Y PROBAR EN OTRO CODIGO

class BankAccount:
    def __init__(self,interes=0.01,saldo = 100):
        self.balance=saldo
        self.yield_interest=interes
    
    def deposit(self,monto,cliente):
        self.balance+=monto
        print(f"Estimado {cliente} usted deposito  ${monto}")
        return self

    def withdraw(self, monto,cliente):
        if  self.balance > 0:
            self.balance-=monto
            print(f"Estimado {cliente} usted retiro ${monto}")
        else:
            self.balance-=5
            print(f"Esitmado {cliente} tiene fondos insuficientes: se cobra una tarifa de $ 5 por intento")
        return self
    
    def display_account_info(self,cliente):
        (print(f"Estimado {cliente} Su saldo es ${self.balance} "))
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

    def cambiar_tasa(self,interesNew,cliente):
        self.yield_interest=interesNew
        print(f"Estimado {cliente} su nuevo interes es {self.yield_interest}")
        return self

    def transferir_dinero(self,monto,otro_usuario,cliente):
        self.withdraw(monto,cliente)
        otro_usuario.account.deposit(monto,otro_usuario.name)
        print(f"Estimado {cliente} Usted transfirio ${monto} al cliente {otro_usuario.name}")
    
        return self



###################################################


class User():	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account=BankAccount(0.4,300)

    def make_deposit(self, amount):	
        cliente=self.name
        self.account.deposit(amount,cliente)
        return self


    def make_withdrawal (self, amount):
        cliente=self.name
        self.account.withdraw(amount,cliente)
        return self

    def display_user_balance (self):
        cliente=self.name
        self.account.display_account_info(cliente)
        return self

    def transfer_money(self,monto,otro_usuario):
        cliente=self.name
        self.account.transferir_dinero(monto,otro_usuario,cliente)
        return self

    def change_int(self,nueva_tasa):
        cliente=self.name
        self.account.cambiar_tasa(nueva_tasa,cliente)



#Crea una nueva instacia de la Clase llamada Eduardo
eduardo=User("Eduardo","grilli.eduardo@gmail.com")
jose=User("Jose","jewqeq@gmail.com")


#Podemos acceder desde User con el sel.account a nuestra clas BankAccount
eduardo.change_int(6)

eduardo.display_user_balance()
eduardo.make_withdrawal(200)
eduardo.make_deposit(600)
eduardo.display_user_balance()
jose.display_user_balance()
eduardo.transfer_money(300,jose)
eduardo.display_user_balance()
jose.display_user_balance()


#jose.display_user_balance()



