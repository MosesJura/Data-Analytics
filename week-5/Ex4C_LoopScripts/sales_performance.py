# sales_performance.py

sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('Diego Alvarez', 'South', 6100.00),
    ('Aisha Okafor', 'East', 3980.75),
]

total_sales = 0

for name, region, amount in sales_data:
    print(f"{name} ({region}): ${amount:,.2f}")
    if amount > 5000:
        print("  ^ Top performer!")
    total_sales += amount

print(f"\nOverall total: ${total_sales:,.2f}")
