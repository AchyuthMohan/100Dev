from pyfiglet import *
from termcolor import colored
from random import randint


def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)


def display_text():
    bordered("100Dev")
    font = ['slant', "banner3-D",   "big"     "larry3d", "avatar"]
    valid_color = ['red', 'green', 'yellow', 'blue', 'cyan']
    random_choice = randint(0, len(font)-1)
    msg = "100Dev"
    color = valid_color[random_choice]
    ascii_art = figlet_format(msg, font=font[random_choice])
    colored_ascii = colored(ascii_art, color)
    print("\n\n\n\n\n\n")
    print(colored_ascii)
    print("\n\n")


def decorator(func):
    def wrapper(*args, **kwargs):

        display_text()
        result = func(*args, **kwargs)

        return result
    return wrapper
