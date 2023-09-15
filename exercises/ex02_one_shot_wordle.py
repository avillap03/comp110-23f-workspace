"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730621663"

# part 1 - establishing a secret word and prompting for a guess
secret_word: str = ("python")
guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

# part 1 - prompting for a guess of the correct lenght
while len(guess) != len(secret_word):
    new_guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")
    guess = new_guess

# part 2 - defining name constants for emojis
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

# part 2 - variables - keeping track of word index and resulting emoji
idx: int = 0 
result: str = ""

# part 2 - checking indices for correct matches - printing emojis 
while idx < len(secret_word):
    if guess[idx] == secret_word[idx]:
        result = result + green_box
    # part 3 - checking for correct characters at incorrect positions
    else:
        # part 3 - variabls - cheking if character is part of secret word
        guessed_character = False
        alt_idx: int = 0
        while not guessed_character and alt_idx < len(secret_word):
            if guess[idx] == secret_word[alt_idx]:
                guessed_character = True
            alt_idx = alt_idx + 1
        # part 3 - correct character at incorrect index
        if guessed_character:
            result = result + yellow_box
        # part 3 - incorrect character 
        else: 
            result = result + white_box
    idx = idx + 1 
print(result)

# part 1 - checking if guess is correct
if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")