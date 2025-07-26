import random

print("Welcome to the Number Guessing Game! \n You have 5 attempts to guess the number between 1 and 50.")

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

print(f"Guess a number between {low} and {high}, Let's see if you can guess it in 5 attempts!")

num = random.randint(low, high)
chances = 5
guess = 0

while guess < chances:
    guess += 1
    user_guess = int(input(f"Attempt {guess}: Enter your guess: "))

    if user_guess == num:
        print("Congratulations! You've guessed the number correctly.")
        break

    elif guess >= chances and user_guess != num:
        print(f"Sorry, you've used all your attempts. The number was {num}.")

    elif user_guess < num:
        print("Your guess is too low. Try again.")

    elif user_guess > num:
        print("Your guess is too high. Try again.")

    else:
        print("Invalid input. Please enter a number between the specified range.")
