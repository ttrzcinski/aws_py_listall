#!/usr/bin/env python

from __future__ import print_function
from backend.UserData import UserData
from backend.Boughts import Boughts
from backend.PrettyPrinter import PrettyPrint


class Lister:
    def main(self):
        print("Hello, I'm your Python..")
        name = input("What is your name?\n")
        account = input("What is your account's name?\n")

        user_data = UserData(name, account)
        user_data.as_line()
        # print('Hi, %s.' % name)

        # Get from AWS list of bought products - buckets
        awsb = Boughts()
        bought_list = awsb.my_buckets()
        # Present list of bought products in console
        pp = PrettyPrint
        pp.numbered_list(bought_list, 'S3 Buckets', 'Bucket')


if __name__ == "__main__":
    lister = Lister()
    lister.main()
