def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
choice = input("Enter the operation (+, -, *, /): ")

if choice == '+':
    print(f"The result is: {add(a,b)}")

elif choice == '-':
    print(f"The result is: {subtract(a,b)}")

elif choice == '*':
    print(f"The result is: {multiply(a,b)}")

elif choice == '/':
    if b != 0:
        print(f"The result is: {divide(a,b)}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print(f"{choice} is not a valid operation.")