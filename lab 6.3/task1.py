class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.roll_no = rollno
        self.marks = marks
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")
    def calculate_grade(self):
        if self.marks <= 100 and self.marks >= 90:
            return 'A'
        elif self.marks <= 89 and self.marks >= 75:
            return 'B'
        elif self.marks <= 74 and self.marks >= 60:
            return 'C'
        else:
            return 'Fail'
name= input("Enter student's name: ")
rollno = input("Enter student's roll number: ")
marks = float(input("Enter student's marks: "))
students= Student(name, rollno, marks)
students.display_details()