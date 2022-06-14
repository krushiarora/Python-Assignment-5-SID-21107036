#First we check if the sides of the triangle make a triangle

#User inputs three sides

side1 = int(input("Enter length 1\n"))
side2 = int(input("Enter length 2\n"))
side3 = int(input("Enter length 3\n"))

a = side1 + side2
b = side2 + side3
c = side1 + side3


#If any of the three lengths is greater than the sum of the other two, then you cannot form a triangle.
#Checking for this condition
check_1 = a > side3
check_2 = b > side1
check_3 = c > side2

#Checking if the three conditions are true or false

triangle_check = str(check_1 & check_2 & check_3)

#Use Heron's formula if the sides form a triangle
s = round((side1 + side2 + side3) / 2)
ar_square = s * (s - side1) * (s - side2) * (s - side3)


if triangle_check == "True":
    area = (ar_square) ** (1/2)
    #Round off the result for a more understandable output
    area_print = round(area)
    #Print the area if sides form a triangle
    print("Area of the triangle is", area_print, "square units")

else:
    print("These sides do not form a triangle.")