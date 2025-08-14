import csv

# Read the CSV file
students = []
with open('LAB Test 1/task4.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header
    for row in reader:
        if row and row[0].strip():  # skip empty lines
            students.append({
                'name': row[0].strip(),
                'marks': [int(row[1]), int(row[2]), int(row[3])]
            })

# Take input from user to calculate total and average for each student
for student in students:
    print(f"\nStudent: {student['name']}")
    # Optionally, allow user to override marks
    choice = input("Do you want to enter marks manually for this student? (y/n): ").strip().lower()
    if choice == 'y':
        marks = []
        for i in range(1, 4):
            mark = int(input(f"Enter marks for subject {i}: "))
            marks.append(mark)
        student['marks'] = marks
    total = sum(student['marks'])
    average = total / 3
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")