class InsufficientInventoryError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Purchase:
    def __init__(self):
        self.inventory = {
            "Laptop": 12,
            "Mouse": 50,
            "Keyboard": 30,
            "Monitor": 20
        }
        self.items = {
            "Laptop": 25000,
            "Mouse": 500,
            "Keyboard": 1200,
            "Monitor": 8500   
        }
        self.selected_items = {}
    
    def purchase(self, name, quantity):
        if quantity < 0:
            raise InsufficientInventoryError("Quantity must be a positive integer.")
        if quantity > self.inventory[name]:
            raise InsufficientInventoryError("Invalid item quantity. Please choose from the available quantities.")
        
        if name in self.selected_items:
            self.selected_items[name] += quantity
        else:
            self.selected_items[name] = quantity
        
        self.inventory[name] -= quantity

    def total_cost(self):
        if not self.selected_items:
            return 0
        total = 0
        for name, quantity in self.selected_items.items():
            total += quantity * self.items[name]
        
        return total

buy = Purchase()

print("Here are our available items with their prices: ")
for name, quantity in buy.inventory.items():
    print(f"{name}: {buy.items[name]} EGP (Available: {quantity})")

while True:
    item = input("Enter the item you wish to purchase (or type 'done' to finish selection): ").strip().title()
    if item == 'Done':
        break
    if item not in buy.inventory.keys():
        print("Invalid item name. Please choose from the available items.")
        continue
    
    try:
        quantity = int(input(f"Enter the quantity for {item}: "))
    except ValueError:
        print("Please enter a valid integer for quantity.")
        continue

    try:
        buy.purchase(item, quantity)
    except InsufficientInventoryError as e:
        print(e)

print(f"Total cost of your purchase: {buy.total_cost()} EGP")
