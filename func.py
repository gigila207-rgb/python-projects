def add(a, b):
  return a + b 

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:

    print("""Choose an operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
""")

    operation = int(input("Choose: "))

    if operation == 5:
        print("Goodbye!")
        break

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))

    if operation == 1:
        result = add(num1, num2)

    elif operation == 2:
        result = subtract(num1, num2)

    elif operation == 3:
        result = multiply(num1, num2)

    elif operation == 4:
        result = divide(num1, num2)

    else:
        result = "Invalid operation"

    print("The result is:", result)



















