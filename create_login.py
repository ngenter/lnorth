# Create your own login for Liberty North
# Nate Genter
# 1-9-16

print("\n\t\tWelcome to Liberty North!")
print("\nAs a new employee, we need you to take a few minutes,")
print("and create a username and password.\n\n")

login = input("Please enter your username: ")
password = input("Please enter your password: \n\n")

print("Thank you, please login to verify your account has been created successfully.")


a = input("\tUsername: ")
b = input("\tPassword: ")

if login == a and password == b:
    print("\nCongratulations!  Your account has been verified.")
    print("Welcome, from us here at 'Liberty North'.")
else:
    print("\nLogin unsuccessfull.  Please try again.")
    
input("\nPress the enter key to exit.")
