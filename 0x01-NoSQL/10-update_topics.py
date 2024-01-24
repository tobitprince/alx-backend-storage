#!/usr/bin/env python3
"""
Change school topic.
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update many rows.
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
