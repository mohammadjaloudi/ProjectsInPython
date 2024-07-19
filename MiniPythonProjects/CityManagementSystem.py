from math import inf
from statistics import mean

cities = {}

def add_city(city_name, population):
    if city_name not in cities:
        cities[city_name] = population
        print(f"{city_name} added successfully")
    else:
        print("City already exists.")

def update_population(city_name, new_population):
    if city_name in cities:
        cities[city_name] = new_population
    else:
        print("City doesn't exist.")

def find_cities():
    if not cities:
        print("No cities available.")
        return
    
    max_city_name, min_city_name = "", ""
    max_pop, min_pop = -inf, inf
    for name, population in cities.items():
        if population < min_pop:
            min_pop = population
            min_city_name = name
        if population > max_pop:
            max_pop = population
            max_city_name = name
    
    print(f"City with highest population: {max_city_name}")
    print(f"City with lowest population: {min_city_name}")

def avg_population():
    if not cities:
        print("No cities available.")
        return None
    return mean(cities.values())

while True:
    print("\nWelcome to City Population Data")
    print("Please choose an option:")
    print("1. For adding a city")
    print("2. Update population for a city")
    print("3. To find cities with highest and lowest population")
    print("4. To calculate the average population among all cities")
    print("5. Exit")
    
    option = input("Enter your option: ")
    
    try:
        option = int(option)
        match option:
            case 1:
                city_name = input("Enter the name of the city: ")
                city_name = city_name.title()
                population = input("Enter the population of the city: ")
                try:
                    population = int(population)
                    if population < 0:
                        print(f"Seriously? {population} popele are in the city?")
                        continue
                    add_city(city_name, population)
                except ValueError:
                    print("Please enter a valid number of people!")
            case 2:
                city_name = input("Enter the city you want to update its population: ")
                city_name = city_name.title()
                population = input("Enter the updated population of the city: ")
                try:
                    population = int(population)
                    if population < 0:
                        print(f"Seriously? {population} popele are in the city?")
                        continue
                    update_population(city_name, population)
                except ValueError:
                    print("Please enter a valid number of people!")
            case 3:
                find_cities()
            case 4:
                avg = avg_population()
                if avg is not None:
                    print(f"Average population: {avg:.2f}")
            case 5:
                print("Thanks for using our system! See you soon.")
                break
            case _:
                print("Invalid choice, please follow the instructions.")
    except ValueError:
        print("Invalid input! Please follow the instructions.")
