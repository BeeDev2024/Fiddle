import datetime
import csv

def get_calories_from_csv(food_item, calorie_file='calories_in_food.csv'):
    try:
        with open(calorie_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].strip().lower() == food_item.strip().lower():
                    return int(row[1])
    except FileNotFoundError:
        print(f"Error: The file {calorie_file} does not exist.")
    return None
start = "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_"
print(start)
print("  -_-_-_-_-_-_ FIDDLE _-_-_-_-_-_-")
print(start)
while True:
    print("""
(1) Enter calorie amount of foods
(2) Enter daily intake
(3) Monthly calories
(4) Exit""")
    inputs = input("=> ").lower()  
    if "1" in inputs:
        all_data = []
        while True:
            print("Type 'Exit' to leave.")
            food = input("Enter food name: ")
            if food.lower() == "exit":
                break
            calories = input("Enter number of calories: ")
            if calories.lower() == "exit":
                break
            try:
                calories = int(calories)
            except ValueError:
                print("Please enter a valid number for calories.")
                continue
            all_data.append([food, calories])
        with open('calories_in_food.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(all_data)
    elif "2" in inputs:
        current_date = datetime.datetime.now()
        formatted_date = current_date.strftime("%m.%Y")
        all_data = []
        while True:
            print("If you have entered this food into the calories_in_food.csv before, please use the same format.")
            print("Type 'Exit' to leave.")
            food = input("Enter food eaten: ")
            if food.lower() == "exit":
                break
            time = input("Enter time and date eaten (please maintain identical formatting): ")
            if time.lower() == "exit":
                break
            calories = get_calories_from_csv(food)
            if calories is None:
                print(f"Calorie information for '{food}' not found. Please enter calories manually.")
                calories = input("Enter calories for the food: ")
            else:
                print(f"Calories for '{food}': {calories}")
            all_data.append([food, time, calories])
        with open(f'calories_monthly({formatted_date}).csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(all_data)
    elif "3" in inputs:
        current_date = datetime.datetime.now()
        formatted_date = current_date.strftime("%m.%Y")
        with open(f'calories_monthly({formatted_date}).csv', mode ='r')as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                print(lines)
    elif "4" in inputs:
        print("Exiting the program.")
        exit()
    else:
        print("Invalid option, please try again.")
