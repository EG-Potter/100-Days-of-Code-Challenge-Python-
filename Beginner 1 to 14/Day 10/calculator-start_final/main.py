#Calculator
from art import logo
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

def calculator():
  print(logo)
  
  num1 = float(input("Whats the first number? "))
  
  for operation in operations:
    print(operation)
  
  symbol = input("Pick an operation from the line above: ")
  num2 = float(input("Whats the second number? "))
  calculation = operations[symbol]
  answer = calculation(num1, num2)
  
  print(f"{num1} {symbol} {num2} = {answer}")
  
  active = True 
  
  while active:
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == 'n':
      active = False
      calculator()

    for operation in operations:
      print(operation)
    symbol = input("Pick another operation: ")
    num3 = float(input("Whats the second number? "))
    calculation = operations[symbol]
    answer2 = calculation(answer, num3)
    
    print(f"{answer} {symbol} {num3} = {answer2}")
  
    answer = answer2

calculator()