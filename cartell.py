# cartel.py
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "CartellDB.txt")

# יצירת הקובץ אם לא קיים
if not os.path.exists(DB_PATH):
    with open(DB_PATH, "w") as f:
        f.write("")

def main():
    attempts = 0
    while True:
        print("\n--- Cartell System ---")
        print("1: Show all cars in database")
        print("2: Find a car by car number")
        print("3: Add new car")
        print("exit")
        choice = input("type option: ").strip()

        if choice == "1":
            get_vehicles()
        elif choice == "2":
            vehicle_id = input("Enter car number: ").strip()
            get_vehicle_by_id(vehicle_id)
        elif choice == "3":
            add_vehicle()
        elif choice.lower() == "EXIT":
  #          print("סיום המערכת. להתראות!")
            break
        else:
            attempts += 1
            print(f"option not exsist! ({attempts}/5)")
            if attempts >= 5:
                print("5 ilegal attempts - exits of the system.")
                break

def get_vehicles():
    print("\n--- list of viechals ---")
    header = "{:<10} {:<15} {:<10} {:<10} {:<12} {:<20}".format(
        "car number", "company", "color", "year ", "KM", " date added")
    print(header)
    print("-" * len(header))
    try:
        with open(DB_PATH, "r") as f:
            lines = f.readlines()
            if not lines:
                print("No viechals in DB.")
                return
            for line in lines:
                parts = line.strip().split(", ")
                print("{:<10} {:<15} {:<10} {:<10} {:<12} {:<20}".format(
                    parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]
                ))
    except FileNotFoundError:
        print("Couldnt find file.")

def get_vehicle_by_id(vehicle_id):
    if not vehicle_id.isdigit():
        print("Error: you must enter a number.")
        return
    found = False
    with open(DB_PATH, "r") as f:
        for line in f:
            parts = line.strip().split(", ")
            if parts[0] == vehicle_id:
                print("\n---  Car details ---")
                print("{:<15}: {}".format("Car number", parts[0]))
                print("{:<15}: {}".format("Company", parts[1]))
                print("{:<15}: {}".format("Color", parts[2]))
                print("{:<15}: {}".format("Year", parts[3]))
                print("{:<15}: {}".format("KM'", parts[4]))
                print("{:<15}: {}".format("Date added", parts[5]))
                found = True
                break
    if not found:
        print("Didnt find car number in DB.")

def add_vehicle():
    while True:
        vehicle_id = input("Car number: ").strip()
        if not vehicle_id.isdigit():
            print("Error: you must enter a number.")
            continue

        # בדיקה אם הרכב כבר קיים
        exists = False
        with open(DB_PATH, "r") as f:
            for line in f:
                if line.startswith(vehicle_id + ","):
                    exists = True
                    break
        if exists:
            print("Error: Car number already exsist.")
            continue

        company = input("Company: ").strip()
        color = input("Color: ").strip()
        year = input(" Year: ").strip()
        if not year.isdigit():
            print("Error: Yeat must be a number.")
            continue
        mileage = input("KM': ").strip()
        if not mileage.isdigit():
            print("Error: KM must be a number.")
            continue

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(DB_PATH, "a") as f:
            f.write(f"{vehicle_id}, {company}, {color}, {year}, {mileage}, {timestamp}\n")
        print("Car added successfully!")

        cont = input("Add another car? (yes/no): ").strip().lower()
        if cont != "yes":
            break

if __name__ == "__main__":
    main()
