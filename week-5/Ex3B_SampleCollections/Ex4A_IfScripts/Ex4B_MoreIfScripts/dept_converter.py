# dept_converter.py

dept_code = 18

if dept_code == 1:
    print("Marketing")
elif dept_code == 5:
    print("Human Resources")
elif dept_code == 10:
    print("Accounting")
elif dept_code == 12:
    print("Legal")
elif dept_code == 18:
    print("IT")
elif dept_code == 20:
    print("Customer Relations")
else:
    print("Unknown department code")
print()
print()
print()
               # dept_converter_v2.py — using match/case


# dept_converter_v2.py

dept_code = 18

match dept_code:
    case 1:
        print("Marketing")
    case 5:
        print("Human Resources")
    case 10:
        print("Accounting")
    case 12:
        print("Legal")
    case 18:
        print("IT")
    case 20:
        print("Customer Relations")
    case _:
        print("Unknown department code")
                  