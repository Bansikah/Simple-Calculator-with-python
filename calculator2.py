# define functions for arithmetic operations
import math
def add(x, y):
 return x + y
def subtract(x, y):
 return x - y
def multiply(x, y):
 return x * y
def divide(x, y):
 return x % y


# get user input
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5.Modolus")
#returning the value sin of p
choice = input("Enter choice(1/2/3/4/5): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# a = float(input("Enter a value:"))

#print("The value of sin of pi / 6 is :", end="")
# print(math.sin())
# perform selected arithmetic operation
if choice == '1':
 print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
 print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
 print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
 print(num1, "/", num2, "=", divide(num1, num2))
elif choice == '5':
 print(num1, "%", num2, "=", divide(num1, num2))
else:
 print("Invalid input")