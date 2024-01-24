#!/usr/bin/env python3
"""Task 0 module"""
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


class Cache:
    def __init__(self) -> None:
        '''stores an instance of the Redis client as a private variable'''
        self._redis = redis.Redis()
        self._redis = flushdb(True)
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''store the input data in Redis using the random key and return the key'''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
    