#EDUARDO POR FAVOR NO MODIFICAR ESTO 
#COPIARE Y PEGAR Y PROBAR EN OTRO CODIGO

class BankAccount:
    def __init__(self,interes=0.01,saldo = 100):
        self.balance=saldo
        self.yield_interest=interes
    
    def deposit(self,monto,cliente,banco):
        self.balance+=monto
        print(f"Estimado {cliente} usted deposito  ${monto} al Banco {banco}")
        return self

    def withdraw(self, monto,cliente,banco):
        if  self.balance > 0:
            self.balance-=monto
            print(f"Estimado {cliente} usted retiro ${monto} del Banco {banco} ")
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

    def transferir_dinero(self,monto,otro_usuario,cliente,banco):
        self.withdraw(monto,cliente,banco)
        otro_usuario.account[banco].deposit(monto,otro_usuario.name,banco)
        print(f"Estimado {cliente} Usted transfirio desde el Banco {banco} un monto de ${monto} al cliente {otro_usuario.name}")
    
        return self



###################################################


class User():	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account={'Santander':BankAccount(0.4,300),'Itau':BankAccount(0.2,10000)}

    def make_deposit(self, amount,banco):	
        cliente=self.name
        self.account[banco].deposit(amount,cliente,banco)
        return self


    def make_withdrawal (self, amount,banco):
        cliente=self.name
        self.account[banco].withdraw(amount,cliente,banco)
        return self

    def display_user_balance (self,banco):
        cliente=self.name
        self.account[banco].display_account_info(cliente,banco)
        return self

    def transfer_money(self,monto,otro_usuario,banco):
        cliente=self.name
        self.account[banco].transferir_dinero(monto,otro_usuario,cliente,banco)
        return self

    def change_int(self,nueva_tasa,banco):
        cliente=self.name
        self.account[banco].cambiar_tasa(nueva_tasa,cliente,banco)



#Crea una nueva instacia de la Clase llamada Eduardo
eduardo=User("Eduardo","grilli.eduardo@gmail.com")
jose=User("Jose","jewqeq@gmail.com")


#Podemos acceder desde User con el sel.account a nuestra clas BankAccount
#eduardo.display_user_balance('Santander')
#eduardo.display_user_balance('Itau')
#eduardo.make_deposit(200,'Itau')


#eduardo.make_withdrawal(200,'Santander')
#eduardo.make_deposit(600,'Santander')
#eduardo.display_user_balance('Santander')
#jose.display_user_balance('Santander').display_user_balance('Itau')
eduardo.transfer_money(300,jose,'Itau')
eduardo.display_user_balance('Santander').display_user_balance('Itau')
jose.display_user_balance('Santander').display_user_balance('Itau')




