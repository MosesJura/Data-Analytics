# if_basics.py

x = 100
y = 20

# 3a
if x / y == 5:
    print("x divided by y is 5")
    x = 1
else:
    print("are the variables set up correctly?")
# x becomes 1

# 3b
if x * y == y:
    print("now x times y is y")
    x = 10
else:
    print("Whoops, x equals " + str(x))
# x = 1, so 1*20 = 20 = y → True → x becomes 10

# 3c
if x < y:
    print("x is less than y")
    x = x * 2
else:
    print("uh oh, x is not less than y")
# x = 10, y = 20 → 10 < 20 True → x becomes 20

# 3d
if x > y:
    print("how is x greater than y?")
else:
    print("x is NOT greater than y")
# x = 20, y = 20 → 20 > 20 False → else branch

# 3e
print(f"The final value of x is {x} and the final value of y is {y}")
# Final: x = 20, y = 20