'''name = "favour"
def welcome_message(name):
    print(f"hello, {name}")
welcome_message(name)
welcome_message("daniel")
welcome_message("david")
welcome_message("yesmi")'''


'''balance = 7000
amount = 6000
def add_balance(balance, amount):
    new_balance = balance + amount
    print(new_balance)
add_balance(balance, amount)'''

'''balance = 7000
amount = 6000
def withdraw(balance, amount):
    return balance - amount

new_balance = withdraw(balance, amount)
print(new_balance)'''

'''balance = 7000
amount = 8000
def withdraw(balance, amount):
    if amount > balance:
        return "insuffient funds"
    else:
        return balance - amount
new_balance = withdraw(balance, amount)
print(new_balance)'''

'''balances = [2000, 9000, -8000, -20000, 800000]

def audit_accounts(balances):
    for bal in balances:
        if bal < 0:
            print("fraud detected")
        elif bal > 0:
            print("legit account")
audit_accounts(balances)'''

# exercise 5 loan checker
'''neg_history_list = []
pos_history_list =[]
num = 0
accounthistorybal =[1000, 4000, 70000, -90000, 10000, -3000, 7200, -9000, 2900]

def checkneg_bal():
    negative_bal = 0
    positive_bal = 0
    for accountbal in accounthistorybal:
        if accountbal < 0:
            negative_bal += 1
            print(neg_history_list)
            accountbal = neg_history_list.append(accountbal)
        elif negative_bal >= 3:
             print("loan denied")
        elif accountbal > 0:
            positive_bal += 1
            print(pos_history_list)
            accountbal = pos_history_list.append(accountbal)
            if positive_bal >= 6:
         
                print("loan accepted")
            else:
                print("loan pending")

checkneg_bal()'''
valid_accounts_list = []
#account auidtor
accounts = [5000, -200, 300, 8000]
def check_valid_account():
    global positive_counter
    positive_counter = 0
    for account in accounts:
        if account > 0:
            positive_counter += 1
            account = valid_accounts_list.append(account)
            print(f"here is the summary of the valid accounts {valid_accounts_list}") 
        elif account < 0:
            print("invalid account")
check_valid_account()
print(f"we have {positive_counter} account")