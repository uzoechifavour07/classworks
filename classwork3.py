#MINI PROJECT
#Transaction Analyzer
legit_transactions = []
valid_transaction = 0
transactions = [500000, -200000, 300000, -50000, 700000]

for transaction in transactions:
    if transaction < 0:
        continue    
    if transaction > 0:
        valid_transaction += 1

        print(f" we have {valid_transaction} valid transactions and it is {transaction} ")
        transaction = legit_transactions.append(transaction)
        sum_legit_transacion = sum(legit_transactions)
print(legit_transactions)
sum_legit_transacion = sum(legit_transactions)
print(sum_legit_transacion)