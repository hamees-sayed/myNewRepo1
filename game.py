import random


print("Game of Stone, Paper, Scissor")
print("You get 5 chances to win.\n")


system = ["stone", "paper", "scissor"]
no_of_chances = 0
your_points = 0
computer_points = 0


while no_of_chances < 5:

    h = input("\nEnter your bet(Stone, Paper, Scissor):")
    s = random.choice(system)
    print("System's Call: ", end="")
    print(s)

    if h == s:
        computer_points += 0
        your_points += 0
        print("\nDraw!")
        print("Your Points",your_points,"and Computer scored",computer_points,"\n")
    elif (h == "stone") and (s == "paper"):
        computer_points += 1
        print("\nYou Lose!")
        print("Your points",your_points,"and Computer scored",computer_points,"\n")
    elif (h == "stone") and (s == "scissor"):
        your_points += 1
        print("\nYou Won!")
        print("Your points", your_points, "and Computer scored", computer_points,"\n")
    elif (h == "paper") and (s == "stone"):
        your_points += 1
        print("\nYou Won!")
        print("Your points", your_points, "and Computer scored", computer_points,"\n")
    elif (h == "paper") and (s == "scissor"):
        computer_points += 1
        print("\nYou Lose!")
        print("Your points", your_points, "and Computer scored", computer_points,"\n")
    elif (h == "scissor") and (s == "stone"):
        computer_points += 1
        print("\nYou Lose!")
        print("Your points", your_points, "and Computer scored", computer_points,"\n")
    elif (h == "scissor") and (s == "paper"):
        your_points += 1
        print("\nYou Won!")
        print("Your points", your_points, "and Computer scored", computer_points,"\n")
    else:
        print("Invalid Input!\nYou can only enter 'Stone', 'Paper', 'Scissor'" )
    no_of_chances += 1

    continue

while no_of_chances == 5:

    if your_points > computer_points:
        print("\nYou are the Winner!")
    el your_points < computer_points:
        print("\nYou are the Loser!")
    else:
        print("\nIt's a Tie!")

    break
