"""Dictionaries practice."""

# Create a new dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("Create my new dictionary:")
print(ice_cream)

# Adding a key, value pair to a dictionary
ice_cream["mint"] = 3
print("Added mint to dictionary:")
print(ice_cream)

# Removing a key, value pair
ice_cream.pop("mint")
print("Removied mint:")
print(ice_cream)

# Accessing a value
print({f"There are {ice_cream['chocolate']} orders of chocolate"})

# Updating a value
ice_cream["vanilla"] = 10
print("After updating vanilla:")
print(ice_cream)

# Print the length
print({f"There are {len(ice_cream)} key-value pairs"})

# Checking if values are in a dictionary
if "mint" in ice_cream:
    print(ice_cream["mint"])
else: 
    print("No orders of mint.")

# Loop through dictionary
for key in ice_cream:
    # print out <flavor> has <num_order> orders
    print(f"{key} has {ice_cream[key]} orders.")