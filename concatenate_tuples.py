# concatenate two tuples
chest = ("gold", "gems")
print("You find a chest. it contains:")
print(chest)

print("You add the contents of the chest to your inventory.")
inventory = ()
inventory += chest
print("your inventory is now:")
print(inventory)

input("\n\nPress the enter key to exit.")
