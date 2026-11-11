# Moses Jura
# 11/10/2026

# Ex2A_tips.py
# Lab1
# Calculate total due at a restaurant: food cost + tax + tip

# 1. Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# 2. Calculate the unknown
total_due = food_cost + tax + tip

# 3. Display results
print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
print("Tip is " + str(tip))
print("Total due is " + str(total_due))

# Q2a: Why str()? Because total_due is a FLOAT, and + cannot
# concatenate str + float. str() casts it to text so + works.
# print("The total due is " + str(total_due))

# Q5: New detailed output using f-strings
print(f"Food cost: ${food_cost}")
print(f"Tax: ${tax}")
print(f"Tip: ${tip}")
print(f"Total due: ${total_due}")

# Q7: Tip with two decimal places
# print("Tip is " + str(tip))      # OLD → shows 12.0
print(f"Tip is {tip:.2f}")         # NEW → shows 12.00


