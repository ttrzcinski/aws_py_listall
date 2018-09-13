#!/usr/bin/env python
"""Keeps data of user needed to remotely connect to AWS."""


class UserData:
    """Keeps name of user"""
    name: str
    """Keeps name of user's account"""
    account: str

    # Creates new instance based on given variables
    def __init__(self, name: str, account: str):
        self.name = name
        self.account = account

    # Equals
    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return False # NetImplemented
        return (self.name, self.account) == (other.name, other.account)

    # Representation
    def __repr__(self):
        return (f'{self.__class__.__name__}'
                f'(name={self.name}, account={self.account})')

    # Prints current object as line in console
    def as_line(self):
        print(f'Users name: {self.name} has account: {self.account}')


if __name__ == "main":
    userData = UserData()

