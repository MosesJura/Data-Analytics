# Moses Jura
# 11/13/2026

# Description: This script tests various numeric
#              conversion techniques
# Author: Sam Q. Newprogrammer

# 2. Define variables (exactly as the workbook shows)
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# 3. a) Test each new variable as you go
#    b) Comment out lines that error, note the error type

# --- a: " 101.1 " (string with spaces + decimal) ---
# a_int = int(a)             # ValueError: invalid literal for int() (decimal)
a_float = float(a)           #  101.1  (float handles spaces + decimal)
a_int_from_float = int(float(a))  # 101  (truncates)

# --- b: '55' (clean integer string) ---
b_int = int(b)               # 55
b_float = float(b)           # 55.0

# --- c: "402 Stevens" (mixed text + number) ---
# c_int = int(c)             # ValueError: invalid literal for int()
# c_float = float(c)         # ValueError: could not convert string to float
c_slice = int(c[:3])         # 402  (slice numeric part, then cast)

# --- d: 'Number 5 ' (text then number) ---
# d_int = int(d)             # ValueError: invalid literal for int()
# d_float = float(d)         # ValueError: could not convert string to float
d_slice = int(d.strip()[-1]) # 5   (strip spaces, take last char, cast)

# 4. Print value + type for each variable
print(f"a = {a!r}  type: {type(a)}")
print(f"b = {b!r}  type: {type(b)}")
print(f"c = {c!r}  type: {type(c)}")
print(f"d = {d!r}  type: {type(d)}")

# 5. a) int() — which work?
#    a → ValueError (has decimal)
#    b → 55 
#    c → ValueError (has letters)
#    d → ValueError (has letters)

# 5. b) float() — which work?
#    a → 101.1 
#    b → 55.0 
#    c → ValueError
#    d → ValueError

# 5. c) int(float(a)) → 101  (two-step cast)
# 5. d) Slicing the numeric part:
#    c_slice = int(c[:3]) → 402
#    d_slice = int(d.strip()[-1]) → 5

# 5. e) .strip() to remove leading/trailing spaces
print(a.strip())   # '101.1'  (spaces gone)
print(d.strip())   # 'Number 5'  (trailing space gone)