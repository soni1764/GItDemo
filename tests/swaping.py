def swap(a, b):
    b, a = a, b
    return a, b


a = int(input("Enter first number\n"))
b = int(input("Enter first number\n"))

result = swap(a,b)
print(result)

print("---------------------")

a = 10
b = 20

if a < 10:
    print("A is less than B")
elif a == b:
    print("A is equl to B")
else:
    print("A is greater than B")
print("---------------------")


