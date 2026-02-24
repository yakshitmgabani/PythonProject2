import random

while True:
    print("\n=== LISTS & FOR-LOOP PROGRAMS MENU ===")
    print("1. Roll dice and print the sum")
    print("2. Print five greatest numbers (descending)")
    print("3. Check if a number is prime")
    print("4. Enter and print five city names")
    print("0. Exit")

    choice = input("Choose a program (0–4): ")

    # 1. Dice rolling
    if choice == "1":
        dice_count = int(input("How many dice to roll? "))
        total = 0

        for _ in range(dice_count):
            roll = random.randint(1, 6)
            total += roll

        print("Sum of dice:", total)

    # 2. Five greatest numbers
    elif choice == "2":
        numbers = []

        while True:
            value = input("Enter a number (empty to quit): ")
            if value == "":
                break
            numbers.append(float(value))

        numbers.sort(reverse=True)

        print("Five greatest numbers:")
        for num in numbers[:5]:
            print(num)

    # 3. Prime number check
    elif choice == "3":
        number = int(input("Enter an integer: "))

        if number < 2:
            print(number, "is not a prime number")
        else:
            is_prime = True
            for i in range(2, number):
                if number % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(number, "is a prime number")
            else:
                print(number, "is not a prime number")

    # 4. City names list
    elif choice == "4":
        cities = []

        for i in range(5):
            city = input(f"Enter city {i + 1}: ")
            cities.append(city)

        print("\nCities entered:")
        for city in cities:
            print(city)

    # Exit
    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")