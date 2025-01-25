money = 1000
import random

print("Wanna play a game of slots?")
print("Balance =", money)

roll = int(input("Do you want to roll? (type 1 for yes or 2 for no): "))
while money > 0 and roll == 1:
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    number3 = random.randint(1, 10)
    
    print(number1, "|", number2, "|", number3)
    
    if number1 == number2 and number1 == number3:
        print("You won!")
        money += 25
    else:
        print("You lost!")
        money -= 25
        print("Balance =", money)
    
    if money <= 0:
        print("You're out of money. Game over!")
        break
    
    roll = int(input("Do you want to re-roll? (type 1 for yes or 2 for no): "))

if money > 0:
    print("Goodbye!")


