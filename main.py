import random


def log_guesses(guess):
    LOG_PATH = "guesses.log"

    with open(LOG_PATH, "a") as f:
        f.write(f"Your guess: {guess}\n")


def compare_guess(guess, random_number):
    if guess == random_number:
        return "Winner Winner!"
    elif guess < random_number:
        return "Too low!"
    elif guess > random_number:
        return "Too high!"


def get_guess():
    MIN_GUESS = 1
    MAX_GUESS = 10

    while True:
        try:
            guess = int(input("Enter a number between 1 - 10: "))
            if guess < MIN_GUESS or guess > MAX_GUESS:
                print("Invalid input. Must be a number between 1 - 10")
            else:
                log_guesses(guess)
                return guess
        except ValueError:
            print("Invalid input. Must be a number between 1 - 10")


def get_random_number():
    return random.randint(1, 10)


def main():
    random_number = get_random_number()
    LOG_PATH = "guesses.log"

    while True:
        guess = get_guess()
        if compare_guess(guess, random_number) == "Winner Winner!":
            print("Winner winner!")
            break
        elif compare_guess(guess, random_number) == "Too low!":
            print("Too low!")
        elif compare_guess(guess, random_number) == "Too high!":
            print("Too high!")
    print(f"See your guesses: {LOG_PATH}")


if __name__ == "__main__":
    main()
