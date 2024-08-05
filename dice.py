print("do you want to roll a dice?")

import random

dice = (random.randint(6,6))

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

