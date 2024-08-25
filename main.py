students = [("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 85), ("Eve", 78), ("Frank", 85), ("Mark", 50), ("George", 21)]

grades = {grades for name, grades in students}

print (grades)

names = {name for name, grades in students}

print(names)


sorted_grades=sorted(grades, reverse=True)
print(sorted_grades)

top_performers = sorted_grades[:3]
print(top_performers)

def failed_students ():
    for name, grade in students:
        if grade < 51:
            print(f"{name}, {grade}")
print("Failed Students:")
failed_students()