# ATM Problem Code: HS08TEST
# Add problem to Todo list
# Submit
# Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an attempted transaction.

# Input
# Positive integer 0 < X <= 2000 - the amount of cash which Pooja wishes to withdraw.

# Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's initial account balance.

# Output
# Output the account balance after the attempted transaction, given as a number with two digits of precision. If there is not enough money in the account to complete the transaction, output the current bank balance.

# Example - Successful Transaction
# Input:
# 30 120.00

# Output:
# 89.50
# Example - Incorrect Withdrawal Amount (not multiple of 5)
# Input:
# 42 120.00

# Output:
# 120.00
# Example - Insufficient Funds
# Input:
# 300 120.00

# Output:
# 120.00
def atmCalc(input):
    input_arr = input.split(' ')
    balance = float(input_arr[1])
    withdraw = float(input_arr[0])
    # check if number is nonnegative
    if withdraw < 0.00 or balance < 0.00:
        return 'nonnegative numbers are required'
    # check insufficient fund
    if withdraw > balance:
        return 'Insufficient funds'
    # Withdraw should be multiple of 5
    if withdraw%5 != 0:
        return 'Incorrect Withdrawal Amount (not multiple of 5)'
    # apply service fee
    withdraw = withdraw + 0.5
    balance = balance - withdraw
    return balance
input = '300 120.00'
print("Balance : {}".format(atmCalc(input)))