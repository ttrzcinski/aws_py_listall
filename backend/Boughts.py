#!/usr/bin/env python

import boto3

"""Keeps methods to process list of bought products in AWS."""


class Boughts:
    """Reads list of bought buckets and returns them as array."""

    @staticmethod
    def my_buckets():
        # Let's call the Amazon about buckets
        s3 = boto3.resource('s3')
        # buckets
        my_buckets = []
        for bucket in s3.buckets.all():
            my_buckets.append(bucket)
        return my_buckets

    @staticmethod
    def my_sqs():
        my_sqs = []
        sqs = boto3.resource('sqs')
        for queue in sqs.queues.all():
            my_sqs.append(queue.url)
        return my_sqs

    @staticmethod
    def my_ec2():
        my_ec2 = []
        ec2 = boto3.resource('ec2')
        # da_response = ec2.describe_instance()
        instances = ec2.instances.all()
        #
        for instance in instances:
            my_ec2.append(instance.id)
        return my_ec2  # my_ec2
