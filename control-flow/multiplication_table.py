# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate through the numbers 1 to 10
for i in range(1, 11):
    product = number * i  # Calculate the product of the number and the current iteration value
    print(f"{number} * {i} = {product}")
