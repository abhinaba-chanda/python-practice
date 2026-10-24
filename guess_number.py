import random

secret = random.randint(1, 100)
tries = 0
print("I picked a number between 1 and 100. Guess it!")
while True:
    guess = int(input("Your guess: "))
    tries += 1
    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")
    else:
        print(f"Correct! You got it in {tries} tries.")
        break
