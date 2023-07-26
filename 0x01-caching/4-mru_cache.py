#!/usr/bin/env python3

from collections import OrderedDict
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    def __init__(self):
        # Call the parent class's init method
        super().__init__()
        # Use OrderedDict to track access order (most recently used at the end)
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
            # Get the most recently used item's key (MRU algorithm)
            mru_key = next(reversed(self.access_order))
            # Discard the most recently used item
            del self.access_order[mru_key]
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        # Add the new item to the cache and update its access order
        self.cache_data[key] = item
        self.access_order[key] = True

    def get(self, key):
        """Returns the self cache data value linked to key

            Args:
                key:the key item
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the access order for the accessed item (move to end)
        self.access_order.move_to_end(key)
        return self.cache_data[key]
