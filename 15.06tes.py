import random

secret_number = random.randint(1, 20)
attempts = 0

print("I am thinking of a number between 1 and 20.")

while True:
    guess = int(input("Take a Guess? "))
    attempts += 1

    if guess < secret_number:
        print("Your Guess is too low.")
    elif guess > secret_number:
        print("Your Guess is too high.")
    else:
        print(f"Well Done! You have Guessed my Number in {attempts} attempts. You Won!")
        break
    