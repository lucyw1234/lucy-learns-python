# oppose the shape to calculate the area

print("Choose a shape to calculate the area")
print("1. Rectangle")
print("2. Square")
print("3. Triangle")

# Take user input
choice = input("Enter 1, 2, or 3: ")

# Rectangle
if choice == "1":
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    area = length * width
    print("The area of the rectangle is:", area)

# Square
elif choice == "2":
    side = int(input("Enter the length of one side of the square: "))
    area = side * side
    print("The area of the square is:", area)

# Triangle
elif choice == "3":
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)

# Invalid input
else:
    print("Invalid choice.")
