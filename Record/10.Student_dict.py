
def find_grade(total_mark):
    if total_mark >= 90:
        return 'A'
    elif total_mark >= 82:
        return 'B'
    elif total_mark >= 75:
        return 'C'
    elif total_mark >= 60:
        return 'D'
    elif total_mark >= 50:
        return 'P'
    else:
        return 'F'
    

student1 = {
    "name": "Nihal",
    "roll_number": 37,
    "register_number": "19857",
    "department": "Computer Applications",
    "semester": 1
}
student1["total_mark"] = int(input("Enter The Total Marks"))
student1["grade"] = find_grade(student1["total_mark"])
print(student1)

del student1["roll_number"]
print(student1)
