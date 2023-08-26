#!/usr/bin/env python3
#Joulle command line utility for developers! :)
import os
import sys
import sqlite3
from colorama import Style,Fore,Back


def gen_cli_msg(msg):
    print(f"{Fore.CYAN}>>{msg}{Style.RESET_ALL}")

print(f"{Fore.CYAN}{'-'*20}{Fore.BLUE}JOULLECLI{Fore.CYAN}{'-'*20}{Style.RESET_ALL}")
for i in sys.argv:
    gen_cli_msg(i)


def get_action(arg:str):
    if arg.startswith('--'):
        idx = sys.argv[1:].index(arg)
        try:
            optval = sys.argv[1:][idx+1]
        except IndexError:
            raise Exception(f'Please provide value for arg{arg.strip("--")}')
    elif arg.startswith('-'):
        ...
    else:
        ...

def handle_argv(argv=None):
    if not argv[1:]:
        return
    else:
        for action in sys.argv:
            get_action(action)


def main():
    """Run administrative tasks."""
    handle_argv(sys.argv)



if __name__ == "__main__":
    main()