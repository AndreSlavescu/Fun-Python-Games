import random

youC = 0 #my points
oppC = 0 #opponent points
gameC = 0 #number of games played
continuegame = True

while continuegame:
  continueplay = input("Please enter 'Play' if you want to play the game, or 'Stop' to stop: ")
  while continueplay not in ["Stop", "stop", "Play", "play"]:
    print("Wrong input, please enter either 'Play' or 'Stop'")
    continueplay = input("Please enter 'Play' if you want to play the game, or 'Stop' to stop: ")
  if continueplay == "play" or continueplay == "Play":
    pass
  elif continueplay == "stop" or continueplay == "Stop":
    break

  gameC += 1
  print(f"Game {gameC} Rock, Paper, Scissors - Play!")
  opponent = input("Choose your weapon: R for Rock, P for Paper, or S for Scissors: ")
  while opponent not in ["S", "s", "P", "p", "R", "r"]:
    print("Wrong input, please enter either 'R', 'P', or 'S'")
    opponent = input("Choose your weapon: R for Rock, P for Paper, or S for Scissors: ")
  you = random.randint(0,2)
  
  if you == 0:
    print("I chose: R")
  elif you == 1:
    print("I chose: P")
  elif you == 2:
    print("I chose: S")
  print(f"You chose: {opponent}")

  if you == 0 and (opponent == "S" or opponent == "s"):
    youC += 1
  elif you == 0 and (opponent == "P" or opponent == "p"):
    oppC += 1
  elif you == 1 and (opponent == "R" or opponent == "r"):
    youC += 1
  elif you == 1 and (opponent == "S" or opponent == "s"):
    oppC += 1
  elif you == 2 and (opponent == "P" or opponent == "p"):
    youC += 1
  elif you == 2 and (opponent == "R" or opponent == "r"):
    oppC += 1
   
diff = youC - oppC

print("~~~Final Scores~~~")
print(f"Your Score: {oppC},  My Score: {youC}")

if diff > 0:
  print(f"Congratulations! You outplayed me by {diff} games!")
elif diff < 0:
  print(f"You're a great opponent! I beat you by only {abs(diff)} games.")
else:
  print(f"We're all tied up with {youC} games each. Let's play again soon.")
