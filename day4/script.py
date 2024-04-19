from random import *

print("*********Welcome to the guessing game!*******************")

name = input("\nHey what's your name: ")
print(f"\nWell {name} I've thought of a number between 1 and 100.  ")
a = input(f"\nYou have 8 tries to guess it ok? ")
if a == "ok":
    print("\nAlright lets do it")
else: 
    print("bye lol")
    exit
tries = 8
number = randint(1,100)

for i in range(tries):
    b = int(input(f"Guess the number, current try: {i+1}: "))
    if  b > number :
        print("**************************************************")
        print("\nIts big lower it <<<")
    elif b < number :
        print("**************************************************")
        print("\nIts small make it bigger it >>>")
    else:
        print("**************************************************")
        print("\nBull's eye haha! CONGRAT you guessed it!")
        break

if b != number:
    print(f"\nOh Sorry, the correct answer was {number}")