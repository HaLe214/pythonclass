class BankAccount:

   def __init__(self,account_number, Customer,balance=0):
        self.account_number = account_number
        self.account_name = Customer
        self.set_balance=balance

   @property
   def get_account_number(self):
       return self.account_number

   @property
   def get_account_name(self):
       return self.account_name
   @property
   def get_account_balance(self):
       return self.balance
   @get_account_balance.setter
   def set_balance(self,balance):
       if balance>=0:
           self.balance=balance
       else:
           print("amount must not be zero")
   def withdraw(self,amount):
       if amount>0 and amount<self.get_account_balance:
           self.set_balance=self.get_account_balance-amount
       else:
           print("invalid amount")
   def deposit(self,amount):
       if amount>0:
           self.set_balance=self.get_account_balance+amount
       else:
           print("invalid amount")
   def display(self):
       print(f'account_number: {self.get_account_number}')
       self.account_name.get_info()
       print(f'account_balance: {self.get_account_balance}')
class SavingAccount (BankAccount):
    def monthly_interest_rate(self):
        self.monthly_interest_rate = 0.005
        return  super.get_account_balance*self.monthly_interest_rate
class Customer :
    def __init__(self,name, date_of_birth, email, phone):
        self.name=name
        self.date_of_birth= date_of_birth
        self.email=email
        self.phone=phone
    def get_info(self):
        print(f'họ tên: {self.name}, ngày sinh: {self.date_of_birth}, email: {self.email}, phone: {self.phone}')




cus= Customer("hale","08-04-1988","ha.le2@onemount.com","0973798488")
bl=BankAccount("987",cus,8)
bl.display()
