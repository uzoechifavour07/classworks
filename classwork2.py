# ATM LOGIN SYSTEM

pin = 1234
name = "favour"
balance = 1000000
limit_transfer = 100000
min_balance = 1000
dfa_code = 5678


print ("welcome to favy atm machine")

user_pin = int(input("what is your card pin ? "))

if user_pin == pin :
    print(f"welcome the favybank {name}")
    print(f"your current balance is {balance}")
    sub_1 = int(input("how much do you wanna withdraw ?"))
    if balance - sub_1 >= limit_transfer :
        print("you need a 2fa")
        dfa_input = int(input("check you device and input the unique code.....?"))
        if dfa_input == dfa_code:
            print("transaction loading...........")
            c_balance = balance - sub_1
            print(f"your current balance is {c_balance}..... transaction sucessfull")
        else:
            print("account blocked")
    elif balance - sub_1 <= min_balance  :
        print("you need to add money to you account this poor boy")
        
elif user_pin != pin:
    print("please try again")
    user_pin = int(input("what is your card pin ? "))

    if user_pin == pin :
        print(f"welcome the favybank {name}")
        print(f"your current balance is {balance}")
        sub_1 = int(input("how much do you wanna withdraw ?"))
        if balance - sub_1 >= limit_transfer :
            print("you need a 2fa")
            dfa_input = int(input("check you device and input the unique code.....?"))
            if dfa_input == dfa_code:
                print("transaction loading...........")
                c_balance = balance - sub_1
                print(f"your current balance is {c_balance}..... transaction sucessfull")
            else:
                print("account blocked")
        elif balance - sub_1 <= min_balance  :
            print("you need to add money to you account this poor boy")
        
