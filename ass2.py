1. start (Program execution begins here)
2. Prompt the user to input two integer values, x and y.
 We use int(input(...)) to ensure the users input is treated as an integer.
print("--- Basic Arithmetic Calculator ---")
try:
    x = int(input("Enter the first integer (x): "))
    y = int(input("Enter the second integer (y): "))
except ValueError:
    print("Invalid input. Please enter valid integers.")
    # Stop the program if input is not a valid integer
    exit() 

3. Calculate and print the addition (x + y)
addition = x + y
print(f"\nResult of Addition (x + y): {addition}")

4. Calculate and print the subtraction (x - y)
subtraction = x - y
print(f"Result of Subtraction (x - y): {subtraction}")
 5. Calculate and print the multiplication (x * y)
multiplication = x * y
print(f"Result of Multiplication (x * y): {multiplication}")

6. Calculate and print the power (x ** y)
The ** operator is used for exponentiation (x raised to the power of y)
power = x ** y
print(f"Result of Power (x ** y): {power}")

--- Division Operations (Handling potential division by zero) ---
if y != 0:
    7. Calculate and print the true division (x / y) - results in a float
    true_division = x / y
    print(f"Result of True Division (x / y): {true_division}")

    8. Calculate and print the floor division (x // y) - results in an integer
    floor_division = x // y
    print(f"Result of Floor Division (x // y): {floor_division}")

    9. Calculate and print the modulus (x % y) - results in the remainder
    modulus = x % y
    print(f"Result of Modulus/Remainder (x % y): {modulus}")
else:
    print("\nNote: Cannot perform division or modulus by zero (y=0).")

10. Stop (Program ends)
print("\n--- Program Finished ---")
