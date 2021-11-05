from atm_controller import ATMController

atm = ATMController()
accounts = atm.insertCard()

sample_account = accounts[0]
atm.balance(sample_account)
atm.deposit(sample_account, dollar1=1, dollar10=10, dollar100=100)
atm.balance(sample_account)
atm.withdraw(sample_account, dollar1=1, dollar10=10, dollar100=100)
atm.balance(sample_account)
print('All Test Passed')
