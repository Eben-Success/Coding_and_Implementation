# create a class HashMap

# Total time: O(n)
# Space: O(n): number of keys added to the table.

class HashMap:

    # create a constructor method for the class
    def __init__(self):
        # initialize the size to a prime to reduce collision in the hash table
        self.size = 10007
        self.table = [None] * self.size

    # find the hash value
    def calculate_hash_value(self, key):
        return key % self.size

    # Time: average of O(1) when the key have unique index
    # Time: O(n) in worst when collision occurs 
    # happens when many keys are hashed to the same index
    def add_value(self, key):
        hv = self.calculate_hash_value(key)

        if self.table[hv] is None:
            self.table[hv] = key
        else:
            self.table[hv].append(key)

    # Time: O(1) in average when key is unique
    # Time: O(n) when collision occurs 
    def remove_value(self, key):
        hv = self.calculate_hash_value(key)

        if self.table[hv] is not None:
            while key in self.table[hv]:
                self.table[hv].remove(key)


    # Tim: O(1) in average when key is unique.
    # Time: O(n) in worst when collision occurs.
    def contain_value(self, key):
        hv = self.calculate_hash_value(key)

        if self.table[hv] is not None:
            return key in self.table[hv]
        return False