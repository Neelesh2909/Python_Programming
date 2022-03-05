import random

def generate_distinct_coupons(num):
    coupon_list=[]
    number_of_coupons=0
    while len(coupon_list)!=num:
        random_coupon_no = random.randint(1111,5555)
        if random_coupon_no not in coupon_list:
            number_of_coupons+=1
            coupon_list.append(random_coupon_no)
    return coupon_list,number_of_coupons


distinct_number = int(input("Enter the number of coupons required :"))
coupon_number = int(input("Enter your coupon number : "))


couponList,coupon_count = generate_distinct_coupons(distinct_number)
print(f"Total number of coupons generated : {coupon_count}")
print("Lucky coupons who won are : ")
for coupon in couponList:
    print(coupon,end=" ")

if coupon_number not in couponList:
    print("\nSorry your coupon number is not in lucky list, Better Luck next time!")
else:
    print("\nCongratulation, you are amongst the lucky winners")
