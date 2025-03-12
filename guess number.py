import random

number = random.randint(1, 20)
max_attempts = 5

print("Guess a number between 1 and 20:")

for attempt in range(1, max_attempts + 1):
    guess = int(input(f"Attempt {attempt}/{max_attempts}: "))

    if guess < 1 or guess > 20:
        print("Enter a number between 1 and 20 only!")
        continue

    if guess == number:
        print("You guessed it!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

if guess != number:
    print(f"Game over!")
