#!/usr/bi/env python3
"""LFU caching"""


from collections import defaultdict, OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A class that impliments the LRUCache algorithm

    Methods
    ------
    """
    def __init__(self):
        # Call the parent class's init method
        super().__init__()
        # Use defaultdict(int) to track the frequency of each item's access
        self.frequency = defaultdict(int)
        # Use OrderedDict to track the access order for LFU and LRU algorithms
        self.access_order = OrderedDict()
        # Counter to keep track of the access order
        self.access_counter = 0

    def put(self, key, item):
        """Assigns the dictionary self.cache_data to the key.

            Args:
                key: The key item
                item: The value item
        """
        if key is None or item is None:
            return

        # Update the frequency of the accessed item
        self.frequency[key] += 1

        # Update the access order for the accessed item
        self.access_counter += 1
        self.access_order[key] = self.access_counter

        # Check if the cache is full
        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the least frequently used item(s)
            min_frequency = min(self.frequency.values())
            least_frequent_keys = [k for k in self.frequency if
                                   self.frequency[k] == min_frequency]

            """If there is more than one least frequent item,
            use the LRU algorithm to discard the least recently used
            """
            if len(least_frequent_keys) > 1:
                lru_key = next(iter(self.access_order))
                for key in self.access_order:
                    if key in least_frequent_keys and self.access_order[key] \
                            < self.access_order[lru_key]:
                        lru_key = key

                # Discard the least recently used
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.access_order[lru_key]
                print("DISCARD:", lru_key)

            else:
                # Discard the least frequent item
                del self.cache_data[least_frequent_keys[0]]
                del self.frequency[least_frequent_keys[0]]
                del self.access_order[least_frequent_keys[0]]
                print("DISCARD:", least_frequent_keys[0])

        """Add the new item to the cache and
        update its access order and frequency"""
        self.cache_data[key] = item

    def get(self, key):
        """Returns the self cache data value linked to key

            Args:
                key: the key item
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the access order for the accessed item
        self.access_counter += 1
        self.access_order[key] = self.access_counter

        return self.cache_data[key]
