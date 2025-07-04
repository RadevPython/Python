# This is a simple calculator application.
# Nolan Welch
import time #This is needed in order to space out the output so the user isn't overwhelmed.
time.sleep(1)
print("Python Calculator made by Br.17.17, 02/07/2025.\n\n\n")
time.sleep(2.5)
# Defining the calculator function, which is used to make all the calculations based on user input
def calculator():
   var1 = input("Enter first number:  ")
   var2 = input("Enter second number:  ")
   if (checkIfInt(var1) and checkIfInt(var2)):
       var1 = int(var1)
       var2 = int(var2)
       if (userInput == "*"):
           print("The product of the first and second number is " + str(mul(var1, var2)))
       elif (userInput == "/"):
           print("The first number divided by the second number is " + str(div(var1, var2)))
       elif (userInput == "+"):
           print("The sum of the first and second numbers is " + str(add(var1, var2)))
       elif(userInput == "-"):
           print("The first number minus the second number is " + str(sub(var1, var2)))
       else:
           print("Invalid input.")
           time.sleep(2)
           main()
   else:
       print("Both inputs must be integers.\nTaking you back to the calculator...")
       time.sleep(2)
       calculator()
def add(num1, num2):
   return(num1 + num2)
def mul(num1, num2):
   return(num1 * num2)
def div(num1, num2):
   return(num1 / num2)
def sub(num1, num2):
   return(num1 - num2)
# Defining a function that checks whether or not the input is an integer(used in the calculator function)
def checkIfInt(possibleInt):
   try:
       val = int(possibleInt)
       return True
   except ValueError:
       return False
# After the entire program has been run, this function checks whether or not the user would like to use the calculator again
def again():
   repeat = input("Would you like to use the calculator again?  ").lower()
   if(repeat == "y" or repeat == "yes"):
       main()
   elif(repeat == "n" or repeat == "no"):
       print("See you next time!")
       time.sleep(2)
       quit()
   else:
       while(True):
           print("Sorry, invalid input.")
           time.sleep(1)
           again()
def main():
   global userInput
   userInput = input("Which mathematical function would you like to do? Insert *, /, +, or -. Type HELP for help.  ")
   if(userInput == "HELP"):
       print("\n* = Multiplication\n/ = Division\n+ = Addition\n- = Subtraction")
       secondaryInput = input("\nType \"BACK\" to go back to the calculator.  ")
       if (secondaryInput == "BACK"):
           main()
       else:
           while(True):
               backInput = input("Invalid input. Please type \"BACK\" to return to the calculator.  ")
               if(backInput == "BACK"):
                   main()
   # Making sure that the user inputs one of the four accepted operators
   elif (userInput != "*" and userInput != "/" and userInput != "+" and userInput != "-"):
       print("Invalid input!")
       time.sleep(2)
       main()
   else:
       calculator()
   again()
main()
""" This entire program seems to be out of order, but I put some functions before others for the sake of
   simplicity in the final code and in an effort to avoid errors.
"""
