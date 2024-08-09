import random
while True:
    correct_guess = random.randint(1, 10)
    attempt = 0
    while attempt<3:
        attempt = attempt+1
        print(f"This is your {attempt} Attempt.")
        user_guess = int(input("Guess the Number from 1 to 10: "))
        if user_guess == correct_guess:
            print("You guessed it Right :) ")
            break
        elif user_guess>correct_guess:
            print("You guessed higher.")
        elif user_guess<correct_guess:
            print("You guessed lower.")
        else:
            print("Incorrect Guessing!")