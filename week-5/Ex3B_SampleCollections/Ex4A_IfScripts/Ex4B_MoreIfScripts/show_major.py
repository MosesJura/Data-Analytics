# show_major.py

student_name = "Priya Sharma"
student_major = "CSCI"

match student_major:
    case "BIOL":
        major_name = "Biology"
        office = "Science Bldg, Room 310"
    case "CSCI":
        major_name = "Computer Science"
        office = "Sheppard Hall, Room 314"
    case "ENG":
        major_name = "English"
        office = "Kerr Hall, Room 201"
    case "HIST":
        major_name = "History"
        office = "Kerr Hall, Room 114"
    case "MKT":
        major_name = "Marketing"
        office = "Westly Hall, Room 310"
    case _:
        major_name = "Unknown"
        office = "Unknown — please contact advising"

print(f"{student_name}: {major_name}")
print(f"Department office: {office}")