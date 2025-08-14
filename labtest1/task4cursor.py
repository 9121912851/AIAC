# Program to read marks of three students and calculate their average

students = []

for i in range(3):
    name = input(f"Enter the name of student {i+1}: ")
    marks = []
    for j in range(3):
        mark = float(input(f"Enter mark {j+1} for {name}: "))
        marks.append(mark)
    total= sum(marks)
    average = sum(marks) / len(marks)
    students.append({'name': name, 'average': average})

print("\nAverages for each student:")
for student in students:
    print(f"{student['name']}: {student['average']:.2f}")