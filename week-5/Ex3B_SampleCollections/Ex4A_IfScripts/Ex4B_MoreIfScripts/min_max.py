# min_max.py

a = 42
b = 17
c = 99

# Smallest
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Largest
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"Smallest: {smallest}")
print(f"Largest: {largest}")