# Define functions for basic arithmetic operations
def add(n1, n2):
    """Adds two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Subtracts two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Multiplies two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Divides two numbers, handling division by zero errors."""
    if n2 == 0:
        return "Error: Division by zero" # Prevents program crash
    return n1 / n2

def calculator():
    """Main calculator function with user input and operations loop."""
    while True: # Loop allows multiple calculations until the user quits
        # Display menu options to the user
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit") # Option to break the loop and end the program

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break # Exit the while loop

        # Validate input choice
        if choice in ('1', '2', '3', '4'):
            try:
                # Take number inputs and convert them to floating-point numbers
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    result = divide(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
            except ValueError:
                # Handle cases where the user enters non-numeric values
                print("Invalid input! Please enter valid numbers.")
        else:
            print("Invalid Choice! Please select a valid operation (1-5).")

# Start the calculator program
if __name__ == "__main__":
    calculator()
