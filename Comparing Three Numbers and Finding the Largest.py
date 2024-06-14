# Comparing Three Numbers and Finding the Largest

# Prompt the user to enter three numbers
num1 = float(input("Please input your first number: "))
num2 = float(input("Please input your second number: "))
num3 = float(input("Please input your third number: "))

# Determine the largest number among the three
if num1 >= num2 and num1 >= num3:
    # Check if the first number is equal to the second or third number
    if num1 == num2 and num1 != num3:
        print("Your first number is equal to your second number.")
    elif num1 == num3 and num1 != num2:
        print("Your first number is equal to third number.")
    elif num1 == num2 == num3:
        print("Your first, second and third number are the same number.")
    elif num2 == num3 and num2 != num1:
        print("Your second number is equal to your third number.")
    # Output the largest number
    print(f"The biggest number is {num1}")

elif num2 >= num1 and num2 >= num3:
    # Check if the second number is equal to the first or third number
    if num1 == num2 and num1 != num3:
        print("Your first number is equal to your second number.")
    elif num1 == num3 and num1 != num2:
        print("Your first number is equal to third number.")
    elif num1 == num2 == num3:
        print("Your first, second and third number are the same number.")
    elif num2 == num3 and num2 != num1:
        print("Your second number is equal to your third number.")
    # Output the largest number
    print(f"The biggest number is {num2}")

elif num3 >= num1 and num3 >= num2:
    # Check if the third number is equal to the first or second number
    if num1 == num2 and num1 != num3:
        print("Your first number is equal to your second number.")
    elif num1 == num3 and num1 != num2:
        print("Your first number is equal to third number.")
    elif num1 == num2 == num3:
        print("Your first, second and third number are the same number.")
    elif num2 == num3 and num2 != num1:
        print("Your second number is equal to your third number.")
    # Output the largest number
    print(f"The biggest number is {num3}")
else:
    print("Error: Please enter a valid number.")