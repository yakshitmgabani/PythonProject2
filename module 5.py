"""
List Structures and Iterative Loop Structures (for)
Assignment demonstration

Covers:
1. Creating lists
2. Indexing and slicing
3. List length
4. Index out of range example (commented)
5. List operations
6. Iterating through lists with for loop
7. range() function usage
"""


# --------------------------------------------------
# 1. Creating a list
# --------------------------------------------------
names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

print("Original list:")
print(names)


# --------------------------------------------------
# 2. Indexing and slicing
# --------------------------------------------------
print("\nIndexing examples:")
print(names[3])      # Olga
print(names[1])      # Ahmed
print(names[-2])     # Olga

print("\nSlicing examples:")
print(names[1:3])    # ['Ahmed', 'Pekka']
print(names[2:])     # ['Pekka', 'Olga', 'Mary']


# --------------------------------------------------
# 3. Length of list
# --------------------------------------------------
print("\nLength of list:")
print(len(names))


# --------------------------------------------------
# 4. Index out of range example (DO NOT RUN)
# --------------------------------------------------
"""
print(names[5])  # IndexError: list index out of range
"""


# --------------------------------------------------
# 5. List operations
# --------------------------------------------------
print("\nList operations:")

names.append("Matti")
print("After append:", names)

names.insert(2, "Teppo")
print("After insert:", names)

names.remove("Ahmed")
print("After remove:", names)

other_names = ["Allu", "Ninni"]
names.extend(other_names)
print("After extend:", names)

if "Olga" in names:
    print("Olga found in list")

print("Index of Pekka:", names.index("Pekka"))

names.sort()
print("After sort:", names)


# --------------------------------------------------
# 6. User input list + for loop iteration
# --------------------------------------------------
print("\nEnter names (press Enter to stop):")

user_names = []
name = input("Enter name: ")

while name != "":
    user_names.append(name)
    name = input("Enter name: ")

print("\nGreeting all users:")
for n in user_names:
    print(f"Hello, {n}!")


# --------------------------------------------------
# 7. for loop with range()
# --------------------------------------------------
print("\nNumbers divisible by 3 from 3 to 30:")
for number in range(3, 31, 3):
    print(number)

print("\nPrint Hello 6 times:")
for i in range(6):
    print("Hello!")
