import colorama 
from colorama import Fore, Back, Style 
colorama.init(autoreset=True) # Initialize colorama for color support

import random #Generates random items from sequences, and shuffle lists.
import os  # Interact with the operating system.


# ASCII art generated from Patorjk
#https://www.digitalocean.com/community/tutorials/python-raw-string

def title_name():
    """
    Function to print the game title in green ASCII art.

    This function uses the colorama library to print the game title in green color.
    The ASCII art for the title is manually centered by adding spaces at the beginning 
    of each line.
    """
    print(Fore.GREEN + r"""
                            ___  ___             _                ___  ___ _             _ 
                            |  \/  |            | |               |  \/  |(_)           | |
                            | .  . |  __ _  ___ | |_   ___  _ __  | .  . | _  _ __    __| |
                            | |\/| | / _` |/ __|| __| / _ \| '__| | |\/| || || '_ \  / _` |
                            | |  | || (_| |\__ \| |_ |  __/| |    | |  | || || | | || (_| |
                            \_|  |_/ \__,_||___/ \__| \___||_|    \_|  |_/|_||_| |_| \__,_|
                                                                    
""" + Fore.RESET)

def display_rules():
    """
    Function to display the game rules.
    """

    print(Fore.LIGHTRED_EX + "                                         ====▞▞▞▞▞▖🆁 🆄 🅻 🅴 🆂 ▝▞▞▞▞▞===\n" + Fore.RESET)
    print("                           1. Guess the computer's random 5-digit number within 7 attempts.\n")
    print("                           2. After each guess, the computer shows:")
    print("                               - Correct digits in the correct positions.")
    print("                               - 'X' for incorrect digits.\n")
    print("                           3. The game provides feedback after each guess to help narrow down the possibilities.\n")
    print("                           4. Use the feedback to refine your next guess and increase your chances of winning.")
    print("                               - After winning or losing, player can use 'q' to quit the game and 's' to starting a new game..\n")
    print("                           5. Have fun playing!\n")
    print(Fore.LIGHTMAGENTA_EX + "Are you ready to uncover the secret code and become the ultimate Master Mind?\n" + Fore.RESET)


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
        req_name = input(Fore.GREEN + "Please enter your name (must be less than 25 characters, and contain only letters): ")

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

if __name__ == "__main__": # This Code executes directly here, when this script runs, from: https://www.youtube.com/watch?v=y_CX2Rvitk8
    main_menu()