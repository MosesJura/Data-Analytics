# savings_goal.py

balance = 500
goal = 3000
weekly_savings = 250

while balance < goal:
    balance += weekly_savings

    if balance >= goal * 0.75:
        treat = 50
        balance -= treat
        print(f"So close! After treating myself, my balance is up to ${balance:.2f}")
    elif balance >= goal * 0.50:
        print(f"Almost there! This week my balance is up to ${balance:.2f}")
    else:
        print(f"This week my balance increased to ${balance:.2f}")

print(f"Goal met! My current balance is ${balance:.2f}")
