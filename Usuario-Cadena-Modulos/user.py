from bankAccount import BankAccount

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
eduardo.display_user_balance('Santander')
eduardo.display_user_balance('Itau')
eduardo.make_deposit(200,'Itau')


eduardo.make_withdrawal(200,'Itau')
eduardo.make_deposit(600,"Itau")
eduardo.display_user_balance()
jose.display_user_balance()
eduardo.transfer_money(300,jose)
eduardo.display_user_balance()
jose.display_user_balance()