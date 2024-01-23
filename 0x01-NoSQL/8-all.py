#!/usr/bin/env python3
"""Python function for NoSQL query in MongoDB"""


def list_all(mongo_collection):
    """"lists/finds all documents in collection"""
    return mongo_collection.find()
