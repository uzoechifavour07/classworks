'''balance = -50
if balance > 0:
    print("account is active")
else:
    print("account is inactive")'''

'''password = 1234

userinput = int(input('what is your password ?'))

if userinput == 1234:
    print("Access granted ")
else:
    print("Access denied")'''

'''balance = 10000000
if balance >= 10000000:
    print("premium account")
else:
    print("basic account")'''

'''balance = 1000000
if balance >= 750000:
    print("approved")
elif balance >= 650000:
    print("review")
else:
    print("rejected")'''

'''balance = 400
card_active = True
if balance >= 1000 and card_active == True:
   print("withdrawl allowed")
else:
   print("transaction denied")'''

##### Excercise 6

balance = 10000
card_active = False
pin = 1234
user_pin = int(input("please enter your pin ?"))

if pin == user_pin:
    amount = int(input("how much do you want to withdraw ?"))
    total_cbalace1 = balance - amount

    if total_cbalace1 >= 1100:
        print ('you can withdraw')
    elif total_cbalace1 <= 0:
        print("sorry please top up")
    elif balance <= 1000 or balance <= 0:
        print ("sorry please top up")
elif pin != user_pin and card_active == True:
    print("let's try again")
    try_1_pin = int(input("what is your pin again ?"))
    if try_1_pin == pin:
        amount = int(input("how much do you want to withdraw ?"))
        total_cbalace1 = balance - amount
        if total_cbalace1 >= 1100:
            print ('you can withdraw')
        elif total_cbalace1 <= 0:
            print("sorry please top up")
        elif balance <= 1000 or balance <= 0:
            print ("sorry please top up") 
else:
    print("account blocked")





