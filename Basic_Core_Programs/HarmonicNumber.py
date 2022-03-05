def nthHarmonicNumber(num):
    harmonic=1.00
    for number in range(2,harmonicValue+1):
        harmonic += 1/number
    return harmonic

harmonicValue = int(input("Enter a number : "))

if harmonicValue > 0 :
    print(f"The {harmonicValue}th Harmonic Value is : {round(nthHarmonicNumber(harmonicValue),2)}")
else:
    print("The number should be greater than zero")