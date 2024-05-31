import random
import time

attempts = 0

print("welcome to my number guessing game! ")
input("press any key to start playing ")

while True:
# ask user for input
    number1 = random.randint(0,10)
    guess = int(input("guess a random number between 0 and 10. "))
    attempts += 1

    if guess == number1:
        playAgain = input(f"correct! the secret number was indeed {number1}, and you guessed it in {attempts} attempts. play again? (yes/no) ")
        if playAgain == "yes":
            number1 = random.randint(0,10) 
            continue
        else:
            break
    elif guess > number1:
        print("try a smaller number. ")
    else:
        print("try a bigger number. ")
