def calc_monthlyPayment(P,Y,R):
    n = 12 * Y
    r = R / (12 * 100)
    payment = (P * r) / (1 - ((1 + r) ** (-n)))
    return round(payment,2)

principal = int(input("Enter the principal amount : "))
rate = int(input("Enter the rate of interest : "))
year = int(input("Enter the number of year : "))

print(f"You have to make a monthly payment of Rs {calc_monthlyPayment(principal,year,rate)} for {year} years to pay off Rs {principal} loan amount"
      f" at interest {rate}% compounded monthly")