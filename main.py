import random

dice1 = random.randint(0,5)
dice2 = random.randint(0,5)
dice3 = random.randint(0,5)

variable =  dice1, dice2, dice3

while dice1 != dice2 or dice2 != dice3 or dice1 != dice3:
   dice1 = random.randint(0, 5)
   dice2 = random.randint(0, 5)
   dice3 = random.randint(0, 5)
   print("Your results:")
   print(random.randint(0,5), random.randint(0,5), random.randint(0,5))
print("You won the game, your numbers:", dice1, dice2, dice3)

