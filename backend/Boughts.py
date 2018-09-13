#!/usr/bin/env python

import boto3

"""Keeps methods to process list of bought products in AWS."""


class Boughts:
    """Reads list of bought buckets and returns them as array."""

    @staticmethod
    def my_buckets():
        # Let's call the Amazon
        # print("Connecting to Amazon..");
        s3 = boto3.resource('s3')
        # buckets
        # print("Listing all buckets.");
        my_bckts = []
        for bucket in s3.buckets.all():
            my_bckts.append(bucket)
            # print(bucket.name)
        return my_bckts
