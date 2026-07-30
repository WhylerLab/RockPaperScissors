import random


# Hand Grafiken
fistHand = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

openHand = ("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")

fingerHand = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


hand_graphics = {
    "rock": fistHand,
    "paper": openHand,
    "scissors": fingerHand
}


# Spieler gibt seine Wahl ein
playerChoice = str(input("rock, paper or scisoors? Choose: "))


# CPU wählt zufällig
cpuOptions = ("rock", "paper", "scissors")
cpuChoice = random.choice(cpuOptions)


# Beide Wahlen ausgeben
print(hand_graphics[playerChoice])
print("versus")
print(hand_graphics[cpuChoice])


# IfEsle Bedingung
if playerChoice == "rock" and cpuChoice == "scissors":
    print("You win!")
elif playerChoice == "scissors" and cpuChoice == "paper":
    print("You win!")
elif playerChoice == "paper" and cpuChoice == "rock":
    print("You win!")
elif playerChoice == cpuChoice:
    print("Draw!")
else:
    print("You lose!")