
# A Basic Calculator
'''
This calculator performs basic arithmetic operations - addition, subtraction, multiplication and division
Collects 3 input data - num1, num2 and operator
Converts num1 and num2 to int
Checks the type of operator inputed using if
Prints the answer, else, "Incorrect input, Try again by inputting two numbers with a +, -, *, / or % operator."
'''

num1, operator, num2 = input("Enter your basic arithmetic below\n").split()
num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "%":
    print("{} % {} = {}".format(num1, num2, num1 % num2))
else:
    print("Incorrect input, Try again by inputting two numbers with a +, -, *, / or '%' operator.")