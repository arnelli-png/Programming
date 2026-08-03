secret_number = 7 
guess = 0
attempts = 0
print("Guess the number between 1 and 10")
while guess != secret_number and attempts < 5:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Your guess is too low. Try again.")
        print(f"You have {5 - attempts} attempts left.")
    elif guess > secret_number:
        print("Your guess is too high. Try again.")
        print(f"You have {5 - attempts} attempts left.")
if guess == secret_number:
    print(f"Congratulations! You guessed the number in {attempts} attempts!")
else:
    print("Sorry, you've used all your attempts.")

