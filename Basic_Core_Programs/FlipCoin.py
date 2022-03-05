import random

no_Of_Flips = int(input("Enter the number of times you want to flip a coin : "))
headsCount=0
tailsCount=0
for flip in range(1,no_Of_Flips+1):
    flipResult = random.uniform(0,1)
    if flipResult < 0.5:
        print(f"It's a Tails at flip {flip}")
        tailsCount +=1
    else:
        print(f"It's a Heads at flip {flip}")
        headsCount +=1

print(f"Percentage of Heads : {(headsCount/no_Of_Flips)*100} \nPercentage of Tails : {(tailsCount/no_Of_Flips)*100}")