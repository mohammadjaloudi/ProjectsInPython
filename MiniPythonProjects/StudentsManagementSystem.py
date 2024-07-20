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
    """Adds a new student to the student_records dictionary."""
    if student_id in student_records:
        print(f"A student with ID {student_id} already exists.")
        return
    student_records[student_id] = Student(student_id, name)
    print(f"Student with ID {student_id} has been successfully added.")

def remove_student(student_id):
    """Removes an existing student from the student_records dictionary."""
    if student_id not in student_records:
        print(f"No student found with ID {student_id}.")
        return
    del student_records[student_id]
    print(f"Student with ID {student_id} has been successfully removed.")

def add_or_update_grade(student_id, subject, grade):
    """Adds or updates a grade for a specific subject for an existing student."""
    if student_id not in student_records:
        print(f"No student found with ID {student_id}.")
        return
    student_records[student_id].add_grade(subject, grade)
    print("Grade has been successfully added/updated.")

def get_student_info(student_id):
    """Prints the information of a specific student."""
    if student_id not in student_records:
        print(f"No student found with ID {student_id}.")
        return
    print(student_records[student_id])

def print_all_students():
    """Prints the information of all students."""
    if not student_records:
        print("There are no students in the record.")
        return
    for student in student_records.values():
        print(student)

def main():
    """Main function to run the Student Management System."""
    while True:
        print("\nWelcome to the Student Management System")
        print("1. Add a new student")
        print("2. Remove an existing student")
        print("3. Add or update a grade for a student")
        print("4. Get the average grade for a student")
        print("5. Print all student information")
        print("6. Exit")
        
        option = input("Please choose an option: ")
        try:
            option = int(option)
            match option:
                case 1:
                    student_id = input("Enter student ID: ")
                    name = input("Enter student name: ")
                    if not name.isalpha() or not name or not student_id:
                        print("Invalid input. Please enter a valid student ID and name.")
                    else:
                        name = name.title()
                        add_student(student_id, name)
                case 2:
                    student_id = input("Enter student ID: ")
                    if not student_id:
                        print("Invalid input. Please enter a valid student ID.")
                    else:
                        remove_student(student_id)
                case 3:
                    student_id = input("Enter student ID: ")
                    subject = input("Enter subject: ")
                    grade = input("Enter grade: ")
                    if not student_id or not subject or not grade:
                        print("Invalid input. Please enter valid student ID, subject, and grade.")
                    else:
                        try:
                            grade = int(grade)
                            subject = subject.title()
                            if not (0 <= grade <= 100):
                                print("Invalid grade. Please enter a grade between 0 and 100.")
                            else:
                                add_or_update_grade(student_id, subject, grade)
                        except ValueError:
                            print("Invalid input. Please enter a numeric value for the grade.")
                case 4:
                    student_id = input("Enter student ID: ")
                    if not student_id:
                        print("Invalid input. Please enter a valid student ID.")
                    else:
                        get_student_info(student_id)
                case 5:
                    print_all_students()
                case 6:
                    print("Thank you for using the Student Management System. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please select a valid option from the menu.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")

if __name__ == '__main__':
    main()
