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

    def get(self, key: str, func: Callable[[bytes], Union[str, bytes, int, float]] = None) -> Union[str, bytes, int, float, None]:
        """get value associated w key from redis"""
        data = self._redis.get(key)
        if data is not None and func is not None:
            return func(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """gets string value associated w key from redis"""
        return self.get(key, func = lambda x: x.decode("utf-8") if isinstance(x, bytes) else x)

    def get_int(self, key: str) -> Union[int, None]:
        """gets int value associated w key from redis"""
        return self.get(key, func = lambda x: int(x) if isinstance(x, bytes) else x)
