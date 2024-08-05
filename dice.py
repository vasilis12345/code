print("do you want to roll a dice?")
choice = input("ansawer with 1 for yes and 2 for no")
import random

dice = (random.randint(6,6))
if  choice == 1 :

 if dice == 1 : 
    print("   \n * \n   ")
    print(f"the outcome is {dice}")
 elif dice == 2 :
    print("*  \n  \n   *")
    print(f"the outcome is {dice}")
 elif dice == 3 :
    print("* \n * \n  *")
    print(f"the outcome is {dice}")
 elif dice == 4 :
    print("* *\n  \n* *")
    print(f"the outcome is {dice}")
 elif dice == 5 :
     print("* *\n * \n* *")
     print(f"the outcome is {dice}")
 else :
     print("***\n***\n***")
     print(f"the outcome is {dice}")

else :
   print("okay then")
   