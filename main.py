# Name: Chase Prasad
# Title: Scientific Calculator

# used for logarithm function of calculator
import math

# used to keep calculator running
cont = True
# used to keep track of current result
result = 0.0
# used for average calculations
sum = 0.0
count = 0

# displaying initial menu
print("Current Result: " + str(result))
print("\nCalculator Menu")
print("-" * 15)
print("0. Exit Program")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")
print("6. Logarithm")
print("7. Display Average")

# asking user for menu choice
selection = int(input("Enter Menu Selection: "))

# loop used to keep calculator running
while(cont):
    match selection:
        # exits calculator through while loop
        case 0:
            print("\nThanks for using this calculator. Goodbye!")
            cont = False
        # addition calculation
        case 1:
            # asks user for first number input
            first = input("Enter first operand: ")
            # checks if user wants to use previous result or not
            if(first == "RESULT"):
                first = result
            else:
                first = float(first)
            # same function as first number input
            second = input("Enter second operand: ")
            if(second == "RESULT"):
                second = result
            else:
                second = float(second)
            # calculation and printing
            result = first + second
            sum += result
            count += 1
            print("")

            print("Current Result: " + str(result))
            # re-displays menu for user
            print("\nCalculator Menu")
            print("-" * 15)
            print("0. Exit Program")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("6. Logarithm")
            print("7. Display Average\n")

            selection = int(input("Enter Menu Selection: "))
# same functionality for cases 2 through 6 as case 1
        # subtraction calculation
        case 2:
            first = input("Enter first operand: ")
            if(first == "RESULT"):
                first = result
            else:
                first = float(first)
            second = input("Enter second operand: ")
            if(second == "RESULT"):
                second = result
            else:
                second = float(second)
            result = first - second
            sum += result
            count += 1
            print("")

            print("Current Result: " + str(result))
            print("\nCalculator Menu")
            print("-" * 15)
            print("0. Exit Program")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("6. Logarithm")
            print("7. Display Average\n")

            selection = int(input("Enter Menu Selection: "))
        # multiplication calculation
        case 3:
            first = input("Enter first operand: ")
            if(first == "RESULT"):
                first = result
            else:
                first = float(first)
            second = input("Enter second operand: ")
            if(second == "RESULT"):
                second = result
            else:
                second = float(second)
            result = first * second
            sum += result
            count += 1
            print("")

            print("Current Result: " + str(result))
            print("\nCalculator Menu")
            print("-" * 15)
            print("0. Exit Program")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("6. Logarithm")
            print("7. Display Average\n")

            selection = int(input("Enter Menu Selection: "))
        # division calculation
        case 4:
            first = input("Enter first operand: ")
            if(first == "RESULT"):
                first = result
            else:
                first = float(first)
            second = input("Enter second operand: ")
            if(second == "RESULT"):
                second = result
            else:
                second = float(second)
            result = first / second
            sum += result
            count += 1
            print("")

            print("Current Result: " + str(result))
            print("\nCalculator Menu")
            print("-" * 15)
            print("0. Exit Program")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("6. Logarithm")
            print("7. Display Average\n")

            selection = int(input("Enter Menu Selection: "))
        # exponentiation calculation
        case 5:
            first = input("Enter first operand: ")
            if(first == "RESULT"):
                first = result
            else:
                first = float(first)
            second = input("Enter second operand: ")
            if(second == "RESULT"):
                second = result
            else:
                second = float(second)
            result = first ** second
            sum += result
            count += 1
            print("")

            print("Current Result: " + str(result))
            print("\nCalculator Menu")
            print("-" * 15)
            print("0. Exit Program")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("6. Logarithm")
            print("7. Display Average\n")

            selection = int(input("Enter Menu Selection: "))
        # logarithm calculation
        case 6:
            first = input("Enter first operand: ")
            if(first == "RESULT"):
                first = result
            else:
                first = float(first)
            second = input("Enter second operand: ")
            if(second == "RESULT"):
                second = result
            else:
                second = float(second)
            result = math.log(second, first)
            sum += result
            count += 1
            print("")

            print("Current Result: " + str(result))
            print("\nCalculator Menu")
            print("-" * 15)
            print("0. Exit Program")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("6. Logarithm")
            print("7. Display Average\n")

            selection = int(input("Enter Menu Selection: "))
        # average calculation
        case 7:
            # checks if any calculations have actually been done and asks for another input if not
            if(count == 0):
                print("Error: No calculations yet to average!\n")

                selection = int(input("Enter Menu Selection: "))
            else:
                # calculates average and asks for next input
                average = sum / count
                print("\nSum of calculations: " + str(sum))
                print("Number of calculations: " + str(count))
                print("Average of calculations: " + str(round(average, 2)))
                print("")

                selection = int(input("Enter Menu Selection: "))
        # fallback if error is thrown
        case _:
            print("\nError: Invalid selection!\n")

            selection = int(input("Enter Menu Selection: "))