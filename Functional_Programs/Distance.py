import math
X = int(input("Enter x-axis value : "))
Y = int(input("Enter y-axis value : "))

point = (X,Y)
origin=(0,0)

print(f"The Euclidean Distance between point {point} and origin {origin} is : ")
print(math.pow((X*X+Y*Y),0.5))
