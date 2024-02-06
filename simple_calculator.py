#welcome message
print("Welcome to the calculator! \n")

#stores action for expression based on input from user
express = int(input("Press the corresponding number for what you like to do:\n"
                " 1 : add \n 2 : subtract \n 3 : divide \n 4 : multiple \n"))

#stores first number user enters
first = int(input("Enter in the first number you would like in the expression: \n"))

#stores second number user enters
second = int(input("Enter in the second number you would like in the expression: \n"))

#if user enters one, adds and prints result
if express == 1:
    add = first + second
    print("Your expression is: ", first , " + " , second , " = " , add)

#if user enters two, subtracts and prints result
elif express == 2:
        subtract = first - second
        print("Your expression is: ", first , " - " + second +" = " , subtract)

#if user enters three, divides and prints result
elif express == 3:

        divide = first/second
        print("Your expression is: ", first + " / " , second , " = " , divide)

#if user enters four, multiplies and prints result
elif express == 4:

        multiply = first*second
        print("Your expression is: ", first , " * " , second , " = " , multiply)

#else, prints invalid message
else:
        print("Your input was invalid")
