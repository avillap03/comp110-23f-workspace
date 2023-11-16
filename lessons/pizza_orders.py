"""Instancing a Class."""


# import the class
# from <file_name>.<module_name> import <class_name>
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) # constructor

# access/set/update attribute values
# my_pizza.size = "large"
# my_pizza.toppings = 10
# my_pizza.gluten_free = True
my_pizza.toppings += 2

print("Size: ")
print(my_pizza.size)
print(my_pizza.toppings)

# print("my_pizza:")
# print(my_pizza)

# print("Pizza class:")
# print(Pizza)

# Make sals_pizza size medium, 5 toppings, NOT GF
sals_pizza: Pizza = Pizza("medium", 5, False)
print(sals_pizza.size)

def price(inp_pizza: Pizza) -> float:
    """Compute the price of a pizza"""
    if inp_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += .75 * inp_pizza.toppings
    if inp_pizza.gluten_free:
        cost += cost
    return cost

# Calling function
print(price(my_pizza))
print(price(sals_pizza))


my_pizza.add_toppings(3)
print(my_pizza.toppings)
print(my_pizza.price())

my_second_pizza: Pizza = my_pizza.add_toppings_new_order[2]
