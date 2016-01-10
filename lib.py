# Nate Genter
# 1-9-16
# Liberty North Login

print("\n\n\t\t\tWelcome to Liberty North!\n\n")

login = "smalley"
password = "shroom"

name = input("What is your last name?\n")
food = input("What is your password?\n\n")

if name == login and password == food:
    print ("\nHello Mr. Smalley.  You have an appointment with Master Hawk.\n")
    print("\nPlease head to the conference room.\n\n")
else: print("Invalid login, please try again.")
          



input("\n\nPress the enter key to exit.")
