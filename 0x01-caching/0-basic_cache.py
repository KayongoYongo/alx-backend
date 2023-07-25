#!/usr/bin/env python3
"""Returns a basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system"""
    def put(self, key, item):
        """Assign to the dictionary the item value for the key"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the self cache data value linked to key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data[key]
