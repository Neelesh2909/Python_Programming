def decimal_to_binary(num):
    binary_str =""
    while num > 0:
        remainder = num%2
        num = num//2
        binary_str += str(remainder)
    binary_str = binary_str[::-1]
    return binary_str



def binary_to_decimal(binary_str):
    decimal_no =0
    n= int(len(binary_str))
    for i in range(0,n):
        decimal_no += int(binary_str[i]) * 2**(n-i-1)
    return decimal_no



def swap(number):
    return number[4:8] + number[0:4]


def main():
    decimal_no = int(input("Enter a decimal number : "))
    binary_number = decimal_to_binary(decimal_no)
    swapped_binary_no = swap(binary_number)
    swaped_decimal_no = binary_to_decimal(swapped_binary_no)
    print(f"The binary representation of {decimal_no} is {binary_number}")
    print(f"The swapped binary number is {swapped_binary_no}")
    print(f"The converted New Decimal number is {swaped_decimal_no}")

if __name__ == "__main__":
    main()