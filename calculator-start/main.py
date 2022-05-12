from art import logo
print(logo)
import math

#Calculator Project
#Add Function
def add(n1, n2):
  return n1 + n2

#Subtract Function
def subtract(n1, n2):
  return n1 - n2

#Multipy Function
def multiply(n1, n2):
  return n1 * n2

#Divide Function
def divide(n1, n2):
  return n1 / n2  
operations ={
"+": add, 
"-": subtract, 
"*": multiply, 
"/": divide       
}
# function = operations["+"]
# function(2, 3)
# print(function)
#print(operations[add])
def calculator(): #this is known as recursion
  # num1 = int(input("What's the first number?: "))
  num1 = float(input("What's the first number?: "))
  continue_on = True
  for symbol in operations:
    print(symbol)
  while continue_on:
    operation_symbol = input("Pick an Operator symbol. ")
    #num2 = int(input("What's the next number?: "))
    num2 = float(input("What's the next number?: "))
  #How i did it below
    # if operation_symbol in operations:
    #   first_answer = operations[operation_symbol](num1, num2)
  
  #how the instructor did it
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}" )
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == "y":
      num1 = answer    
    else:    
      continue_on = False
      #print("All Calculations have ended")
      calculator()
calculator() #this is known as recursion
#code not neccessary
# operation_symbol = input("Pick an Operator symbol from Above ")
# num3 = int(input("What's the next number?: "))
# calculation_function = operations[operation_symbol]
# second_answer = calculation_function(first_answer, num3)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}" )

# new_answer = second_answer
  # continue_on = input(f"Type 'y' to continue calculating with {new_answer}, or type 'n' to exit.: ")
# operation_symbol = input("Pick an Operator symbol from Above ")
    # new_num = int(input("What's the next number?: "))
    # calculation_function = operations[operation_symbol]
    # new_answer = calculation_function(new_answer, new_num)
    # print(f"{new_answer} {operation_symbol} {new_num} = {new_answer}" )    
# continue_on = "y"
# new_answer = second_answer
# while continue_on == "y":  
  




