"""Program that loops until correct number is guessed"""

from random import randint
secret_number: int = randint(1,10) 
guess: int = int(input ("Guess a nuber between 1 and 10: "))
number_of_tries: int = 0
max_tries: int = 3

while (guess != secret_number) and (number_of_tries < max_tries - 1):
    print("Wrong!")
    if (guess < 1) or (guess > 10):
         print("That is not between 1 and 10")
    # if guess is to low, tell them
    if guess < secret_number:
          print("Too low!")
    # if guess is to high, tell them 
    else:
          print("Too high!")
    # ask for a different guess
    guess = int(input ("Guess again: "))
    number_of_tries += 1
# if I have reached this point, guess == secret number 
if guess == secret_number:
     print("You guessed correctly!")
else: 
     print("You lose. :()")
