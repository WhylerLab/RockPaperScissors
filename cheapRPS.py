import random

wins_against = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock"
}


# Spieler gibt seine Wahl ein
playerChoice = str(input("rock, paper or scisoors? Choose: "))


# CPU wählt zufällig
cpuOptions = ("rock", "paper", "scissors")
cpuChoice = random.choice(cpuOptions)


# Beide Wahlen ausgeben
print(playerChoice)
print(cpuChoice)


# Prüfen ob Spieler == CPU → Unentschieden
if playerChoice == cpuChoice:
    print("Unentschieden!")
    exit()


# Prüfen ob wins_against[player] == CPU Spieler gewinnt
# Ansonsten CPU gewinnt
if wins_against[playerChoice] == cpuChoice:
    print("Du hast gewonnen!")
else:
    print("Du hast verloren!")