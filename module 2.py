import math
import random

# 1. Ask name and greet
name = input("Enter your name: ")
print(f"Hello, {name}!")
print()

# 2. Area of a circle
radius = float(input("Enter the radius of the circle: "))
circle_area = math.pi * radius ** 2
print(f"The area of the circle is {circle_area:.2f}")
print()

# 3. Rectangle perimeter and area
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

perimeter = 2 * (length + width)
area = length * width

print(f"Perimeter of the rectangle: {perimeter}")
print(f"Area of the rectangle: {area}")
print()

# 4. Sum, product, and average of three integers
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))

total_sum = num1 + num2 + num3
product = num1 * num2 * num3
average = total_sum / 3

print(f"Sum: {total_sum}")
print(f"Product: {product}")
print(f"Average: {average}")
print()

# 5. Medieval units to kilograms and grams
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

grams_per_lot = 13.3
lots_per_pound = 32
pounds_per_talent = 20

total_lots = (talents * pounds_per_talent * lots_per_pound) + \
             (pounds * lots_per_pound) + lots

total_grams = total_lots * grams_per_lot

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print("The weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")
print()

# 6. Random combination lock codes
code_3_digit = [random.randint(0, 9) for _ in range(3)]
code_4_digit = [random.randint(1, 6) for _ in range(4)]

print("3-digit combination lock code:", code_3_digit)
print("4-digit combination lock code:", code_4_digit)
