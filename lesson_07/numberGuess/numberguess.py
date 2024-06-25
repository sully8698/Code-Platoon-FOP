user_guess = int(input("Enter the integer for the player to guess. "))
print("Enter your guess.")
guess = (int(input()))
count = 1

if user_guess == guess:
    print(f'You guessed it in {count} try.')
else:
    while guess != user_guess:
        if guess > user_guess:
            print("Too high - try again")
        elif guess < user_guess:
            print("Too low - try again")
        count += 1
        guess = (int(input()))
    print(f'You guessed it in {count} tries.')
