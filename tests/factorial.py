# This file is cleated at the Banglore end
print("Hello, Delhi How are you doing ")

def factorial(n):

    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)


n = int(input("Enter a number to get its factorial:\n"))
fact = factorial(n)
print(fact)
