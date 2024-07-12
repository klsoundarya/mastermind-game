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