# pay_rules.py
# Gross pay: overtime (>40 hrs) paid at 1.5× rate

pay_rate = 17.30
hours_worked = 45

if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked
else:
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

print(f"Pay Rate: ${pay_rate:.2f}")
print(f"Hours Worked: {hours_worked}")
print(f"Gross Pay: ${gross_pay:.2f}")