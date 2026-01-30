def calculate_area(length, width):
    return length * width

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")
