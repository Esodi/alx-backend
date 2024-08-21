#!/usr/bin/env python3
'''
class BasicCache that inherits from BaseCaching and is a caching system
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''the class itself '''
    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item
        return self.cache_data

    def get(self, key):
        try:
            return self.cache_data[key]
        except KeyError:
            return
