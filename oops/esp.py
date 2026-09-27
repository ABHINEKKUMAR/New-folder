# class BankAccount:

#      def __init__(self,name ,balance):
#         self.name =name 
#         self.balance =balance

#        def show_balance(self):
#         print("balance:",self.balance) 

#        def deposit(self,amount):
#         self.balance =self.balance + amount

#        def withdraw(self,amount):
#         if amount<=self.show_balance
#         self.blance =self.balance - amount
#         else:
#         print("insufficient balance")

# account= BankAccount("Rahul",1000)            
# account.show_balance()

# account.deposit(1000)
# account.show_balance()

# account.withdraw(1000)
# account.show_balance()






class BankAccount:

    def __init__(self, name, balance):
        self.name = name  # Rahul
        self.balance = balance # access  private # 1000

    def show_balance(self):
        print("Balance:", self.balance)# these self.balance call # 1000

    def deposit(self, amount):
        self.balance = self.balance + amount # call balance +amount _>1000+1000=2000

    def withdraw(self, amount): # 2000
        if amount <= self.balance: #2000
            self.balance = self.balance - amount # 2000-amount
        else:
            print("Insufficient balance")


account = BankAccount("Rahul", 1000)

account.show_balance()

account.deposit(0)
account.show_balance()

account.withdraw(2000)
account.show_balance()
