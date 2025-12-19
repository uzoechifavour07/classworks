'''name = input("what is your name?")
balance = input("what is your account balance ?")

print (f" hi my name is {name}, and i have {balance} in my wallet address")
'''


def addtobalance ():
       account_balance = 5000
       topup = int(input("how huch do you want to deposit ? "))
       global current
       current= account_balance + topup
       
       print(f"your account balance is {current}")

addtobalance()


def subbalance():
       
       amount = int(input("how much do you wan to withdraw ? "))
       balance = current - amount

       print(f"your currrent balance is {balance}")

subbalance()
    