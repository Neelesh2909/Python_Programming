def decimalToBinary(num):
        if num >= 1:
            decimalToBinary(num // 2)
            # print(num)
            print(num%2,end="")

decimal_no = int(input("Enter a number : "))
print(f"Binary representation of {decimal_no} is :")
decimalToBinary(decimal_no)

