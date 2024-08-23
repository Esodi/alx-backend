#!/usr/bin/env python3
'''
class LIFOCache that inherits from BaseCaching and is a caching system
'''


from collections import OrderedDict
from base_caching import BaseCaching  # Assuming BaseCaching is provided in base_caching module

class LRUCache(BaseCaching):
    ''' class itself '''
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' put method '''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        ''' get method '''
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]

