def add(a, b):
  return a + b 

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b

print("""Choose an operation:
1. Add
2. Subtract
3. Multiply
4. Divide
""")

operation = int(input())
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
if operation == 1 :
  result = add(num1,num2)
  print("the result is : ",result )
elif  operation == 2 :
  result = subtract(num1,num2)
  print("the result is : ",result )
elif operation == 3 :
  result = multiply(num1,num2)
  print("the result is : ",result )

elif operation == 4 :
  result = divide(num1,num2)
  print("the result is : ",result )
else :
  print("invalid operation ,please try again")




















