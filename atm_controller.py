from bank_system import bank
from cash_bin import cashbin

class ATMController:
    def insertCard(self):
        card_information = self.readCardInformation()
        if not bank.isValidCard(card_information):
            raise Exception('Invalid Card')

        pin_number = self.getPINnumber()
        if not bank.checkPINnumber(card_information, pin_number):
            raise Exception('Incorrect PIN Number')

        accounts = bank.getAccounts(card_information)
        return accounts

    def readCardInformation(self):
        return {'dummyCardInfo': '1234-4567-1234-1234'}
        
    def getPINnumber(self):
        pin_number = '1234'
        return pin_number

    def balance(self, account):
        balance = account.getBalance()
        return balance
    
    def deposit(self, account, dollar1, dollar10, dollar100):
        account.deposit(dollar1 + dollar10 * 10 + dollar100 * 100)
        cashbin.deposit(dollar1, dollar10, dollar100)

    def withdraw(self, account, dollar1, dollar10, dollar100):
        if not cashbin.withdraw(dollar1, dollar10, dollar100):
            raise Exception('Not enough dollars in cash bin')
        if not account.withdraw(dollar1 + dollar10 * 10 + dollar100 * 100):
            raise Exception('Not enough dollars in bank account')