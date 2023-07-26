#!/usr/bin/env python3
"""FIFO Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache"""
    def __init__(self):
        """Initializes the FIFO caching"""
        super().__init__()

    def put(self, key, item):
        """Assigns the dictionary self.cache_data to the key."""
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}". format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """Returns the self cache data value linked to key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data[key]
