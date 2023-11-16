"""Dictonaries practice."""

# Create a new dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Create my dictionary")
print(ice_cream)

# Adding a key, value pair to a dictionary
ice_cream["mint"] = 3
print("Add mint to dictionary")
print(ice_cream)

# Removing a key, value pair from a dictionary
ice_cream.pop("mint")
print("Remove mint:")
print(ice_cream)

# Accessing a value
print(f"There are {ice_cream['chocolate']} orders of chocolate")

# Updating a vlaue
ice_cream["vanilla"] = 10
# ice_cream ["vanilla"] += 2
print("After updating vanilla:")
print(ice_cream)

# Print the lenght 
print(f"There are {len(ice_cream)} key-value pairs")

# Checking if keys are in a dictionary 
print("Chocolate in dictionary?")
print("Chocolate" in ice_cream)
print("Mint in dictionary?")
print("Mint" in ice_cream)

# Using "in" in a conditional 
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no or ders of mint")

for flavor in ice_cream:
    print(f"{flavor} has {ice_cream[flavor]} orders")