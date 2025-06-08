# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR  # Add global keyword as per requirements
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR  # Add global keyword as per requirements
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Get and validate temperature
        temperature = input("Enter the temperature to convert: ")
        temperature = float(temperature)

        # Get and validate unit choice
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

        match unit:
            case "C":
                result = convert_to_fahrenheit(temperature)
                print(f"{temperature:}°C is {result}°F")
            case "F":
                result = convert_to_celsius(temperature)
                print(f"{temperature}°F is {result}°C")
            case _:
                print("Invalid unit. Please enter C or F.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()



