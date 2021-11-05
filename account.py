class Account:
    def __init__(self, balance):
        self.balance = balance

    def getBalance(self):
        print('Your Balance: ', self.balance)
        return self.balance
    
    def deposit(self, dollars):
        self.balance += dollars
        return True
    
    def withdraw(self, dollars):
        if self.balance < dollars:
            return False
        self.balance -= dollars
        return True