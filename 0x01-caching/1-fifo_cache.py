#!/usr/bin/env python3
'''class FIFOCache that inherits from BaseCaching and is a caching system'''


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' inherits from BaseCaching and is a caching system'''
    def __init__(self):
        '''init method'''
        super().__init__()

    def put(self, key, item):
        '''put method'''
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                kv = next(iter(self.cache_data.items()))
                k = kv[0]
                print(f'DISCARD: {k}')
                del self.cache_data[k]
        return self.cache_data

    def get(self, key):
        ''' get method '''
        try:
            return self.cache_data[key]
        except KeyError:
            return
