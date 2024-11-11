import math

print("Choose your operation: ")
print("1. Addition")
print("2. Subtarction")
print("3. Multiplication")
print("4. Division")
print("5. Square root")

choice = int(input("Enter the opeartion number you want to perform: "))
if choice in [1, 2, 3, 4]:  # These operations require two numbers
    a = float(input("Enter number one: "))
    b = float(input("Enter second number: "))
elif choice == 5:  # Square root only needs one number
    a = float(input("Enter the number: "))
else:
    print("Invalid choice!")
    exit()

def add(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    return a / b
def squareroot(a):
    return math.sqrt(a)

if choice == 1:
    print("Addition result: ",add(a,b))
elif choice == 2:
    print("Subtraction result: ",subtraction(a,b))
elif choice == 3:
    print("Multiplication result: ",multiplication(a,b))
elif choice == 4:
    print("Division result: ",division(a,b))
elif choice == 5:
    print("Squareroot result: ",squareroot(a))
else:
    print("Invalid choice!")
