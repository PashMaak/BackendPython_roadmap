# As easy at it looks
# if number is disible by 3 and 5 print FizzBuzz
# if number is divisible only by 3 print Fizz
# if number is divisible only by 5 print Buzz

try:
    input = int(input("Enter number: "))
    if (input % 3 == 0 and input % 5 == 0):
        print("FizzBuzz")
    elif (input % 3 == 0):
        print("Fizz")
    elif (input % 5 == 0):
        print("Buzz")
except ValueError:
    raise ValueError("Incorect input! Try again.")