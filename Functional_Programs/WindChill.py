def compute_WindChills(temp,wind_speed):
    wind_chill = 35.74+0.6215*temp+(0.4275*temp+35.75)*(wind_speed**0.16)
    return round(wind_chill,2)

def main():
    temperature = int(input("Enter the temperature : "))
    speed = int(input("Enter the speed : "))

    if abs(temperature) >50 or speed > 120 or speed <3:
        print("Please check the values for temperature(-50 to 50) and wind_speed(3 to 120) are in the specified range")
    else:
        print(compute_WindChills(temperature,speed))

if __name__ == "__main__":
    main()