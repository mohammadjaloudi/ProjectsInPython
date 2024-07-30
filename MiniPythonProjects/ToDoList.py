class ToDoList:
    def __init__(self):
        self.tasks = {}
    
    def add_task(self, task, time) -> None:
        if task in self.tasks:
            print("Task already exists.")
            return None
        
        try:
            th, tm = time.split(":")
            task_mins = int(th) * 60 + int(tm)
        except ValueError:
            print("Invalid time format. Please use HH:MM format.")
            return None
        
        for _, time_d in self.tasks.items():
            th, tm = time_d.split(":")
            curr_mins = int(th) * 60 + int(tm)
            if curr_mins <= task_mins <= curr_mins + 60:
                print("Time is unavailable")
                return None
        
        self.tasks[task] = time
        print("Task has been added successfully.")
        return None
    
    def finish_task(self, task_name) -> None:
        if task_name not in self.tasks:
            print("Task doesn't exist.")
            print("You can display the tasks if you want to know what are the available")
            return None
        
        del self.tasks[task_name]
        print("Task done successfully! Good job :)")
        return None
    
    def view_tasks(self) -> None:
        if not self.tasks:
            print("No tasks exist :(")
            return None
        
        for number, (task, time) in enumerate(self.tasks.items(), start=1):
            print(f"Task {number} is: {task} on time {time}")
        return None

def main():
    to_do_list = ToDoList()
    while True:
        print("Welcome to our To Do List app")
        print("Here are the options we offer in our special To Do List app, please choose an option: ")
        print("1. Add Task")
        print("2. Finish task")
        print("3. View tasks")
        print("4. Exit")
        
        option = input("Enter your option: ")
        try:
            option = int(option)
            match option:
                case 1:
                    task = input("Enter the task that you want to add: ").title()
                    time = input("Enter the time of the task (HH:MM): ")
                    to_do_list.add_task(task, time)
                case 2:
                    task_number = input("Enter the number of the task that you've finished: ")
                    try:
                        task_number = int(task_number)
                        task = list(to_do_list.tasks.keys())[task_number - 1]
                        to_do_list.finish_task(task)
                    except (ValueError, IndexError):
                        print("Invalid task number!")
                case 3:
                    to_do_list.view_tasks()
                case 4:
                    print("Thanks for using our To Do List app, see you soon")
                    break
        except ValueError:
            print("Invalid input")

if __name__ == '__main__':
    main()
