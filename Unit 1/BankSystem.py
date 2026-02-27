class Bank: 
    def __init__(self, name, passwrd, address, balance):
        self.name = name
        self.password = passwrd
        self.address = address
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print('thanks for your deposit of $' + str(amount))

    def encryptionlayer(self):
        password = "123ABC"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print('thanks for your withdrawal of $' + str(amount))
        else:
            print("Insufficient funds")
        print('')

    def accessAccount(self, password):
        print('')

    def transfer(self):
        print('')


account_1 = Bank("John", "123ABC", "123 Main St", 100)
account_2 = Bank("Ashley", "456DEF", "456 Elm St", 200)
account_1.deposit(50)
account_1.withdraw(25)

def createAccount(name, password, address, balance):
    new_account = Bank(name, password, address, balance)
    return new_account

account_3 = createAccount("name, password, adress, balance")