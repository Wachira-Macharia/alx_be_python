# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    while True:
        try:
            # Prompt the user to enter a temperature and validate it's a number
            temp_input = input("Enter the temperature to convert (or 'exit' to quit): ")
            if temp_input.lower() == 'exit':
                print("Goodbye!")
                break
            temp_input = float(temp_input)  # Input validation for numeric value

            # Ask the user to specify if it's Celsius or Fahrenheit and validate input
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
            if unit not in ['C', 'F']:
                raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

            # Perform conversion based on user input
            if unit == 'F':
                converted_temp = convert_to_celsius(temp_input)
                print(f"{temp_input}°F is {converted_temp:.2f}°C")
            elif unit == 'C':
                converted_temp = convert_to_fahrenheit(temp_input)
                print(f"{temp_input}°C is {converted_temp:.2f}°F")

        except ValueError as e:
            # Handle invalid inputs and display an error message
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
