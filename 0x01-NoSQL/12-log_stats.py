#!/usr/bin/env python3
"""
Stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def print_stats(collection):
    ''' Print the number of documents in the collection
    '''
    total_logs = collection.count_documents({})
    print(total_logs, "logs")

    methods = ["GET", "POST", "PUTS", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print("    method", method + ":", count)

    count_status = collection.count_documents({"method": "GET", "path": "/status"})
    print(count_status, "status check")
