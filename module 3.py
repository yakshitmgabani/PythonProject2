# 1) Zander size check
length = int(input("Enter the length of the zander (cm): "))
size_limit = 42

if length < size_limit:
    difference = size_limit - length
    print("The zander is too small. Release it back into the lake.")
    print(f"It is {difference} cm below the size limit.")
else:
    print("The zander meets the size limit.")

print()  # empty line for readability

# 2) Cruise ship cabin class description
cabin_class = input("Enter cabin class (LUX, A, B, C): ").upper()

if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

print()

# 3) Hemoglobin level check
gender = input("Enter biological gender (female/male): ").lower()
hemoglobin = int(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Hemoglobin level is low.")
    elif hemoglobin <= 155:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Hemoglobin level is low.")
    elif hemoglobin <= 167:
        print("Hemoglobin level is normal.")
    else:
        print("Hemoglobin level is high.")
else:
    print("Invalid gender.")

print()

# 4) Leap year checker
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")