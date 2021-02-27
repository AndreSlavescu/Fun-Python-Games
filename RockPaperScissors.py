import random

youC = 0
oppC = 0
diff = youC - oppC
continuegame = True

while continuegame:
  continueplay = input("enter play to continue or stop to stop")
  if continueplay == "play":
    pass
  else:
    break
  opponent = input("input either S,P, or R: ")
  you = random.randint(0,2)

  if you == 0 and opponent == "S":
    youC += 1
  elif you == 0 and opponent == "P":
    oppC += 1
  elif you == 1 and opponent == "R":
    youC += 1
  elif you == 1 and opponent == "S":
    oppC += 1
  elif you == 2 and opponent == "P":
    youC += 1
  elif you == 2 and opponent == "R":
    oppC += 1

if diff > 0:
  print(f"you win by {diff} games")
elif diff < 0:
  print(f"you lose by {abs(diff)} games")
else:
  print(f"We're all tied up with {youC} games")
