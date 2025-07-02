import random, time

time.sleep(1)
print("Game by br.17.17 01/07/2025")
time.sleep(2)


choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
player = input("Please choose rock, paper or scissors: ")

if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
    print("You Win!")
else:
    print("You Lose 🙁")