#!/usr/bin/env python3
'''
   Exercise: Writing strings to Redis
'''
import redis
import uuid
from typing import Union, Optional, Callable


class Cache:
    ''' Cache class '''

    def __init__(self, host='localhost', port=6379, db=0):
        ''' Constructor '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        ''' Method that takes a data argument 
            and returns a string
        '''
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key


    def get(self, key: str, fn: Optional[Callable] = None):
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> str:
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key:str) -> int:
        return self.get(key, fn=int)


if __name__ == '__main__':
    cache = Cache()

    data_to_store = b"hello"
    stored_key = cache.store(data_to_store)

    local_redis = redis.Redis()
    print(local_redis.get(stored_key))

    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

    print("All test cases passed!")
