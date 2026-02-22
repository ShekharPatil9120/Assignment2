# ---------------------------------------------------
# Question 16: Number Guessing Game
# Basic version with difficulty (simple implementation)
# ---------------------------------------------------

import random

while True:
    print("\nSelect Difficulty")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter choice: ")

    # Setting range based on difficulty
    if choice == '1':
        number = random.randint(1, 50)
    elif choice == '2':
        number = random.randint(1, 100)
    elif choice == '3':
        number = random.randint(1, 1000)
    else:
        print("Invalid choice")
        continue

    attempts = 7

    print("Guess the number")

    # Game loop
    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
            attempts -= 1

            if guess == number:
                print("You guessed correctly!")
                break
            elif guess > number:
                print("Too high")
            else:
                print("Too low")

        except:
            print("Enter a valid number")

    if attempts == 0:
        print("Game over! Number was:", number)

    play = input("Play again? (y/n): ")
    if play != 'y':
        break