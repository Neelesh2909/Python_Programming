import math

a = int(input("Enter a value for a : "))
b = int(input("Enter a value for b : "))
c = int(input("Enter a value for c : "))

delta = ((b*b)-(4*a*c))
root_1 = round(-b+ (math.sqrt(delta))/(2*a),2)
root_2 = round(-b- (math.sqrt(delta))/(2*a),2)

print(f"The 2 Roots for the equation a*x*x + b*x +c are : ")
print(f"Root 1 of x ((-b + sqrt(delta))/(2*a)) : {root_1}")
print(f"Root 2 of x ((-b - sqrt(delta))/(2*a)) : {root_2}")