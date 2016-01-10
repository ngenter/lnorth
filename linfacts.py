# Liberty North fact calculator
# Nate Genter
# 1/9/16

print("\t\t\nWelcome to Liberty Norths fact calculator.")
print("\nThe object is to get some input from our employees, and calculate")
print("certain facts...")
print("\nLets begin.")



name = input("\nWhat is your full name?")
weight = int(input("\nHow many pounds do you weigh?"))
smoke = int(input("\nHow many joints a day do you smoke?"))
eggs = int(input("\nHow many eggs a day do you eat?"))
icp = int(input("\nHow many ICP albums do you own?\n\n"))

stones = int(weight / 6)
gpd = int(smoke * 1.25)
wpy = int(gpd * 7 * 52 / 28)
egp = int(eggs * 7 * 52 / 12)
weed = int(wpy * 200)
input("\nPress the enter key to see your results!\n")

print("\nYour name in all capitalized letters is...")
print(name.upper())

print("\nYour weight on the moon is...")
print(stones, "pounds")

print("\nYou smoke", gpd, "grams a day")
print("That is", wpy, "ounces per year.")
print("That is an average of", weed, "Dollars a year. (At $200 an ounce)")

print("\nYou eat", egp, "dozen eggs per year.")

print("\nYou own", icp, "too many ICP albums.")

print("\n\n\t\tThank you for supporting Liberty North!")

input("\n\nPress the enter key to exit.\n")
