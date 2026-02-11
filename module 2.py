# Conditional Statements Assignment
# This program demonstrates if, elif, else, comparison operators, and logical operators

# Latte purchase example
money = float(input("Enter the amount of money you have (€): "))

if money >= 5:
    print("You can buy a latte.")
else:
    print("You do not have enough money to buy a latte.")

print()  # empty line for readability

# Medicine eligibility example
age = int(input("Enter age: "))

if 15 <= age < 18:
    weight = float(input("Enter weight (kg): "))

if age >= 18 or (age >= 15 and weight >= 55):
    print("The medicine can be used.")
else:
    print("The medicine cannot be used.")

print()

# Age category example
age = int(input("Enter your age again: "))

if age >= 65:
    print("You are retired.")
elif age >= 18:
    print("You are working-age.")
elif age >= 7:
    print("You are in school.")
else:
    print("You are a small child.")
