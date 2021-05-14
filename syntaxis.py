#Esto es una clase
class User:
    
    pass    

#Esto es una instancia de una Clase

michael = User()
anna = User()


# declara una clase y dale el nombre User, le estamos dando todos los valores por defecto a esta clase.
class User:		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0


eduardo=User() #Instanciamos nuevos usuarios 
print(eduardo.name)
eduardo.name="eduardo" #Cambiamos el valor por defecto que era Michael por Matias
print(eduardo.name)


#Pasamos los atributos con argumentos ,a traves del def init

class User:		
    def __init__(self,user_name,email_address):
        self.name = user_name
        self.email = email_address
        self.account_balance = 0


eduardo=User("Eduardo","grilli.eduardo@gmail.com")

print(eduardo.name)
print(eduardo.email)

#Metodos!!!!!!!!!!!!!!!!!!!!!!


class User:		# aqui está lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # agrega el método deposit 
    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
        self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido

    def make_withdrawal (self, amount):
        self.account_balance-=amount

    def display_user_balance (self):
        return (f"Su saldo es de {self.account_balance}")


eduardo=User("Eduardo","grilli.eduardo.cl")
matias=User("Matias","matias@temuco.cl")

eduardo.make_deposit(1000)
eduardo.make_withdrawal(500)
matias.make_deposit(25)
matias.make_withdrawal(24)


print(f"Usuario = {eduardo.name} Correo = {eduardo.email} {eduardo.display_user_balance()}")
print(f"Usuario = {matias.name} Correo = {matias.email}  {matias.display_user_balance()}")



