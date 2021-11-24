
class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self.set_balance(balance)

    def get_account_number(self):
        return self._account_number

    def get_account_name(self):
        return self._account_name

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            self._balance = 0
            print("Số dư không hợp lệ")    

    def display(self):
        print(f"BankAccount Info: {self.get_account_number()}, {self.get_account_name()}, {self.get_balance()}")

    def withdraw(self, amount):
        if 0 < amount < self._balance: 
            self._balance -= amount
        else:
            print ("Cash invalid")    

    def deposit(self, amount):
        if amount > 0: 
            self._balance += amount
        else:
            print ("Input Cash not acceptable")    


bank_account = BankAccount("VIB", "Ha Le", -40) 
bank_account.display() 

bank_account.deposit(8000000)
bank_account.display() 

bank_account.withdraw(4000000)
bank_account.display()