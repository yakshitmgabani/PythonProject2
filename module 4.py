"""
Loop Structure (while) – Assignment
Demonstrates:
1. Fixed repetitions
2. User-controlled repetition
3. Random repetition
4. Nested while loops
5. break statement
6. while/else
7. Infinite loop example (commented out)
"""

import random


# --------------------------------------------------
# Example 1: Fixed amount of repetitions
# --------------------------------------------------
print("EXAMPLE 1: Fixed number of repetitions")

rounds = int(input("How many greetings: "))
finished_rounds = 0

while finished_rounds < rounds:
    print("Good morning")
    finished_rounds += 1


# --------------------------------------------------
# Example 2: User ends the repetition
# --------------------------------------------------
print("\nEXAMPLE 2: User-controlled repetition")

command = input("Enter command: ")
while command != "stop":
    print("Executing command:", command)
    command = input("Enter command: ")

print("Execution stopped.")


# --------------------------------------------------
# Example 3: Varying amount of repetitions (dice)
# --------------------------------------------------
print("\nEXAMPLE 3: Dice rolling simulation")

dice1 = 0
dice2 = 0
rolls = 0

while dice1 != 6 or dice2 != 6:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    rolls += 1

print(f"Rolled {rolls} times to get double sixes.")


# --------------------------------------------------
# Nested while loops: multiplication table
# --------------------------------------------------
print("\nNESTED LOOPS: Multiplication table (1–5)")

first = 1
while first <= 5:
    second = 1
    while second <= 5:
        print(f"{first} times {second} is {first * second}")
        second += 1
    first += 1


# --------------------------------------------------
# break statement
# --------------------------------------------------
print("\nBREAK STATEMENT EXAMPLE")

command = input("Enter command: ")
while command != "stop":
    if command == "MAYDAY":
        break
    print("Executing command:", command)
    command = input("Enter command: ")

print("Execution stopped.")


# --------------------------------------------------
# while / else example
# --------------------------------------------------
print("\nWHILE / ELSE EXAMPLE")

command = input("Enter command: ")
while command != "stop":
    if command == "MAYDAY":
        break
    print("Executing command:", command)
    command = input("Enter command: ")
else:
    print("Goodbye.")

print("Execution stopped.")


# --------------------------------------------------
# Infinite loop example (DO NOT RUN)
# --------------------------------------------------
"""
number = 1
while number < 5:
    print(number)   # number never changes → infinite loop
"""
