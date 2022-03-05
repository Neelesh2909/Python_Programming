import random

def gamble(stake,goal,n_times):
    wins =0
    for i in range(n_times):
        cash = stake
        while cash > 0 and cash < goal:
            result = random.randint(0,1)
            if result==1:
                cash +=1
            else:
                cash -=1
        if(cash==goal):
            wins +=1
    return wins


stake = int(input("Enter the stake : "))
goal = int(input("Enter the goal : "))
no_of_trials = int(input("Enter the no of times : "))

no_of_wins= gamble(stake,goal,no_of_trials)
# print(no_of_wins)
print(f"User Won {no_of_wins} times out of {no_of_trials}")
print(f"Win Percentage : {round(no_of_wins*100/no_of_trials),2} | Loss Percentage : {(no_of_trials-no_of_wins)*100/no_of_trials}")



