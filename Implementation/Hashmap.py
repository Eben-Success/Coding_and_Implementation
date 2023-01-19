# Create a HashMap class

class HashMap:

    # define a constructor method for the class
    def __init__(self):
        """The size is set to 10000 which is a prime number to avoid 
        collision. Collision occurs when multiple keys are mapped to the
        same index in a hash table."""
        self.size = 10007
        self.table = [None] * self.size

    def calculate_hash_value(self, key):
        return key % self.size

    def add(self, key):
        hv = self.calculate_hash_value(key)

        if self.table[hv] is None:
            self.table[hv] = key
        else:
            self.table[hv].append(key)

    def remove(self, key):
        hv = self.calculate_hash_value(key)
        