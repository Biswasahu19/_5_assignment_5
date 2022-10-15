class Account:
   
    title = 0
    balance = 0

    def __init__(self, title, balance):
        self.title = title
        self.balance = balance 
        
class Saving_Account(Account):
    def __init__(self, title, balance, interest_rate):
        super().__init__(title, balance)
        self.interest_rate = interest_rate

account_obj = Account ("Ashish", 5000)
Saving_Account_obj = Saving_Account ("Ashish", 5000, 5)
print(Saving_Account_obj.title)
print(Saving_Account_obj.balance)
print(Saving_Account_obj.interest_rate)