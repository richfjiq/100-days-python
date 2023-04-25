from art import logo
# from replit import clear

def calc_operations(operation, num1, num2):
  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
  elif operation == "/":
    return num1 / num2
  else:
    return "Invalid operation."

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  print("+")
  print("-")
  print("*")
  print("/")
  should_continue = True
  while should_continue:
    picked_operation = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    result = calc_operations(picked_operation, num1, num2)
    print(f"{num1} {picked_operation} {num2} = {result} ")
    new_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if new_calculation == "y":
      num1 = result
    else:
      should_continue = False
      # clear()
      calculator()

calculator()