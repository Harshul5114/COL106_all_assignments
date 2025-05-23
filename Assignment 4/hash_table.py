from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        self.collision_type = collision_type
        self.params = params
        self.size = self.params[-1]
        self.table = [None] * self.size
        self.num_elements = 0

    def insert(self, x):
        pass

    def find(self, key):
        pass

    def get_slot(self, key):
        z = self.params[0]
        val = self.hash_func(key, z, self.size)
        return val

    def get_load(self):
        return self.num_elements / self.size

    def probe(self, index, i, double_hash_value=None):
        if self.collision_type == "Linear":
            return (index + i) % self.size
        elif self.collision_type == "Double":
            return (index + i * double_hash_value) % self.size

    def double_hash(self, key):
        z2, c2 = self.params[1], self.params[2]
        return c2 - (self.hash_func(key, z2, c2) % c2)

    def hash_func(self, key, param, mod):
        z = param
        p = lambda x: ord(x) - (97, 39)[ord(x) <= 90]
        val = p(key[-1])
        for i in range(len(key) - 2, -1, -1):
            val = (val * z + p(key[i])) % mod
        return val

    def __str__(self):
        result = []
        if self.collision_type == "Chain":
            for i in self.table:
                if i:
                    chain_elements = []
                    for j in i:
                        if isinstance(j, tuple):
                            chain_elements.append(f"({j[0]}, {j[1]})")
                        else:
                            chain_elements.append(f"{j}")
                    result.append(" ; ".join(chain_elements))
                else:
                    result.append("<EMPTY>")
            return " | ".join(result)
        else:
            for i in self.table:
                if isinstance(i, tuple):
                    result.append(f"({i[0]}, {i[1]})")
                else:
                    result.append(f"{i}" if i else "<EMPTY>")
            return " | ".join(result)

    def rehash(self):
        pass


class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def insert(self, key):
        if self.find(key):
            return

        index = self.get_slot(key)
        double_hash_value = self.double_hash(key) if self.collision_type == "Double" else None

        if self.collision_type == "Chain":
            self.num_elements += 1
            if not self.table[index]:
                self.table[index] = [key]
            else:
                self.table[index].append(key)
        else:
            i = 0
            while i < self.size:
                new_index = self.probe(index, i, double_hash_value)
                if not self.table[new_index]:
                    self.table[new_index] = key
                    self.num_elements += 1
                    return
                i += 1
            raise Exception("Table is full")

    def find(self, key):
        index = self.get_slot(key)
        double_hash_value = self.double_hash(key) if self.collision_type == "Double" else None

        if self.collision_type == "Chain":
            if self.table[index]:
                for i in self.table[index]:
                    if i == key:
                        return True
            return False
        else:
            i = 0
            while i < self.size:
                new_index = self.probe(index, i, double_hash_value)
                if self.table[new_index] == key:
                    return True
                i += 1
            return False

    def contents(self):
        contents = []
        if self.collision_type == "Chain":
            for slot in self.table:
                if slot:
                    for key in slot:
                        contents.append(key)
        else:
            for key in self.table:
                if key:
                    contents.append(key)
        return contents


class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def insert(self, x):
        key, val = x
        if self.find(key):
            return

        index = self.get_slot(key)
        double_hash_value = self.double_hash(key) if self.collision_type == "Double" else None

        if self.collision_type == "Chain":
            self.num_elements += 1
            if not self.table[index]:
                self.table[index] = [x]
            else:
                self.table[index].append(x)
        else:
            i = 0
            while i < self.size:
                new_index = self.probe(index, i, double_hash_value)
                if not self.table[new_index]:
                    self.table[new_index] = x
                    self.num_elements += 1
                    return
                i += 1
            raise Exception("Table is full")

    def find(self, key):
        index = self.get_slot(key)
        double_hash_value = self.double_hash(key) if self.collision_type == "Double" else None

        if self.collision_type == "Chain":
            if self.table[index]:
                for i, v in self.table[index]:
                    if i == key:
                        return v
            return
        else:
            i = 0
            while i < self.size:
                new_index = self.probe(index, i, double_hash_value)
                if self.table[new_index] and self.table[new_index][0] == key:
                    return self.table[new_index][1]
                i += 1
            return

    def contents(self):
        contents = []
        if self.collision_type == "Chain":
            for slot in self.table:
                if slot:
                    for key, value in slot:
                        contents.append(key)
        else:
            for entry in self.table:
                if entry:
                    key, value = entry
                    contents.append(key)
        return contents
