# bonus_gregorian_calendar.py

year = 2000

if year % 400 == 0:
    print(f"{year} IS a leap year.")
elif year % 100 == 0:
    print(f"{year} is NOT a leap year.")
elif year % 4 == 0:
    print(f"{year} IS a leap year.")
else:
    print(f"{year} is NOT a leap year.")