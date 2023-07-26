#!/usr/bin/env python3
"""This class impliments the FIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache"""

    def __init__(self):
        """Initializes the LIFO caching"""
        super().__init__()

    def put(self, key, item):
        """Assigns the dictionary self.cache_data to the key.

            Args:
                key: The key item
                item: The value item
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                last_key = next(reversed(self.cache_data))
                del self.cache_data[last_key]
                print("DISCARD: {}". format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """Returns the self cache data value linked to key

            Args:
                key:the key item
        """
        if key is None or self.cache_data.get(key) is None:
            return None
