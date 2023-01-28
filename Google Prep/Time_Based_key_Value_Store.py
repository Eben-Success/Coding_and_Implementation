# Time Based Key-Value Store

"""
Implement the TimeMap class:
    * Timemap() initialize the object of the data structure.
    * void set(String key, String value, int timestamp): stores the key `key` with the value
    `value` at the given time `timestamp`.
    * String get(String key, int timestamp): return a value such that
    `set` was called previously, with `timestamp_prev` <= `timestamp`. If there are multiple such 
    value, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns
    """

class TimeMap:
    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int):
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int):
        res = ""

        values = self.map.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2

            if values[mid] <= timestamp:
                l = mid + 1
            else:
                h = mid - 1
        return res
