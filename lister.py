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
        
        # TODO Check, if user is present in global in ~user/.aws/config

        # TODO Present menu with available actions - and loop until answer is from list of wanted

        choosen = 'ec2'
        if choosen == 'buckets':
            # Get from AWS list of bought products - buckets
            awsb = Boughts()
            bought_list = awsb.my_buckets()
            # Present list of bought products in console
            pp = PrettyPrint
            pp.numbered_list(bought_list, 'S3 Buckets', 'Bucket')
        elif choosen == 'queues':
            # Get from AWS list of bought products - queues
            awsb = Boughts()
            bought_list = awsb.my_sqs()
            # Present list of bought products in console
            pp = PrettyPrint
            pp.numbered_list(bought_list, 'Simple Queue Services', 'sqs')
        elif choosen == 'ec2':
            # Get from AWS list of bought products - queues
            awsb = Boughts()
            ec2s = awsb.my_ec2()
            # Present list of bought products in console
            pp = PrettyPrint
            pp.numbered_list(ec2s, 'EC2', 'ec2 inst')
        else:
            print('Then have a nice day..')


if __name__ == "__main__":
    lister = Lister()
    lister.main()
