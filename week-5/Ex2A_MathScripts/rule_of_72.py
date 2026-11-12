# Moses Jura
# 11/11/2026
## Rule of 72: years_to_double ≈ 72 / interest_rate_percent

Savings = 15000
IR = 0.1
Time = 72 / (IR * 100)
Double_Investment = Savings * 2

# Display results
print(f'Your current savings is ${Savings}.')
print(f'At a {IR * 100}% interest rate, your savings account will be')
print(f'worth ${Double_Investment:.2f} in {Time:.1f} years.')

print(f'With an initial investment of ${Savings} and an interest rate of {IR * 100}%,\
it will take approximately {Time:.1f} years for the investment to double \
to ${Double_Investment:.2f}.')


## Lab 3: - The input() function
bank_bal = float(input('25000.00'))  # Prompt user for bank balance
print('Your current bank balance is $' + str(bank_bal) + '.')
print(f'Your current bank balance is ${bank_bal:.2f}.')