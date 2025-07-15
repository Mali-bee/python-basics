#task: calculate the area and perimeter of a rectangle

import calculate
print()

rect_length = int(input("Enter the length of the rectangle: "))
rect_width = int(input("Enter the width of the rectangle: "))
print()

rect_area = calculate.calc_area(rect_length, rect_width)
print(f"The area of the rectanlge is: {rect_area}cm")
print()

rect_perimeter = calculate.calc_perimeter(rect_length, rect_width)
print(f"The perimeter of a rectange is: {rect_perimeter}cm")
print()