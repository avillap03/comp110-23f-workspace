"""EX01 - Chardle - A cute step toward Worldle."""

__author__ = "730621663"

# part 1 - prompting for inputs
word_chosen: str = input("Enter a 5-character word: ")
character_chosen: str = input("Enter a single character: ")

# part 4 - exiting early for invalid inputs 
if len(word_chosen) != int(5):
    print("Error: Word must contain 5 characters.")
    exit()
if len(character_chosen) != int(1):
    print("Error: Character must be a single character.")
    exit()

# part 1 continuation 
print("Searching for " + character_chosen + " in " + word_chosen)

# required varaible for part 2 - part 3
num_instances: int = 0 

# part 2 - checking indices for matches
if word_chosen[0] == character_chosen:
    print(character_chosen + " found at index 0")
    num_instances = num_instances + 1
if word_chosen[1] == character_chosen:
    print(character_chosen + " found at index 1")
    num_instances = num_instances + 1
if word_chosen[2] == character_chosen:
    print(character_chosen + " found at index 2")
    num_instances = num_instances + 1
if word_chosen[3] == character_chosen:
    print(character_chosen + " found at index 3")
    num_instances = num_instances + 1
if word_chosen[4] == character_chosen:
    print(character_chosen + " found at index 4")
    num_instances = num_instances + 1 

# part 3 - counting matching indices  
if num_instances == int(0): 
    print("No instances of " + character_chosen + " found in " + word_chosen)
if num_instances == int(1): 
    print(str(num_instances) + " instance of " + character_chosen + " found in " + word_chosen)
if num_instances > int(1): 
    print(str(num_instances) + " instances of " + character_chosen + " found in " + word_chosen)