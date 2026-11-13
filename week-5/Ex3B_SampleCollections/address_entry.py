# address_entry.py

# 1. Dictionary with sample values
contact_info = {
    "name": "Bilbo Baggins",
    "address": "123 Bag End Lane",
    "city": "Hobbiton",
    "state": "The Shire",
    "zip": "12345"
}

# 2. Print formatted address using a multi-line f-string (triple quotes)
#    — no separate print statements per line.
print(f"""
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")

# 3. Remove the 'name' key
contact_info.pop("name")

# 4. New full_name dictionary
full_name = {
    "first name": "Bilbo",
    "last name": "Baggins"
}

# 5. Add an honorific
full_name.update({"honorific": "Mr."})

# 6. Merge full_name into contact_info
contact_info.update(full_name)

# 7. Print the formatted address again, now including the name
print(f"""
{contact_info['honorific']} {contact_info['first name']} {contact_info['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")