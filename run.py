import random  # Generates random items from sequences, and shuffle lists.
import os   # Interact with the operating system.
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)  # Initialize colorama for color support

# ASCII art generated from Patorjk
# https://www.digitalocean.com/community/tutorials/python-raw-string


def title_name():
    """
    Function to print the game title in green ASCII art.

    This function uses the colorama library to print the title in green color.
    The ASCII title is centered by adding spaces at the start of each line..
    """
    print(Fore.LIGHTYELLOW_EX + r"""
        ___  ___             _                ___  ___ _             _ 
        |  \/  |            | |               |  \/  |(_)           | |
        | .  . |  __ _  ___ | |_   ___  _ __  | .  . | _  _ __    __| |
        | |\/| | / _` |/ __|| __| / _ \| '__| | |\/| || || '_ \  / _` |
        | |  | || (_| |\__ \| |_ |  __/| |    | |  | || || | | || (_| |
        \_|  |_/ \__,_||___/ \__| \___||_|    \_|  |_/|_||_| |_| \__,_|

""" + Fore.RESET)
    print("           =====================================================\n")


def display_rules():
    """
    Function to display the game rules.
    """
    print(Fore.LIGHTRED_EX + "▞▞▞▞▞  🆁 🆄 🅻 🅴 🆂 ▝▞▞▞▞▞\n" + Fore.RESET)
    print("1. Guess the random 5-digit number within the difficulty level.\n")
    print("2. Choose a number between 10,000 and 99,999.\n")
    print("3. After each guess, the computer shows:")
    print(" - Correct digits in the correct positions.")
    print(" - 'X' for incorrect digits.\n")
    print("4. Feedback is given after each guess to narrow possibilities.\n")
    print("5. Use feedback to refine guesses and improve chances.")
    print(" - After winning or losing, press 'q' to quit or 's' to start.\n")
    print("6. Have fun playing!\n")
    print(Fore.LIGHTGREEN_EX + "Are you ready to be the Mastermind?\n")


def clear_the_terminal():
    """
    From:https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_player_name():
    """
    Prompt the player to enter their name. It must be less than 25 characs.
    and contain no numbers or special characters.
    """
    name_attempts = 0
    max_name_attempts = 4

    while name_attempts < max_name_attempts:
        req_name = input(Fore.RED + "Please enter your name (max 25 chars): ")

        if len(req_name) > 25:
            print(Fore.YELLOW + "\nError: Name must be under 25 chars.\n")
            name_attempts += 1
        elif not req_name.isalpha():
            print(Fore.YELLOW + "\nError: Name must contain only letters.\n")
            name_attempts += 1

        else:
            return req_name
        if name_attempts == max_name_attempts:
            print(Fore.CYAN + "Too many invalid tries, please start over.\n")
    # it will ask the user, if they want to try again
    while True:
        retry = input("Retry entering your name? (y/n): ").strip().lower()
        if retry == "y":
            clear_the_terminal()
            return get_player_name()
        elif retry == "n":
            clear_the_terminal()
            print("\nThank you! To continue, click 'Run Program'.\n")
            exit()
        else:
            print(Fore.YELLOW + "\nInvalid input, please enter 'y'/'n'.\n")


def select_difficulty():
    """
    Function to select the difficulty level.
    """
    while True:
        print("Select Difficulty Level:\n")
        print("1. Easy (10 attempts)")
        print("2. Medium (7 attempts)")
        print("3. Hard (5 attempts)\n")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            return 10
        elif choice == "2":
            return 7
        elif choice == "3":
            return 5
        else:
            print("Invalid choice, please select 1, 2, or 3.")


def generate_secret_number():
    """
    Function to generate a 5-digit secret numbers.
    """
    return str(random.randint(10000, 99999))


# From: https://www.geeksforgeeks.org/mastermind-game-using-python/
def game_play(player_name, attempts):
    """
    Function to play game, the player has to guess the 5-digit secret number.
    """
    secret_number = generate_secret_number()  # saving the value in a variable
    guess_count = 0  # Initialize the guess counter
    while guess_count < attempts:
        guess = input(f"\nEnter a num in {attempts - guess_count} attempts:  ")
        if guess.lower() == 'q':
            print(Fore.LIGHTGREEN_EX + f"You quit. Goodbye, {player_name}!\n")
            return
        if guess.lower() == 's':
            print(Fore.LIGHTGREEN_EX + "\nStarting a new game...\n")
            main_menu()
            return
        if not guess.isdigit() or len(guess) != 5:
            print(Fore.YELLOW + "\nInvalid input. Enter 5 digit num.\n")
            continue
        guess_count += 1

        if int(guess) < int(secret_number):
            print(Fore.YELLOW + "\nYour guess is too low. Try again.\n")
        elif int(guess) > int(secret_number):
            print(Fore.YELLOW + "\nYour guess is too high. Try again.\n")
        else:
            print(Fore.GREEN + f"Fab! {secret_number} is the secret number!\n")
            return
        correct_digits = 0  # Initializes the counter for correct digits.
        feedback = ["X"] * 5  # Creates a list of five "X" characters.
        for i in range(5):
            if guess[i] == secret_number[i]:
                correct_digits += 1
                feedback[i] = Fore.LIGHTRED_EX + guess[i] + Fore.RESET
        print(f"{correct_digits} digit(s) right\n")
        print(Fore.GREEN + "Feedback on digits: ", " ".join(feedback) + "\n")
    print(Fore.RED + f"Sorry, {player_name}. The num was {secret_number}.\n")


def main_menu():
    """
    Function to display the main menu and start/re-start the game.
    """
    clear_the_terminal()
    title_name()
    display_rules()
    player_name = get_player_name()
    print(Fore.YELLOW + f"\nWelcome to the Mastermind Game, {player_name}!\n")
    attempts = select_difficulty()
    game_play(player_name, attempts)
    """Attempts to play/restart the game"""
    restart_attempts = 0
    max_restart_attempts = 3
    while restart_attempts < max_restart_attempts:
        restart = input("Do you want to play again? (y/n): ").strip().lower()
        if restart == "y":
            clear_the_terminal()
            main_menu()
        elif restart == "n":
            clear_the_terminal()
            print(Fore.LIGHTGREEN_EX + "\nThank you for playing! Goodbye!\n")
            break
        else:
            print(Fore.YELLOW + "\nInvalid input, please enter 'y'/'n'.\n")
        restart_attempts += 1
        if restart_attempts >= max_restart_attempts:
            print(Fore.CYAN + "\nToo many invalid tries, please start over\n")
            exit()


# Code executes directly, when script runs in main
if __name__ == "__main__":
    main_menu()
