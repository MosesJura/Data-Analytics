# complex_taxes.py

# --- Inputs ---
pay_rate = 25.50
hours_worked = 45
filing_status = 'joint'

# --- Compute weekly gross (reuse pay_rules logic) ---
if hours_worked <= 40:
    weekly_gross = pay_rate * hours_worked
else:
    weekly_gross = (pay_rate * 40) + ((hours_worked - 40) * pay_rate * 1.5)

# --- Estimate annual gross ---
annual_gross = weekly_gross * 52

# --- Determine tax rate based on filing status ---
if filing_status == 'single':
    if annual_gross < 12000:
        tax_rate = 0.05
    elif annual_gross < 25000:
        tax_rate = 0.10
    elif annual_gross < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
else:  # joint
    if annual_gross < 12000:
        tax_rate = 0.00
    elif annual_gross < 25000:
        tax_rate = 0.06
    elif annual_gross < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

# --- Weekly withholding ---
weekly_tax = weekly_gross * tax_rate

# --- Output ---
print(f"You worked {hours_worked} hours this period.")
print(f"Weekly gross: ${weekly_gross:,.2f}")
print(f"Estimated annual gross: ${annual_gross:,.2f}")
print(f"Filing status: {filing_status}")
print(f"Tax rate: {tax_rate:.0%}")
print(f"Weekly tax withheld: ${weekly_tax:,.2f}")