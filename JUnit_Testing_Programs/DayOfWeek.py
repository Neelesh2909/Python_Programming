def dayOfWeek(d,m,y):
    y0 = y - (14 - m) / 12
    x = y0 + y0//4 - y0//100 + y0//400
    m0 = m + 12 *((14-m) /12) -2
    d0 = (d + x + (31*m0) /12)%7
    return int(d0)


print("Please follow DD/MM/YY format here :")
day = int(input("Enter the day : "))
month = int(input("Enter the month :"))
year = int(input("Enter the year :"))

day_of_week = dayOfWeek(day,month,year)

if day_of_week==0:
    print(f"It's Sunday on {day}/{month}/{year}")
elif day_of_week==1:
    print(f"It's Monday on {day}/{month}/{year}")
elif day_of_week==2:
    print(f"It's Tuesday on {day}/{month}/{year}")
elif day_of_week==3:
    print(f"It's Wednesday on {day}/{month}/{year}")
elif day_of_week==4:
    print(f"It's Thursday on {day}/{month}/{year}")
elif day_of_week==5:
    print(f"It's Friday on {day}/{month}/{year}")
elif day_of_week==6:
    print(f"It's Saturday on {day}/{month}/{year}")
