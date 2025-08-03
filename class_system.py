import csv
import os

class Student:
    def __init__(self, name, roll_no, student_class):
        self.name = name
        self.roll_no = roll_no
        self.student_class = student_class
        self.marks = {} 
    def add_marks(self, subject, score):
        self.marks[subject] = score
        print(f"Marks added for {subject}: {score}")

    def total_marks(self):
        return sum(self.marks.values())

    def percentage(self):
        if self.marks:
            return self.total_marks() / len(self.marks)
        return 0

    def display_details(self):
        print("\n--- Student Report ---")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Class: {self.student_class}")
        print("Marks:")
        for subject, score in self.marks.items():
            print(f"  {subject}: {score}")
        print(f"Total: {self.total_marks()}")
        print(f"Percentage: {self.percentage():.2f}%")

students = {}

def load_students():
    if not os.path.exists("students.csv"):
        return
    with open("students.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            roll_no = row["roll_no"]
            name = row["name"]
            student_class = row["class"]
            subject = row["subject"]
            marks = float(row["marks"])

            if roll_no not in students:
                students[roll_no] = Student(name, roll_no, student_class)
            students[roll_no].marks[subject] = marks

def save_students():
    with open("students.csv", "w", newline="") as f:
        fieldnames = ["roll_no", "name", "class", "subject", "marks"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for roll_no, student in students.items():
            for subject, score in student.marks.items():
                writer.writerow({
                    "roll_no": roll_no,
                    "name": student.name,
                    "class": student.student_class,
                    "subject": subject,
                    "marks": score
                })


load_students()


while True:
    print("\nStudent Management System (CSV)")
    print("1. Add Student")
    print("2. Add/Update Marks")
    print("3. View Student Report")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == '1':
        roll_no = input("Enter roll number: ")
        if roll_no in students:
            print("Student already exists.")
        else:
            name = input("Enter name: ")
            student_class = input("Enter class: ")
            students[roll_no] = Student(name, roll_no, student_class)
            save_students()
            print(f"Student {name} added.")

    elif choice == '2':
        roll_no = input("Enter roll number: ")
        if roll_no in students:
            student = students[roll_no]
            subject = input("Enter subject: ")
            try:
                marks = float(input("Enter marks: "))
                student.add_marks(subject, marks)
                save_students()
            except ValueError:
                print("Invalid marks.")
        else:
            print("Student not found.")

    elif choice == '3':
        roll_no = input("Enter roll number: ")
        if roll_no in students:
            students[roll_no].display_details()
        else:
            print("Student not found.")

    elif choice == '4':
        print("Exiting. Data saved to students.csv.")
        break

    else:
        print("Invalid option.")
