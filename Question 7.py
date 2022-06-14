#Take range from 1 to 500.
#Then use if else with and operator to print the numbers divisible by 7 and 11.

print("Numbers which are multiple of 7 and divisible by 11 in the range 1-500 are:")
for number in range(1, 500):
   if number % 7 == 0 and number % 11 == 0:
       print(number)