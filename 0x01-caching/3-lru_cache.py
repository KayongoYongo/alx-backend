#!/usr/bin/env python3
"""LRU Caching implimentation"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    A class that impliments the LRUCache algorithm

    Methods
    ------
    """
    def __init__(self):
        # Call the parent class's init method
        super().__init__()
        # Use OrderedDict to track access order
        self.access_order = OrderedDict()

    def put(self, key, item):
        """Assigns the dictionary self.cache_data to the key.

            Args:
                key: The key item
                item: The value item
        """
        if key is None or item is None:
            return

        # Check if the cache is full
        if len(self.cache_data) >= self.MAX_ITEMS:
            # Get the least recently used item's key (LRU algorithm)
            lru_key, _ = next(iter(self.access_order.items()))
            # Remove the LRU item from both the access order and the cache
            del self.access_order[lru_key]
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        # Add the new item to the cache and update its access order
        self.cache_data[key] = item
        self.access_order[key] = True

    def get(self, key):
        """Returns the self cache data value linked to key

            Args:
                key: the key item
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the access order for the accessed item
        self.access_order.move_to_end(key)
        return self.cache_data[key]
