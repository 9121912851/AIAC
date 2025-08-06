class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

# Taking input for 'n' number of students
n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    name = input("Name: ")
    roll_no = input("Roll No: ")
    marks = float(input("Marks: "))
    students.append(Student(name, roll_no, marks))

print("\nStudent Details:")
for student in students:
    student.display_details()
    print("-" *20)