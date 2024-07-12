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