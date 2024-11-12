import random

def generate_number():
    return str(random.randint(1000, 9999))

def bulls_and_cows(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows

def game(secret, attempts=0):
    guess = input("Enter your guess: ")
    attempts += 1
    bulls, cows = bulls_and_cows(secret, guess)
    print(f"Bulls: {bulls}, Cows: {cows}")
    if bulls == 4:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
    else:
        game(secret, attempts)

if __name__ == "__main__":
    secret_number = generate_number()
    print("Welcome to Bulls and Cows!")
    game(secret_number)
