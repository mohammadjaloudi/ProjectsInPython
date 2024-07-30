class ToDoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task) -> None:
        if task in self.tasks:
            print("Task is already exist.")
            return None
        
        self.tasks.append(task)
        print("Task has been added successfully.")
        return None
    
    def finish_task(self, pos) -> None:
        if pos > len(self.tasks):
            print("Task doesn't exist.")
            print(f"There exist {len(self.tasks)} tasks")
            return None
        
        self.tasks.pop(pos - 1)
        print("Task done successfully! Good job :)")
        return None
    
    def view_tasks(self) -> None:
        if not self.tasks:
            print("No tasks exists :(")
            return None
        
        for number, task in enumerate(self.tasks, start=1):
            print(f"Task {number} is: {task}")
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
                    to_do_list.add_task(task)
                case 2:
                    task = input("Enter the number of the task that you've finished: ").title()
                    try:
                        task = int(task)
                        to_do_list.finish_task(task)
                    except ValueError:
                        print("Inalid number of a task!")
                case 3:
                    to_do_list.view_tasks()
                case 4:
                    print("Thanks for using our To Do List app, see you soon")
                    break
        except ValueError:
            print("Invalid input")

if __name__ == '__main__':
    main()
