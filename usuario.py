class User:	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):	
        self.account_balance += amount	

    def make_withdrawal (self, amount):
        self.account_balance-=amount

    def display_user_balance (self):
        (print(f"{self.name} Su saldo es de {self.account_balance}"))

    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)

#Creo instancias de la clase Usuario
eduardo=User("Eduardo","grilli.eduardo.cl")
matias=User("Matias","matias@temuco.cl")
javier=User("Jasvier","j.temuco@gmail.com")

#Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo
eduardo.make_deposit(1000)
eduardo.make_deposit(500)
eduardo.make_deposit(600)
eduardo.make_withdrawal(600)
eduardo.display_user_balance()



#Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
matias.make_deposit(25)
matias.make_deposit(25)
matias.make_withdrawal(24)
matias.make_withdrawal(24)
matias.display_user_balance()

#Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
javier.make_deposit(700)
javier.make_withdrawal(300)
javier.make_withdrawal(300)
javier.make_withdrawal(50)
javier.display_user_balance()

#Agrega un método transfer_money; haga que el primer usuario transfiera dinero al tercer usuario y luego imprima los saldos de ambos usuarios
eduardo.transfer_money(matias,500)
eduardo.display_user_balance()
matias.display_user_balance()


