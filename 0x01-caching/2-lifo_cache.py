#!/usr/bin/env python3
'''
class LIFOCache that inherits from BaseCaching and is a caching system
'''


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''the class itself'''
    def __init__(self):
        ''' init method '''
        super().__init__()

    def put(self, key, item):
        ''' put method '''
        if key and item:
            if key in self.cache_data:
                del self.cache_data[key]
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                k = next(reversed(self.cache_data))
                print(f'DISCARD: {k[0]}')
                del self.cache_data[k]
            self.cache_data[key] = item


    def get(self, key):
        ''' get method '''
        try:
            return self.cache_data[key]
        except KeyError:
            return
