#!/usr/bin/env python3
"""write strings to redis"""
import redis
import uuid
from typing import Union


class Cache:
    """class cache"""
    def ___init(self) -> None:
        """initialize cache instance w redis and flush db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """returns string of random key used store input data in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
