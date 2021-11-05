from cash_bin import cashbin

class BankSystem:
    def isValidCard(self, card_information):
        # TODO: 올바른 카드 확인
        return True
    def checkPINnumber(self, card_information, pin_number):
        # TODO: 올바른 비밀번호 확인
        return True

    def getAccounts(self, card_information):
        return [{'dummyAccount': 1234}, {'dummyAccount': 1234}, {'dummyAccount': 1234}]

    def balance(self, account):
        return 100000

    def deposit(self, account, dollars):
        return True
    
    def withdraw(self, account, dollars):
        # TODO: 계좌에 잔액이 있는지 확인
        return True

bank = BankSystem()