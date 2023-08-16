#!/usr/bin/env python3
'''
   Exercise: Writing strings to Redis
'''
import redis
import uuid
from typing import Union


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


if __name__ == '__main__':
    cache = Cache()

    data_to_store = b"hello"
    stored_key = cache.store(data_to_store)

    local_redis = redis.Redis()
    print(local_redis.get(stored_key))
