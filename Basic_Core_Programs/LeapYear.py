year = int(input("Enter a year : "))
if len(str(year)) == 4:
    if year%400 == 0 or (year%4 == 0 and year%100 != 0):
        print("Leap Year")
    else:
        print("Non Leap Year")
else:
    print("Your year should be a 4 digit number")

#Single line if-else to determine the year is leap or not.

# leapOrNot = "Leap Year" if year%400==0 else "Leap Year" if year%4==0 and year%100!=0 else "Non Leap Year"
# print(leapOrNot)