def swap(a, b):
    b, a = a, b
    return a, b


a = int(input("Enter first number\n"))
b = int(input("Enter first number\n"))

result = swap(a,b)
print(result)

print("--------------------------")


a = int(input("Enter first number\n"))
b = int(input("Enter first number\n"))

print(a, b)
b, a = a, b

print(a, b)