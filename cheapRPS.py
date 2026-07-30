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


# Sieges - Konditionen
wins_against = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}

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


# Prüfen ob Spieler == CPU → Unentschieden
if playerChoice == cpuChoice:
    print("Draw!")
    exit()


# Prüfen ob wins_against[player] == CPU Spieler gewinnt
# Ansonsten CPU gewinnt
if wins_against[playerChoice] == cpuChoice:
    print("You win!")
else:
    print("You lose!")