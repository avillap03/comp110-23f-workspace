"""EX03 - Structured Wordle."""

__author__ = "730621663"


# function to check if a character is contained within a given word
def contains_char(chosen_word: str, searched_chr: str) -> bool:
    """Check if searched character is found at the chosen word."""
    assert len(searched_chr) == 1
    idx: int = 0 
    result: bool = False
    while idx < len(chosen_word):
        if chosen_word[idx] == searched_chr:
            result = True
        idx += 1
    return result


# function to create an emoji string representing the similarity between two words
def emojified(guess: str, secret: str) -> str:
    """Print emoji string that represents similarity between the guess and the secret."""
    assert len(guess) == len(secret)
    result: str = ""
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    idx: int = 0
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            result += green_box
        elif contains_char(secret, guess[idx]) is True:
            result += yellow_box
        else:
            result += white_box
        idx += 1
    return result 


# function to prompt the user for a guess of a specific length
def input_guess(exp_len: int) -> str:
    """Prompt the user for a guess of the expected length."""
    chosen_word: str = input(f"Enter a {exp_len} character word: ")
    while len(chosen_word) != exp_len:
        chosen_word = input(f"That wasn't {exp_len} chars! Try again: ")
    return chosen_word


# main function that controls the game loop - pulling together the functions
def main() -> None: 
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 1
    max_turns: int = 6
    correct_guess: bool = False
    while turn <= max_turns and not correct_guess:
        print(f"=== Turn {turn}/{max_turns} ===")
        chosen_word: str = input_guess(len(secret_word))
        print(emojified(chosen_word, secret_word))
        if secret_word == chosen_word:
            print(f"You won in {turn}/{max_turns} turns! ")
            correct_guess = True
        turn += 1   
    if not correct_guess:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()