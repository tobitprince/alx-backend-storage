#!/usr/bin/env python3
"""Implement the get_page function."""
import requests
import redis
from functools import wraps
from typing import Callable
cache = redis.Redis()


def counter(method: Callable) -> Callable:
    """Set an expiration on a key."""

    @wraps(method)
    def wrapper(url) -> Callable:
        """Set function wrapper."""
        count_key = f"count:{url}"
        print(count_key)
        result_key = f"result:{url}"

        cache.incr(count_key)
        result = cache.get(result_key)
        if result:
            return result.decode('utf8')
        result = method(url)
        cache.set(count_key, 0)
        cache.setex(result_key, 10, result)
        return result
    return wrapper


@counter
def get_page(url: str) -> str:
    """Get a url response."""
    return requests.get(url)
