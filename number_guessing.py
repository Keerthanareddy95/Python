import random

def number_guessing_game():
    print("Welcome to number guessing game. You'll have unlimited number of attempts to guess the correct number!")
    print("I'm thinkinh of a number between 1 and 100")

    number_to_be_guessed = random.randint(1,10)
    attempts = 0
   
    while True:
        try:
            user_guess = int(input("enter your guess: "))
            attempts += 1
            if user_guess > number_to_be_guessed:
                print("Too high! Try again")
            elif user_guess < number_to_be_guessed:
                print("Too low! Try again")
            else:
                print(f"Congratulations! You guessed the number {number_to_be_guessed} correctly in {attempts} attempts!!")
                break
        
        except ValueError as e:
            print("Enter correct number")

if __name__ == "__main__":
    number_guessing_game()


