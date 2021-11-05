from atm_controller import ATMController

atm = ATMController()
account = atm.insertCard()

atm.balance(account)
atm.deposit(atm, dollar1=1, dollar10=10, dollar100=100)
atm.withdraw(atm, dollar1=1, dollar10=10, dollar100=100)
