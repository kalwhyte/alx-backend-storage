#!/urs/bin/env python3
"""lists all documents in a collection
"""


def list_all(mongo_collection):
    """Return an empty list
    """
    return [doc for doc in mongo_collection.find()]