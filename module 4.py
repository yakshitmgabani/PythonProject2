import random

while True:
    print("\n=== WHILE LOOP PROGRAMS MENU ===")
    print("1. Print numbers divisible by 3 (1–1000)")
    print("2. Inches to centimeters converter")
    print("3. Find smallest and largest number")
    print("4. Number guessing game")
    print("5. Username and password login")
    print("6. Approximate value of pi (Monte Carlo)")
    print("0. Exit")

    choice = input("Choose a program (0–6): ")

    # 1. Divisible by 3
    if choice == "1":
        number = 1
        while number <= 1000:
            if number % 3 == 0:
                print(number)
            number += 1

    # 2. Inches to centimeters
    elif choice == "2":
        while True:
            inches = float(input("Enter inches (negative to quit): "))
            if inches < 0:
                break
            print(inches * 2.54, "cm")

    # 3. Smallest and largest number
    elif choice == "3":
        numbers = []
        while True:
            value = input("Enter a number (empty to quit): ")
            if value == "":
                break
            numbers.append(float(value))

        if numbers:
            print("Smallest:", min(numbers))
            print("Largest:", max(numbers))
        else:
            print("No numbers entered.")

    # 4. Guessing game
    elif choice == "4":
        secret = random.randint(1, 10)
        while True:
            guess = int(input("Guess a number (1–10): "))
            if guess < secret:
                print("Too low")
            elif guess > secret:
                print("Too high")
            else:
                print("Correct!")
                break

    # 5. Login system
    elif choice == "5":
        correct_username = "python"
        correct_password = "rules"
        attempts = 0

        while attempts < 5:
            username = input("Username: ")
            password = input("Password: ")

            if username == correct_username and password == correct_password:
                print("Welcome")
                break
            else:
                print("Incorrect credentials")
                attempts += 1

        if attempts == 5:
            print("Access denied")

    # 6. Pi approximation
    elif choice == "6":
        N = int(input("How many random points? "))
        inside_circle = 0
        count = 0

        while count < N:
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x**2 + y**2 < 1:
                inside_circle += 1
            count += 1

        pi_approx = 4 * inside_circle / N
        print("Approximation of pi:", pi_approx)

    # Exit
    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")