from datetime import datetime

def add_appointment(book_date, book_time, doctor_name, check_mins):
    global bonus, doctors
    
    book_time_mins = int(book_time[:2]) * 60 + int(book_time[3:])
    
    try:
        appointment_datetime = datetime.strptime(f"{book_date} {book_time}", "%Y-%m-%d %H:%M")
        if appointment_datetime < datetime.now():
            print("Invalid book time, date/time is in the past")
            return False
    except ValueError:
        print("Invalid date or time format")
        return False
    
    if not (9 * 60 <= book_time_mins <= 17 * 60):
        print("Invalid book time, outside of working hours (09:00 to 17:00)")
        return False

    if book_date in doctors[doctor_name]:
        for existing_time, duration in doctors[doctor_name][book_date].items():
            existing_time_mins = int(existing_time[:2]) * 60 + int(existing_time[3:])
            if abs(existing_time_mins - book_time_mins) < duration:
                print("Invalid book time, overlapping with another appointment")
                return False
    
    if book_date not in doctors[doctor_name]:
        doctors[doctor_name][book_date] = {}
    
    doctors[doctor_name][book_date][book_time] = check_mins
    bonus[doctor_name] += 1
    print(f"Appointment booked with Dr. {doctor_name} on {book_date} at {book_time}")
    return True

def view_appointments():
    current_appointment = 1
    for name, values in doctors.items():
        for date, times in values.items():
            for time in times:
                print(f"Appointment {current_appointment}")
                print(f"Date: {date}")
                print(f"Time: {time}")
                print(f"Doctor: {name}")
                current_appointment += 1

bonus = {"Nicola": 0, "Ahmad": 0, "Ali": 0}
doctors = {"Nicola": {}, "Ahmad": {}, "Ali": {}}

while True:
    print("\nWelcome to our ultimate clinic")
    print("Choose an option:")
    print("1. Book an appointment")
    print("2. View appointments")
    print("3. Exit")
    
    option = input("Enter your option: ")
    try:
        option = int(option)
        match option:
            case 1:
                date = input("Enter the date of the book (YYYY-MM-DD): ")
                time = input("Enter the time of the book (HH:MM): ")
                name = int(input("Enter the name of the doctor (1 for Nicola, 2 for Ahmad, 3 for Ali): "))
                if name <= 0 or name > 3:
                    print("Invalid input")
                    continue
                doctor_name = {1: "Nicola", 2: "Ahmad", 3: "Ali"}[name]
                mins = 30
                add_appointment(date, time, doctor_name, mins)
            case 2:
                view_appointments()
            case 3:
                print("Thank you for your visit.")
                break
            case _:
                print("Invalid choice")
    except ValueError:
        print("Invalid input")

for name, client in bonus.items():
    if client > 0:
        print(f"{name} has {client} clients.")
