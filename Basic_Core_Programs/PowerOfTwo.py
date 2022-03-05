'''Function to compute the 2^N'''
# def computePower(num):
#     return 2**num

powerValue = int(input("Please enter a number in range (0-30): "))
if powerValue >= 0 and powerValue < 31:
    for power in range(powerValue + 1):
        # result= computePower(power)
        result= lambda x,y: x**y
        print(f"The Power of 2^{power} is : {result(2,power)}")
else:
    print("Please enter a valid number in the range (0-30)")


