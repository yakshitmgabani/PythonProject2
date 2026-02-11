# ----------------------------------------
# WHILE LOOP ASSIGNMENT
# ----------------------------------------

# Example 1: Fixed amount of repetitions
print("Example 1: Fixed number of greetings")

rounds = int(input("How many greetings: "))
finished_rounds = 0

while finished_rounds < rounds:
    print("Good morning")
    finished_rounds = finished_rounds + 1

print("----------------------------------------")


# Example 2: User ends the repetition
print("Example 2: User controlled loop")

command = input("Enter command: ")

while command != "stop":
    print("Executing command:", command)
    command = input("Enter command: ")

print("Execution stopped.")
print("----------------------------------------")


# Example 3: Dice rolling simulation
print("Example 3: Dice rolling until double six")

import random

dice1 = 0
dice2 = 0
rolls = 0

while dice1 != 6 or dice2 != 6:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    rolls = rolls + 1

print("Rolled", rolls, "times.")
print("----------------------------------------")


# Example 4: Nested while loops (multiplication table)
print("Example 4: Multiplication table (1 to 5)")

first = 1
while first <= 5:
    second = 1
    while second <= 5:
        print(f"{first} times {second} is {first * second}")
        second = second + 1
    first = first + 1

print("----------------------------------------")


# Example 5: Using break statement
print("Example 5: break statement")

command = input("Enter command: ")

while command != "stop":
    if command == "MAYDAY":
        break
    print("Executing command:", command)
    command = input("Enter command: ")

print("Execution stopped.")
print("----------------------------------------")


# Example 6: while / else
print("Example 6: while / else")

command = input("Enter command: ")

while command != "stop":
    if command == "MAYDAY":
        break
    print("Executing command:", command)
    command = input("Enter command: ")
else:
    print("Goodbye.")

print("Execution stopped.")
print("----------------------------------------")


# Example 7: Corrected infinite loop example
print("Example 7: Avoiding infinite loop")

number = 1
while number < 5:
    print(number)
    number = number + 1

print("All ready.")
