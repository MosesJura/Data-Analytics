
# Ex3A_string_cleaning.py

# 2. Messy contact records
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

# 3. .lower()
print(name_1.lower())     # priya sharma
print(name_2.lower())     # bob nguyen
print(name_3.lower())     # latonya williams

# 4. .title()
print(name_1.title())     # Priya Sharma
print(name_2.title())     # Bob Nguyen
print(name_3.title())     # Latonya Williams

# 5. .replace() to remove $
salary_1_clean = salary_1.replace('$', '')
salary_2_clean = salary_2.replace('$', '')
print(salary_1_clean)     # 82,500  (still has a comma!)
print(type(salary_1_clean))  # <class 'str'>

# To do math on them, you must ALSO remove commas, then cast:
# int('82,500') → ValueError
# So chain: replace $ → replace , → int()

# 6. Chain .replace() + int() in ONE line
salary_1_int = int(salary_1.replace('$', '').replace(',', ''))
print(salary_1_int)       # 82500
print(type(salary_1_int)) # <class 'int'>