
import random

stake = int(input("Enter the Stake"))
goal = int(input("Enter your goal"))
trials = int(input("Enter the trials"))

# Run trialCount experiments that start with stake and terminate on
# 0 or goal.
print("++++++++++")
bets = 0
wins = 0
for t in range(trials):
    # Run one experiment.
    cash = stake
    while cash > 0 and cash < goal:
        # Simulate one bet.
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1

print(str(100 * wins/trials) + '% wins')
print('Avg # bets: ' + str(bets/trials))