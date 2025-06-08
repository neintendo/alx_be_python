FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = None

while not isinstance(temperature, float):
    #type input check
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        temperature = None

temp_check = False
while temp_check == False:
    scale = None

    while not isinstance(scale, str):
        try:
            scale = str.upper(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))
        except ValueError:
            print("Invalid scale. Please enter C or F.")
            scale = None

    match scale:
        case "C":
            result = convert_to_fahrenheit(temperature)
            print("{0}°C is {1}°F".format(temperature, result))
            temp_check = True
        case "F":
            result = convert_to_celsius(temperature)
            print("{0}°F is {1}°C".format(temperature, result))
            temp_check = True
        case _:
            print("Invalid scale. Please enter C or F.")

