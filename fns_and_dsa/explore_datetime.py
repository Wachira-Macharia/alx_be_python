# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print(f"Current date and time: {formatted_date}")
    return current_date

# Part 2: Calculate a Future Date
def calculate_future_date(days_to_add):
    current_date = datetime.now()  # Get the current date and time
    future_date = current_date + timedelta(days=days_to_add)  # Calculate the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
    print(f"Future date: {formatted_future_date}")
    return future_date

# Main function to demonstrate both parts
def main():
    # Display the current date and time
    display_current_datetime()

    # Prompt user to enter a number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
