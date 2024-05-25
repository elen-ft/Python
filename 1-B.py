def factorial(num):
    if num < 0:
        print("num must be non-negative")
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

number = int(input("Enter a non-negative number: "))

try:
    result = factorial(number)
    print("The factorial of {} is {}".format(number, result))
except ValueError as e:
    print("Error: {}".format(e))
