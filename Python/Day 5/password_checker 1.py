print("Welcome to your account! Please enter the password to access your account.")
password = ""
attempts = 0
while password != "RoooBik" and attempts < 3:
    password = input("Enter the password: ")
    attempts += 1
    if password != "RoooBik" and attempts < 3:
        print(f"Wrong password! Attempts left: {3 - attempts}")
if password == "RoooBik":
    print("Access granted!")
else:
    print("You're blocked!")
