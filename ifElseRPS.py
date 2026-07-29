import random


# Spieler gibt seine Wahl ein
playerChoice = str(input("rock, paper or scisoors? Choose: "))


# CPU wählt zufällig
cpuOptions = ("rock", "paper", "scissors")
cpuChoice = random.choice(cpuOptions)


# Beide Wahlen ausgeben
print(playerChoice)
print(cpuChoice)


# IfEsle Bedingung
if playerChoice == "rock" and cpuChoice == "scissors":
    print("Du hast gewonnen!")
elif playerChoice == "scissors" and cpuChoice == "paper":
    print("Du hast gewonnen!")
elif playerChoice == "paper" and cpuChoice == "rock":
    print("Du hast gewonnen!")
else:
    print("Du hast verloren!")