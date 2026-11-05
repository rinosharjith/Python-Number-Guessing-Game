# SECTION 1: Welcome message

print("================================")
print("   NUMBER GUESSING GAME")
print("================================")

# SECTION 2: Setting variables

secret_number = 13
max_attempts = 5

# SECTION 3: Start the game

while True:

    attempts = 0
    guessed = False

    print("\nI have chosen a number between 1 and 20.")
    print("You have 5 attempts to guess it!")

    # SECTION 4: Get and check the guess

    while attempts < max_attempts:

        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess == secret_number:
            print("Congratulations! You guessed it right!")
            print("Number of attempts:", attempts)
            guessed = True
            break
