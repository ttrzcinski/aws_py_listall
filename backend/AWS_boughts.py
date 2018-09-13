#!/usr/bin/env python

import boto3

"""Keeps methods to process list of bought products in AWS."""


class AWS_boughts:
    """Reads list of bought buckets and returns them as array."""

    def my_buckets(self):
        # Let's call the Amazon
        # print("Connecting to Amazon..");
        s3 = boto3.resource('s3');
        # buckets
        # print("Listing all buckets.");
        my_bckts = []
        for bucket in s3.buckets.all():
            my_bckts.append(bucket)
            # print(bucket.name)
        return my_bckts
