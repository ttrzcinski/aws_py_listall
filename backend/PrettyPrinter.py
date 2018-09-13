#!/usr/bin/env python

from colorama import Fore, Style

"""Prints given variable to console for debug or in runtime."""


class PrettyPrint:
    """Presents numbered list with optional title of list and name of entires"""
    def numbered_list(da_list, title=None, name=None):
        # Check entered list
        if not da_list or len(da_list) == 0:
            return
        print()
        # Trim entry params
        if title:
            title = title.strip()
        if name:
            name = name.strip()
        # Present title of list
        if title:
            print(f'List {Fore.CYAN}"{title}"{Style.RESET_ALL}')
        else:
            if name:
                print(f'List of {Fore.CYAN}{name}s{Style.RESET_ALL}')
            else:
                print('Some list')
        print("-----------------------------------")
        # Prepare beginning of line
        beginning = '- '
        if name:
            beginning = name + ": "
        # Present the list
        for item in da_list:
            if not item.name:
                print(f"{beginning}{Fore.LIGHTCYAN_EX}{item}{Style.RESET_ALL}")
            else:
                print(f'{beginning}{Fore.LIGHTCYAN_EX}{item.name}{Style.RESET_ALL}')

        pass