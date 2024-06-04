print("Lets play a 1game of rock paper scissors!! \nYou start\n")
print("quick guide \nto choose you type 1 for rock 2 for paper 3 for scissors\nyou need to reach a score of 3 to win\n")

point_player = 0
point_cpu = 0
round = 0
asked = 0


while asked == 0 :
  move_player = input("now choose")
 
  move_player =int(int(move_player))
  
asked + 1

while point_player or point_cpu < 3 :
 
 import random
 move_cpu=random.randint(1,3)
 
 print(f"I throw {move_cpu}")
if move_player == move_cpu :
 
 print("again")
elif move_cpu == 1 and move_player == 2 or move_player == 1 and move_cpu == 3 or move_cpu == 2 and move_player == 3 :
   print("you won")


