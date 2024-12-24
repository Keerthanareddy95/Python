import random

def roll_dice():
    #Simulates rolling a dice and returns a random value between 1 to 6
    return random.randint(1,6)

def main():
    while True:
        user_input = input("Roll the dice? (yes/no): ").strip().lower()
        if user_input == "yes":
            dice_value = roll_dice()
            print(f"You rolled: {dice_value}")
        elif user_input == "no":
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
