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
else: print("\n\nLogin Failure, please exit the system.\n")

input("\n\nPress the enter key to exit.")
