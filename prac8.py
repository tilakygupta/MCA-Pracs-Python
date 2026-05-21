# ==================================================
# CUSTOM EXCEPTION CLASS
# ==================================================

class AgeValidationError(Exception):
    pass


# ==================================================
# MAIN PROGRAM
# ==================================================

try:

    # Input numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Division
    result = num1 / num2

    print("\nDivision Result =", result)

    # Age input
    age = int(input("\nEnter your age: "))

    # Custom exception check
    if age < 18:
        raise AgeValidationError(
            "Age below 18 is not allowed."
        )

    print("Age is valid.")

# ==================================================
# HANDLE DIVISION BY ZERO
# ==================================================

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# ==================================================
# HANDLE INVALID INPUT
# ==================================================

except ValueError:
    print("Error: Invalid input. Please enter numbers only.")

# ==================================================
# HANDLE CUSTOM EXCEPTION
# ==================================================

except AgeValidationError as e:
    print("Custom Exception:", e)

# ==================================================
# FINALLY BLOCK
# ==================================================

finally:
    print("\nProgram execution completed.")