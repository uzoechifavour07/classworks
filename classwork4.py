#MINI PROJECT
'''
Docstring for classwork4
Functions:
● check_balance()
● deposit()
● withdraw()
● login()
Use:
● conditions
● loops
● returns
'''


login_pin = 1234
balance = 5000
chances = 0
user_pin = int(input("what is your pin? "))

if user_pin == login_pin:
    print("welcome to favybank ")

    while user_pin == login_pin :
        def checkbalance(balance):
            print(f"your current balance is {balance} naira")
        checkbalance(balance)

        amount = int(input("how much do you wanna deposit ?"))

        def deposit(balance, amount):
            if amount < 0:
                return "invalid amount"
            elif amount > 0 :
                return balance + amount
            
        balance = deposit(balance, amount)
        print(f"your current balance is {balance} naira")

        amount = int(input("how much do you wanna withdraw ?"))
        def withdraw(balance, amount):
            if amount < 0:
                return "invalid amount"
            elif amount > 0 :
                return balance - amount
            
        balance = withdraw(balance, amount)
        print(f"your current balance is {balance} naira")
        break
elif user_pin != login_pin:
    print("lets try again you have two more chance")
    while chances < 2:
        user_pin = int(input("what is your pin? "))
        if chances == 2 and user_pin != login_pin:
            print("this is your last chance if pin wrong you atm card will be stuck in the machine")
        if user_pin != login_pin and chances < 2 :
            print("lets try again")
            chances += 1
        elif user_pin == login_pin:
            print("welcome to favybank ")
            