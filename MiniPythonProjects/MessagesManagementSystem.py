import datetime

class Message:
    def __init__(self):
        self.messages = []
    
    def add(self, message):
        time = datetime.datetime.now().replace(microsecond=0)
        self.messages.append((message, time))
        print("Message sent successfully")
    
    def rem(self, message, time=None):
        for msg, tme in self.messages:
            if msg == message and (time is None or time == tme):
                self.messages.remove((msg, tme))
                print("Message deleted successfully")
                return
        print("Can't find the message")
    
    def display(self):
        if not self.messages:
            print("No messages are in the archive :(")
            return 
        
        for msg, time in self.messages:
            print(f"Message: {msg} on: {time}")

socialApp = Message()
while True:
    print("\nWelcome to our message management system")
    print("Enter your choice: ")
    print("1. Send a message")
    print("2. Delete a message")
    print("3. Display messages")
    print("4. Exit")
    
    option = input("Enter your option: ")
    try:
        option = int(option)
        match option:
            case 1:
                message = input("Enter your message: ")
                socialApp.add(message)
            case 2:
                message = input("Enter the message you want to remove: ")
                timeornot = input("Do you want to specify a time? (y/n): ").strip().lower()
                time = None
                if timeornot == 'y':
                    time_str = input("Enter the time (YYYY-MM-DD HH:MM:SS): ")
                    try:
                        time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        print("Invalid time format. Please try again.")
                        continue
                socialApp.rem(message, time)
            case 3:
                socialApp.display()
            case 4:
                print("Thanks for using our social media app")
                break
            case _:
                print("Invalid choice")
    except ValueError:
        print("Invalid input")
