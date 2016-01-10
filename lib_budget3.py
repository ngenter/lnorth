# Liberty Budget Calculator
# Nate Genter
# 1-9-16

name = "smalley"
password = "shroom"

print("\t\t\n\nWelcome to Liberty North.\n\n")
print("\nPlease login to continue.")

login = input("\nWhat is your last name?")
pas = input("\nWhat is your password?")

if login == name and pas == password:
    print("\t\t\nLogin Sucessfull!")
    print("\t\t\n\nWelcome to the Liberty North Budget Calculator!")
    print("\nThe object is to total monthly spending.\n")
    print("Please enter the requested, monthly costs.\n\n")

    employees = int(input("Employees Salaries: "))
    weed = int(input("Weed for Employees: "))
    electric = int(input("Electric Bill: "))
    hookers = int(input("Hookers :"))
    grizzly = int(input("Grizzly Wintergreen longcut: "))
    bar = int(input("Bar Tab: "))
    fuel = int(input("Fuel Costs: "))

    total = employees + weed + electric + hookers + grizzly + bar + fuel

    print("\nGrand Total is:", total)

else: print("n\nLogin Failure, please exit the system.\n")
    

if employees <= 500:
        print("\nYour employee fund looks low, I hope you are hiring Mexicans.")
else: print("\nThat seems like a sufficient Employee fund.")
if weed <=100:
        print("\nBruno gonna smoke you out.")
else: print("\nThat's enough smoke to be the life of the party... for a day.")
if electric >= 500:
        print("\nBetter cut back on the grow lights.")
else: print("\nYou running a generator or something?")
if grizzly <= 50:
        print("\nYou aren't going to make it through the month.")
else: print("\nGrizzly, it's not just for breakfast anymore.")
if total <= 1000:
        print("\nYour budget is too low")
        print("\nYou are a cheap ass.")
        print("\nInvest more in your business for success.")
else: print("\nYour bussiness looks sufficiently funded.")

        



input("\n\nPress the enter key to exit.")
