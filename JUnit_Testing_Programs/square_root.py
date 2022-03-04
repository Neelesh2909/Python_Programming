def sqrt(c):
    t = c
    epsilon = 1e-15
    while abs(t-c/t) > epsilon*t:
        t = (c/t + t) / 2
    return round(t,3)

c = int(input("Enter a number for which you want o find the square root : "))

if c > 0:
    print(f"The square root of {c} = {sqrt(c)}")
else:
    print("Please enter a non-negative number")
