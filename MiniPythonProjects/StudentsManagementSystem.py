class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def __repr__(self):
        avg_grade = self.get_average_grade()
        return f"Student ID: {self.student_id}, Name: {self.name}, Average Grade: {avg_grade:.2f}"

    def __str__(self):
        avg_grade = self.get_average_grade()
        return f"Student ID: {self.student_id}, Name: {self.name}, Average Grade: {avg_grade:.2f}"


student_records = {}

def add_student(student_id, name):
    if student_id in student_records:
        print(f"Student with ID: {student_id} already exists.")
        return
    student_records[student_id] = Student(student_id, name)
    print(f"Student with ID: {student_id} has been added successfully.")

def remove_student(student_id):
    if student_id not in student_records:
        print(f"Student with ID: {student_id} doesn't exist.")
        return
    del student_records[student_id]
    print(f"Student with ID: {student_id} has been deleted successfully.")

def add_or_update_grade(student_id, subject, grade):
    if student_id not in student_records:
        print(f"Student with ID: {student_id} doesn't exist.")
        return
    student_records[student_id].add_grade(subject, grade)
    print("Grade added/updated successfully!")

def get_student_info(student_id):
    if student_id not in student_records:
        print(f"Student with ID: {student_id} doesn't exist.")
        return
    print(student_records[student_id])

def print_all_students():
    if not student_records:
        print("No students! :(")
        return
    for student in student_records.values():
        print(student)

def main():
    while True:
        print("\nWelcome to the Student Management System")
        print("1. Add a new student")
        print("2. Remove an existing student")
        print("3. Add or update a grade for a student")
        print("4. Get the average grade for a student")
        print("5. Print all student information")
        print("6. Exit")
        
        option = input("Choose an option: ")
        try:
            option = int(option)
            match option:
                case 1:
                    student_id = input("Enter student ID: ")
                    name = input("Enter student name: ")
                    if not name.isalpha() or name == '' or student_id == '':
                        print("Invalid input")
                    else:
                        name = name.title()
                        add_student(student_id, name)
                case 2:
                    student_id = input("Enter student ID: ")
                    if student_id == '':
                        print("Invalid input")
                    else:
                        remove_student(student_id)
                case 3:
                    student_id = input("Enter student ID: ")
                    subject = input("Enter subject: ")
                    grade = input("Enter grade: ")
                    try:
                        grade = int(grade)
                        subject = subject.title()
                        if student_id == '' or subject == '':
                            print("Invalid input")
                        elif not (0 <= grade <= 100):
                            print("Onvalid grade!")
                        else:
                            add_or_update_grade(student_id, subject, grade)
                    except ValueError:
                        print("Invalid grade input!")
                case 4:
                    student_id = input("Enter student ID: ")
                    if student_id == '':
                        print("Invalid input")
                    else:
                        get_student_info(student_id)
                case 5:
                    print_all_students()
                case 6:
                    print("Thanks for using our humble system :)")
                    break
                case _:
                    print("Invalid choice! Please follow the instructions!")
        except ValueError:
            print("Invalid input")

if __name__ == '__main__':
    main()
