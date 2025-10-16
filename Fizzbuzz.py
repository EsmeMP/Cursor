# if the number is divisible by 3, print "Fizz"
# if the number is divisible by 5, print "Buzz"
# if the number is divisible by 3 and 5, print "FizzBuzz"
# if the number is not divisible by 3 or 5, print the number


# ask the user for the number of the range
number = int(input("Enter the number of the range: ")) 
for i in range(1, number + 1):
    if i % 3 == 0 and i % 5 == 0:
    # if the number is divisible by 3 and 5, print "FizzBuzz"
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    # if the number is not divisible by 3 or 5, print the number
    else:
        print(i)