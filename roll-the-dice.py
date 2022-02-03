import random
roll_dice = input("type 1 to start: ")

if roll_dice == "1":
   posiblle_results = [1, 2, 3, 4, 5, 6]
   result = random.choice(posiblle_results)
   print("Result of dice rolling is : " + str(result))