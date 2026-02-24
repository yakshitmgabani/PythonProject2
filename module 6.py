import random
import math

# --------------------------------------------------
# 1 & 2. Dice rolling functions
# --------------------------------------------------

def roll_dice(sides=6):
    return random.randint(1, sides)


# --------------------------------------------------
# 3. Gallons to liters
# --------------------------------------------------

def gallons_to_liters(gallons):
    return gallons * 3.785


# --------------------------------------------------
# 4. Sum of list
# --------------------------------------------------

def sum_list(numbers):
    return sum(numbers)


# --------------------------------------------------
# 5. Remove uneven numbers
# --------------------------------------------------

def remove_uneven(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


# --------------------------------------------------
# 6. Pizza unit price
# --------------------------------------------------

def pizza_unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100
    area = math.pi * radius_m ** 2
    return price_eur / area


# ==================================================
# MAIN PROGRAM MENU
# ==================================================

while True:
    print("\n=== FUNCTIONS MENU ===")
    print("1. Roll a 6-sided dice until 6")
    print("2. Roll an N-sided dice until max value")
    print("3. Convert gallons to liters")
    print("4. Sum numbers in a list")
    print("5. Remove uneven numbers from list")
    print("6. Compare pizza value")
    print("0. Exit")

    choice = input("Choose an option (0–6): ")

    # 1. Roll 6-sided dice until 6
    if choice == "1":
        result = 0
        while result != 6:
            result = roll_dice()
            print(result)

    # 2. Roll N-sided dice until max value
    elif choice == "2":
        sides = int(input("Enter number of sides: "))
        result = 0
        while result != sides:
            result = roll_dice(sides)
            print(result)

    # 3. Gallons to liters
    elif choice == "3":
        while True:
            gallons = float(input("Enter gallons (negative to quit): "))
            if gallons < 0:
                break
            liters = gallons_to_liters(gallons)
            print(f"{liters:.2f} liters")

    # 4. Sum list
    elif choice == "4":
        numbers = [1, 2, 3, 4, 5]
        total = sum_list(numbers)
        print("List:", numbers)
        print("Sum:", total)

    # 5. Remove uneven numbers
    elif choice == "5":
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        even_numbers = remove_uneven(numbers)
        print("Original list:", numbers)
        print("Even numbers:", even_numbers)

    # 6. Pizza value comparison
    elif choice == "6":
        d1 = float(input("Enter diameter of pizza 1 (cm): "))
        p1 = float(input("Enter price of pizza 1 (€): "))
        d2 = float(input("Enter diameter of pizza 2 (cm): "))
        p2 = float(input("Enter price of pizza 2 (€): "))

        unit1 = pizza_unit_price(d1, p1)
        unit2 = pizza_unit_price(d2, p2)

        if unit1 < unit2:
            print("Pizza 1 is better value")
        else:
            print("Pizza 2 is better value")

    # Exit
    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")