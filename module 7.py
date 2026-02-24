# ==================================================
# TUPLE, SET, AND DICTIONARY PROGRAMS
# ==================================================

# -------------------------------
# 1. Month → Season (tuple)
# -------------------------------

def month_to_season():
    seasons = ("winter", "spring", "summer", "autumn")

    month = int(input("Enter month number (1–12): "))

    if month in (12, 1, 2):
        print("Season:", seasons[0])
    elif month in (3, 4, 5):
        print("Season:", seasons[1])
    elif month in (6, 7, 8):
        print("Season:", seasons[2])
    elif month in (9, 10, 11):
        print("Season:", seasons[3])
    else:
        print("Invalid month number")


# -------------------------------
# 2. Name storage (set)
# -------------------------------

def name_storage():
    names = set()

    while True:
        name = input("Enter a name (empty to quit): ")
        if name == "":
            break

        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)

    print("\nNames entered:")
    for name in names:
        print(name)


# -------------------------------
# 3. Airport data (dictionary)
# -------------------------------

def airport_data():
    airports = {}

    while True:
        print("\nChoose an option:")
        print("1. Enter new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Your choice: ")

        if choice == "1":
            icao = input("Enter ICAO code: ").upper()
            name = input("Enter airport name: ")
            airports[icao] = name
            print("Airport saved")

        elif choice == "2":
            icao = input("Enter ICAO code: ").upper()
            if icao in airports:
                print("Airport name:", airports[icao])
            else:
                print("Airport not found")

        elif choice == "3":
            break

        else:
            print("Invalid choice")


# ==================================================
# MAIN MENU
# ==================================================

while True:
    print("\n=== TUPLE, SET & DICTIONARY MENU ===")
    print("1. Month to season")
    print("2. Name storage using set")
    print("3. Airport data using dictionary")
    print("0. Exit")

    selection = input("Choose an option (0–3): ")

    if selection == "1":
        month_to_season()
    elif selection == "2":
        name_storage()
    elif selection == "3":
        airport_data()
    elif selection == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")