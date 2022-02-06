import random
import shapes 
roll_dice = input("type 1 to start: ")

if roll_dice == "1":
   posiblle_results = shapes.stages
   result = random.choice(posiblle_results)
   print("Result of dice rolling is : " + str(result))