from getpass import getpass as input
print ("Welcome To The Epic 🪨  📄 ✂️  Battle Simulator")
print ()
print ("Now both players should select your move (pick between R-Rock, P-Paper or S-Scissors)")
print ()
player_1 = input()
player_2 = input()
print ()
print ("Player 1 picked", player_1)
print ("Player 2 picked", player_2)
print()
if player_1 == "r" or player_1 == "R":
  if player_2 == "r" or player_2 == "R":
    print ("Both players went for a rock fest. It's a tie")
  elif player_2 == "p" or player_2 == "P":
    print ("Paper covers rock in defeat. Player 2 wins")
  elif player_2 == "s" or player_2 == "S":
    print ("Rock crushes scissors to smithereens. Player 1 wins")
  else:
    print ("Pick right option")
elif player_1 == "p" or player_1 == "P":
  if player_2 == "r" or player_2 == "R":
    print ("Paper covers rock in defeat. Player 1 wins")
  elif player_2 == "p" or player_2 == "P":
    print ("Both players got a paper cut. It's a tie")
  elif player_2 == "s" or player_2 == "S":
    print ("Scissors tears paper to shreds. Player 2 wins")
  else:
    print ("Pick right option")
elif player_1 == "s" or player_1 == "S":
  if player_2 == "r" or player_2 == "R":
    print ("Rock crushes scissors to smithereens. Player 2 wins")
  elif player_2 == "p" or player_2 == "P":
    print ("Paper covers rock in defeat. Player 2 wins")
  elif player_2 == "s" or player_2 == "S":
    print ("The scissors fight got bloody for both players. It's a tie")
  else:
    print ("Pick right option")
else:
  print ("Pick right option")