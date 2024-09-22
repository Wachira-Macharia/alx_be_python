# Prompt the user to input a positive integer for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# Use a while loop to iterate through each row of the pattern
while row < size:
    # For each row, use a for loop to print asterisks (*) side by side
    for col in range(size):
        print("*", end="")  # Print an asterisk without a newline
    print()  # After each row, print a newline to move to the next row
    row += 1  # Increment the row counter
