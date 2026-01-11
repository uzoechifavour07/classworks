'''balances  = [1000, 2500, 500, 8000]

for balance in balances:
    if balance >= 300000:
        print("loan approved")
    else:
        print("loan denied")'''
#Exerise 4
'''pin = 1234
pin_attempts = 0
user_pin = int(input("what is your atm pin ?"))

print("processing..............")
if pin == user_pin:
    print("lets withdraw")
elif pin_attempts < 3:
    print("pin incorrect")
    while pin_attempts < 3  :
        user_pin = int(input("what is your atm pin ?"))
        if pin_attempts ==2 and pin != user_pin:
            print("you have tried three times please wait for 30 sec......")       
        if user_pin != pin and pin_attempts < 2:
            print("try again")
        pin_attempts += 1'''

   

'''balances  = [1000, -1, 500, 8000]

for balance in balances :
    if balance < 0:
        break
    print(balance)'''

'''for balance in balances :
    if balance < 0:
        continue
    print(balance)'''

'''transctions = [9000, 6000, -1000, 700, -10000, 7000]


for transaction in transctions:
    if transaction < 0:
          continue
    print(f"your {transaction} transaction is valid")'''

'''accounts ={
            "001": 50000,
            "002": 2000,
            "003": 90000}
for acc, bal in accounts.items():
    print(acc, bal)'''

#Exercise 5
accounts ={
    "f001": 500000,
    "c001": 8000,
    "y001": 7000,
    "e001":  11000,
    "l001": 300000
}

for id, bal in accounts.items():
    if bal > 100000:
        print(f"{id} high value account")   
    elif bal < 100000:
        print(f"{id} low value account")   
    print(id, bal)
