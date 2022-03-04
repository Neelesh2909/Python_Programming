def convert_ToFahrenheit(celsius):
    print(f"Temperature in Fahrenheit is {round((celsius*9)/5 + 32,2)} degree F")

def convert_ToCelsius(fahrenheit):
    print(f"Temperature in Celsius is {round((fahrenheit - 32) * 5/9,2)} degree C")
    return


print("TEMPERATURE CONVERTION :")
temp_conversion = input("Press 'C' if you want to convert Celsius to Fahrenheit,Press 'F' if you want to convert Fahrenheit to Celsius : ")
if temp_conversion.upper() == 'C':
    temp_celsius = int(input("Enter the temperature in Celsius : "))
    convert_ToFahrenheit(temp_celsius)
elif temp_conversion.upper() == 'F':
    temp_fahrenheit = int(input("Enter the temperature in Fahrenheit : "))
    convert_ToCelsius(temp_fahrenheit)
else:
    print("Invalid Input. Please press either F or C to proceed for temperature conversion")