"""Take the range by asking the user for two numbers
that will be the starting and end points for the range"""

start_range = int(input("Enter start of range:\n"))
end_range = int(input("Enter end of range:\n"))


#Create three cases for if numbers are starting from 0, 1, or some other number

""" Divide the numbers by the numbers preceding them,
if they are divisible, they are not prime.
So, everytime a number is divisible, increase the value of a variable,
if the variable remains zero, the number is prime """


print("Prime numbers in the range are:")
#Since we know 0 and 1 are not prime, we start from 2.
if start_range == 0:
    for number in range(start_range + 2, end_range+1):
        check = 0
        for divide_check in range(2, number):
            if number % divide_check == 0:
                check += 1
        if check == 0:
             print(number)
    
elif start_range == 1:
    for number in range(start_range + 1, end_range+1):
        check = 0
        for divide_check in range(2, number):
            if number % divide_check == 0:
                check += 1
        if check == 0:
             print(number)
    
else:
    for number in range(start_range , end_range+1):
        check = 0
        for divide_check in range(2, number):
            if number % divide_check == 0:
                check += 1
        if check == 0:
            print(number)