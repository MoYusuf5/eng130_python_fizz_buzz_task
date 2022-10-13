# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz" instead of the number
# For numbers which are multiples of both three and five print "FizzBuzz".


for number in range(101):
    if (number % 3 == 0 and number % 5 == 0):
        print(("FizzBuzz"))
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 ==0):
        print("Buzz")
