# Display a welcome message
print("Hello, and welcome to temp changer 3000")
print("Let's get started ")

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    somecelsius = float(input("What degree Celsius would you like to convert to Fahrenheit?\n"))
    fahrenheit = (somecelsius * 9/5) + 32.0
    print(f"\n{somecelsius} degrees Celsius is {fahrenheit} degrees Fahrenheit\n")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
    somefahrenheit = float(input("What degree Fahrenheit would you like to convert to Celsius?\n"))
    celsius = (somefahrenheit - 32) * 5/9
    print(f"\n{somefahrenheit} degrees Fahrenheit is {celsius} degrees Celsius\n")

# Main program function
def main():
    print("Please select one of the following options:\n")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input(":")
    
    if choice == "1":
        celsius_to_fahrenheit()  # Call the Celsius to Fahrenheit conversion function
    elif choice == "2":
        fahrenheit_to_celsius()  # Call the Fahrenheit to Celsius conversion function
    else: 
        print("Make sure you enter '1' or '2'")

# Start the program by calling the main function
main()
