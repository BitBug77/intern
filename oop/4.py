class BankAccount:
   def __init__(self, account_holder:str, balance: float = 0.0):
      self.account_holder = account_holder
      self.__balance = balance

   def deposit(self, amount:float):
      if amount > 0:
         self.__balance += amount
         print(f"Deposited{amount}. New balance: {self.__balance}")

      else:
          print("Deposit amount must be positive.")

   def withdraw(self, amount:float):
      if amount < 0 or amount >self.__balance:
          print("Invalid withdrawal amount.")
       
      else:
         self.__balance -= amount
         print(f"Withdrew {amount}. New balance: {self.__balance}")

   def get_balance(self, current_balance:float = 0.0):
      self.current_balance = self.__balance
      return self.current_balance

   def __str__(self):
      return f"Account Holder: {self.account_holder}, Balance: {self.__balance}"
   
class SavingAccounts(BankAccount):
   def __init__(self, account_holder:str, balance:float =0.0, interest_rate:float = 0.05):
    super().__init__(account_holder, balance)
    self.interest_rate = interest_rate

   def add_interest(self, interest_amount:float, current_balance:float = 0.0):
      interest_amount = current_balance * self.interest_rate
      current_balance += interest_amount
      print(f"Interest added: {interest_amount}. New balance: {current_balance}")

   def __str__(self):
      return f"interest rate: {self.interest_rate}, " 
   

acc1 = BankAccount("John Doe", 1000.0)
acc1.deposit(500)
acc1.withdraw(200)
print(acc1.__str__())

acc2 = SavingAccounts("Jane Doe", 2000.0, 0.03)
print(acc2.__str__())
print("Adding interest...",{acc2.add_interest(0.03, acc2.get_balance())})
