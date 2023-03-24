
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def exponentiate(num1, num2):
    return num1 ** num2

def modulus(num1, num2):
    return num1 % num2

print("Welcome to the calculator program!")
print("Please choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Modulus")

operation = int(input("Enter operation number (1-6): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operation == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
elif operation == 5:
    print(num1, "^", num2, "=", exponentiate(num1, num2))
elif operation == 6:
    print(num1, "%", num2, "=", modulus(num1, num2))
else:
    print("Invalid input. Please choose an operation from 1-6.")
