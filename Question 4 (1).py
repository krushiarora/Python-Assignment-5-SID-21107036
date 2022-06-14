#Use string formatting to print the required output
string = "*"

"""Starting with n = 5, we make a for loop for a number in range n,
since we want nested for loop, we make another loop inside in which the range
is the number (whose earlier range was defined as n)
Using string formatting to print the required output"""
n = 5
for number in range(n):
    for nested_no in range(number):
        print(string, end=" ")
    print(" ")    


for number in range(n , 0, -1):
    for nested_no in range(number):
        print(string, end=" ")
    print(" ")    
        