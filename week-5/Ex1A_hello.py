print('Hello world!')

message = 'Hello world!'
print(message)

# "Hello world" prints twice because ...


# Displaying dollar and cents

dollar = 3
cents = .50

print(dollar + cents)

# Observation: the result is 3.5, NOT 3.50. 
# Python doesn't keep the trailing zero because .50 is just 0.5 as a float,
# and the default print format shows the shortest form of the number.

cents = cents + .25
print(dollar + cents)
# Now the result is 3.75 — same reason, no padding to two decimal places.

# Combining strings:
d_str = '3 dollars'
c_str = '50 cents'
print(d_str + " " + c_str)
# Output: 3 dollars 50 cents
# I inserted a space string " " between them to separate the two parts.

