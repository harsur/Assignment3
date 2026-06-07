class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def search(self, key):
        return self.table.get(key, None)

    def delete(self, key):
        if key in self.table:
            del self.table[key]

ht = HashTable()

ht.insert("Alice", 90)
ht.insert("Bob", 85)

print(ht.search("Alice"))
ht.delete("Bob")
print(ht.search("Bob"))