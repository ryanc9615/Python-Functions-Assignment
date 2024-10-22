## Addition
def addition(a,b):
    return a + b

## Subtraction
def subtraction(a,b):
    return a - b

## Multiplication 
def multiplication(a,b):
    return a * b

## Division
def division(a,b):
    # Handle division by zero
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def main():
    first_number = int(input("Input a number: "))
    second_number = int(input("Input a second number: "))
    operation = int(input("Select operation: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n Enter your choice (1/2/3/4): "))

    if operation == 1: 
        add_output = addition(first_number, second_number)
        print("Result:", add_output)
    elif operation == 2:
        sub_output = subtraction(first_number, second_number)
        print("Result:", sub_output)
    elif operation == 3:
        mul_output = multiplication(first_number, second_number)
        print("Result:", mul_output)
    elif operation == 4:
        div_output = division(first_number, second_number)
        print("Result:", div_output)
    else:
        print("Invalid operation choice. Please select a number between 1 and 4.")

# Call the main function to run the program
main()
