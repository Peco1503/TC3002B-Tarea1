class HashTable:
    def __init__(self):
        self._table = {}

    def insert(self, key, value):
        """Insert a key-value pair into the hashtable"""
        if key in self._table:
            print(f"Key {key} already exists. Updating value.")
        self._table[key] = value
        print(f"Inserted {key}: {value} into the hashtable")

    def get(self, key):
        """Retrieve a value by key from the hashtable"""
        if key not in self._table:
            print(f"Key {key} not found in the hashtable")
            return None
        return self._table[key]
    
    def delete(self, key):
        """Delete a key-value pair from the hashtable"""
        if key not in self._table:
            print(f"Key {key} not found in the hashtable")
            return
        del self._table[key]
        print(f" Deleted {key} from the hashtable")
    
    def values(self):
        """Get all values in the hashtable"""
        return list(self._table.values())
    
    def keys(self):
        """Get all keys in the hashtable"""
        return list(self._table.keys())
    
    def items(self):
        """Get all key-value pairs in the hashtable"""
        return list(self._table.items())
    
    def size(self):
        """Get the number of key-value pairs in the hashtable"""
        return len(self._table)