from cash_bin import cashbin
from account import Account

class BankSystem:
    def isValidCard(self, card_information):
        # TODO: 올바른 카드 확인
        return True
    def checkPINnumber(self, card_information, pin_number):
        # TODO: 올바른 비밀번호 확인
        return True

    def getAccounts(self, card_information):
        return [Account(balance=1010), Account(balance=100)]

bank = BankSystem()