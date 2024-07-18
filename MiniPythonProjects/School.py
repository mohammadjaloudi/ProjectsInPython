from statistics import mean

students = {}

def add_student(student_id, name, age):
    if student_id not in students:
        students[student_id] = {"name": name, "age": age, "grades": {}}
    else:
        print(f"Student with ID {student_id} already exists.")

def update_grades(student_id, subject, grade):
    if student_id in students:
        students[student_id]["grades"][subject] = grade
    else:
        print(f"Student with ID {student_id} doesn't exist.")

def calculate_average_grade(student_id):
    if student_id in students:
        grades = students[student_id]["grades"].values()
        if grades:
            return mean(grades)
        else:
            print(f"No grades exist for student with ID {student_id}")
            return None
    else:
        print(f"Student with ID {student_id} doesn't exist.")
        return None

def display_student_info(student_id):
    if student_id in students:
        print(f"Name: {students[student_id]['name']}, Age: {students[student_id]['age']}")
        print("Grades:")
        for subject, grade in students[student_id]['grades'].items():
            print(f" - {subject}: {grade}")
        avg = calculate_average_grade(student_id)
        if avg is not None:
            print(f"Average Grade: {avg:.2f}")
    else:
        print(f"Student with ID {student_id} doesn't exist.")

while True:
    print("Welcome to NEW school.")
    print("Follow the instructions:")
    print("1. Add a student")
    print("2. Update grades for a student")
    print("3. Calculate average grade for a student")
    print("4. Display a student info")
    print("5. Exit")
    
    option = input("Enter your option: ")
    try:
        option = int(option)
        match option:
            case 1:
                id = input("Enter Student's ID: ")
                name = input("Enter Student's name: ")
                age = input("Enter Student's age: ")
                add_student(id, name, age)
            case 2:
                id = input("Enter Student's ID: ")
                subject = input("Enter subject's name: ")
                grade = input("Enter subject's grade: ")
                update_grades(id, subject, grade)
            case 3:
                id = input("Enter Student's ID: ")
                calculate_average_grade(id)
            case 4:
                id = input("Enter Student's ID: ")
                display_student_info(id)
            case _:
                print("Invlid choice")
    except ValueError:
        print("Invalid input, please follow the instructions!")
