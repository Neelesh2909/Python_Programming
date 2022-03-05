def prime_factor(num):
    prime_fact = []
    divisor=2
    while divisor <= num:
        if num % divisor == 0:
            prime_fact.append(divisor)
            num=num/divisor
        else:
            divisor+=1
    return  prime_fact

number = int(input("Enter a number : "))
print(prime_factor(number))
