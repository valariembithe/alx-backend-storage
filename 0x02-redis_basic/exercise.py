#!/usr/bin/env python3
"""Task 0 module"""
import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


class Cache:
    '''Represents an object for storing data in a Redis data storage'''
    def __init__(self) -> None:
        '''stores an instance of the Redis client as a private variable'''
        self._redis = redis.Redis()
        self._redis.flushdb(True)
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''store the input data in Redis using the random key and return the key'''
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
    
    def get(self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        '''used to convert the data back to the desired format.'''
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        '''Returns a string value of the Redis storage'''
        return self.get(key, lambda x: x.decode('utf-8'))    

    def get_int(self, key: str) -> int:
        '''Returns an integer value of Redis storage'''
        return self.get(key, lambda x: int(x)) 
