import random

number = random.randint(1, 101)
print(number)
#number = int(input("please enter a number "))
if number % 5 == 0 and number % 3 == 0:
    print("Fizz Buzz")

elif number % 3 == 0:
    print("Fizz")

elif number % 5 == 0:
    print("Buzz")