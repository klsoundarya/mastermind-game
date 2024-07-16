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
    print("    ============================================================\n")

def display_rules():
    """
    Function to display the game rules.
    """
    
    print(Fore.LIGHTRED_EX + "▞▞▞▞▞▞ 🆁 🆄 🅻 🅴 🆂 ▝▞▞▞▞▞\n" + Fore.RESET)
    print("1. Guess the computer's random 5-digit number within the chosen difficulty level.\n")
    print("2. Choose a number between 10,000 and 99,999.\n")
    print("3. After each guess, the computer shows:")
    print(" - Correct digits in the correct positions.")
    print(" - 'X' for incorrect digits.\n")
    print("4. Feedback is given after each guess to narrow possibilities.\n")
    print("5. Use feedback to refine guesses and improve chances.")
    print(" - After winning or losing, press 'q' to quit or 's' to start a new game.\n")
    print("6. Have fun playing!\n")
    print(Fore.YELLOW + "Are you ready to uncover the secret code and become the ultimate Master Mind?\n" + Fore.RESET)


def clear_the_terminal():
    """
    This function clears the terminal screen. https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_player_name():
    """
    Prompt the player to enter their name. The name must be less than 25 characters
    and contain no numbers or special characters.
    """
    name_attempts = 0
    max_name_attempts = 4
    
    while name_attempts < max_name_attempts:
        req_name = input(Fore.LIGHTGREEN_EX + "Please enter your name (max 25 chars, letters only): ")

        if len(req_name) > 25:
            print(Fore.YELLOW + "\nError: The name should be less than 25 characters.\n")
            name_attempts += 1
        
        elif not req_name.isalpha():
            print(Fore.YELLOW + "\nError: Invalid input. The name should only contain letters.\n")
            name_attempts += 1

        else:
            return req_name
        
        if name_attempts == max_name_attempts:
            print(Fore.CYAN + "Too many invalid attempts. Please start over the game.\n")
            exit()
            
def select_difficulty():
    """
    Function to select the difficulty level.
    """
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

def game_play(player_name, attempts):
    """
    Function to play the number guessing game. The player has to guess the 5-digit secret number within 7 attempts.
    strip() is from: (https://www.w3schools.com/python/ref_string_strip.asp)
    """
    secret_number = generate_secret_number() #saving the value in a variable 
    attempts = 7  # Number of attempts allowed
    guess_count = 0  # Initialize the guess counter
    
    while guess_count < attempts:
        guess = input(Fore.RED + f"\nHello, {player_name}! Try to guess the 5-digit secret number, you have {attempts - guess_count} attempts left: ").strip()
        
        if guess.lower() == 'q':
            print(Fore.LIGHTGREEN_EX + "\nYou chose to quit the game. Goodbye, {player_name}!\n")
            return
        
        if guess.lower() == 's':
            print(Fore.LIGHTGREEN_EX + "\nStarting a new game...\n")
            main_menu()
            return
        
        if not guess.isdigit() or len(guess) != 5:
            print(Fore.LIGHTYELLOW_EX + "\nInvalid input. Please enter a 5-digit number.\n")
            continue
        
        guess_count += 1

        if int(guess) < int(secret_number):
            print(Fore.YELLOW + "\nThe number you guessed is lower than the correct number, please try again.\n")
        elif int(guess) > int(secret_number):
            print(Fore.YELLOW + "\nThe number you guessed is higher than the correct number, please try again.\n")
        else:
            print(Fore.GREEN +  f"\nCongratulations, {player_name}! You guessed the correct number {secret_number} in {guess_count} tries! You're a true Mastermind!\n")
            return
        
        correct_digits = 0  #Initializes the counter for correct digits.
        feedback = ["X"] * 5  #Creates a list of five "X" characters for feedback on correct digits.
        
        for i in range(5):
            if guess[i] == Fore.GREEN + secret_number[i]:
                correct_digits += 1
                feedback[i] = Fore.RED + guess[i] + Fore.RESET
        
        print(f"Not the correct number, but you got {correct_digits} digit(s) right\n")
        print(Fore.GREEN + "Feedback on correct digits: ", " ".join(feedback) + "\n")
    
    print(Fore.RED + f"Sorry, {player_name}. The correct number was {secret_number}. Better luck next time!\n")

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
            restart_attempts += 1
            break
        else:
            print(Fore.LIGHTYELLOW_EX + "\nInvalid input. Please enter 'y' or 'n'.\n")
        
        if restart_attempts >= max_restart_attempts:
            print(Fore.CYAN + "\nToo many invalid inputs. Please start over the game again.\n")
            exit()

# Code executes directly, when script runs in main

if __name__ == "__main__": 
    main_menu()
