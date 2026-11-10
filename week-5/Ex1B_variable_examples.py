# Ex1B_variable_examples.py

# Variables with good names + sample values

customer_id = 1001  # Customer ID
customer_name = 'Moses Jura'  # Customer's name
customer_gender = 'Male' # Customer gender
customer_date_of_birth = '1999-10-10'  # Customer date of birth
driver_license_number = 'D12345678'  # Driver’s license number
auto_policy_number = 'APN-1234567'  # Auto policy number

# Assumptions/notes about types and representation:
# customer_id = 1001  -> int. But maybe it should be a string if IDs can have letters/leading zeros.
# customer_name = 'Moses Jura' -> str. Could split into first/last name for sorting/filtering.
# customer_gender = 'Male'  -> str. Maybe use a fixed set of options for consistency. e.g male or female
# customer_dob = '1999-10-10'  -> str. Could use datetime.date for date math.
# drivers_license_number = 'D12345678'  -> str. Must be string (letters + numbers).
# auto_policy_number = 'APN-1234567'  -> str. IDs with dashes/letters need strings.


# My own name, and birth/growing-up city and state:
my_name = 'Moses Jura'
birth_city = 'Charlotte'
birth_state = 'North Carolina'

# ---- Reserved words questions (from flexiple.com) ----

# a) Full list of reserved words that can't be used for variable names:
# False, None, True, and, as, assert, async, await, break, class, continue,
# def, del, elif, else, except, finally, for, from, global, if, import, in,
# is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

# b) 5 reserved words and what they mean:
# 1) if: starts a conditional block; runs code only when a condition is true.
# 2) for: begins a loop that iterates over each item in an iterable (list, range, string).
# 3) while: repeats a block of code as long as a condition remains true.
# 4) def: defines a function (a reusable named block of code).
# 5) class: defines a class, a blueprint for creating objects with attributes and methods.
