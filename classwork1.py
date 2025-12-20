balance = 5000
topup = int(input("how much you you want to deposit ? "))
current = balance + topup
print(f"your current balance is {current}")
remove_balance = int(input("how much do you want to withdraw"))
current = current - remove_balance
print(f"your current balance is {current}. ")