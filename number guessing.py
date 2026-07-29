import random

secretnum = random.randint(1, 100)
attempts = 1

while True:
    try:
        guess = int(input("Guess a number (1-100): "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    if guess < secretnum:
        print("Too low!")
    elif guess > secretnum:
        print("Too high!")
    else:
        print(f"You got it in {attempts} attempts!")
        break
    attempts += 1
