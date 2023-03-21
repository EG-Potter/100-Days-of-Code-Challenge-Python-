#Calculator

#Add
def add(n1,n2):
  return n1 + n2

#Subtract
def subtract(n1,n2):
  return n1 - n2

#Multiply
def multiply(n1,n2):
  return n1 * n2

#Divide
def divide(n1,n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

num1 = int(input("Whats the first number? "))
num2 = int(input("Whats the second number? "))

for operation in operations:
  print(operation)

symbol = input("Pick an operation from the line above: ")

calculation = operations[symbol]

answer = calculation(num1, num2)



print(f"{num1} {symbol} {num2} = {answer}")