#Take 10 integers as input from user.

int_1 = int(input("1st integer: "))
int_2 = int(input("2nd integer: "))
int_3 = int(input("3rd integer: "))
int_4 = int(input("4th integer: "))
int_5 = int(input("5th integer: "))
int_6 = int(input("6th integer: "))
int_7 = int(input("7th integer: "))
int_8 = int(input("8th integer: "))
int_9 = int(input("9th integer: "))
int_10 = int(input("10th integer: "))

#Make a list of the integers, so that it is easier to traverse them for operations in loop
integer_list = [int_1, int_2, int_3, int_4, int_5, int_6, int_7, int_8, int_9, int_10]

#Applying simple if else statements to print required outputs

#Part (a)
print("Positive numbers are:")
for number in integer_list:
    if number > 0:
        print(number)

#Part (b)
print("Negative numbers are:")
for number in integer_list:
    if number < 0:
        print(number)

#Part (c)
print("Odd numbers are:")
for number in integer_list:
    if number % 2 != 0:
        print(number)

#Part (d)
print("Even numbers are:")
for number in integer_list:
    if number % 2 == 0:
        print(number)

#Part (e)
""" Assign number of occurances of an integer to a corresponding
variable and print the same."""
"""If an integer is repeating, we do not need to count it again, so
we will use if statements to print only if the integer is unique"""

count_1 = integer_list.count(int_1)
count_2 = integer_list.count(int_2)
count_3 = integer_list.count(int_3)
count_4 = integer_list.count(int_4)
count_5 = integer_list.count(int_5)
count_6 = integer_list.count(int_6)
count_7 = integer_list.count(int_7)
count_8 = integer_list.count(int_8)
count_9 = integer_list.count(int_9)
count_10 = integer_list.count(int_10)



print(int_1, "occurs", count_1, "times") 


if int_2 != int_1:
    print(int_2, "occurs", count_2, "times")
    
    
if int_3 != int_1 and int_3 != int_2:
    print(int_3, "occurs", count_3, "times")
    
    
if int_4 != int_1 and int_4 != int_2 and int_4 != int_3:
    print(int_4, "occurs", count_4, "times")
    
    
if int_5 != int_1 and int_5 != int_2 and int_5 != int_3 and int_5 != int_4:
    print(int_5, "occurs", count_5, "times")

    
if int_6 != int_1 and int_6 != int_2 and int_6 != int_3 and int_6 != int_4 and int_6 != int_5:
    print(int_6, "occurs", count_6, "times")
 
    
if int_7 != int_1 and int_7 != int_2 and int_7 != int_3 and int_7 != int_4 and int_7 != int_5 and int_7 != int_6:
    print(int_7, "occurs", count_7, "times")
    
    
if int_8 != int_1 and int_8 != int_2 and int_8 != int_3 and int_8 != int_4 and int_8 != int_5 and int_8 != int_6 and int_8 != int_7:
    print(int_8, "occurs", count_8, "times")
    
    
if int_9 != int_1 and int_9 != int_2 and int_9 != int_3 and int_9 != int_4 and int_9 != int_5 and int_9 != int_6 and int_9 != int_7 and int_9 != int_8:
    print(int_9, "occurs", count_9, "times")
    
    
if int_10 != int_1 and int_10 != int_2 and int_10 != int_3 and int_10 != int_4 and int_10 != int_5 and int_10 != int_6 and int_10 != int_7 and int_10 != int_8 and int_10 != int_9:
    print(int_10, "occurs", count_10, "times")
