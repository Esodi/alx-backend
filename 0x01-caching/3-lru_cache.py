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
        self.cache_data = OrderedDict()  # Use an OrderedDict to maintain the order of insertion

    def put(self, key, item):
        if key is None or item is None:
            return

        # If the key already exists, move it to the end (most recently used)
        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

        # If the number of items exceeds MAX_ITEMS, discard the least recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key, _ = self.cache_data.popitem(last=False)  # Pop the first item
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        ''' get method '''
        if key is None or key not in self.cache_data:
            return None

        # Move the key to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]

