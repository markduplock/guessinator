import random

def compare_guess(guess, random_number):
    if guess == random_number:
        return "Winner!"
    elif guess < random_number:
        return "Too low!"
    elif guess > random_number:
        return "Too high!"
    else:
        return "Something went wrong!"

def get_guess():
    MIN_GUESS = 1
    MAX_GUESS = 10

    while True:
        try:
            guess = int(input("Enter a number between 1 - 10: "))
            if guess < MIN_GUESS or guess > MAX_GUESS:
                print("Invalid input. Must be a number between 1 - 10")
            else:
                return guess
        except ValueError:
            print("Invalid input. Must be a number between 1 - 10")

def get_random_number():
    return random.randint(1, 10)

def main():
    random_number = get_random_number()

    while True:
        guess = get_guess()
        result = compare_guess(guess, random_number)

        if result == "Winner!":
            print("Winner!")
            break
        elif result == "Too low!":
            print("Too low!")
        elif result == "Too high!":
            print("Too high!")
        elif result == "Some went wrong!":
            print("Something went wrong!")
            break

if __name__ == "__main__":
    main()
