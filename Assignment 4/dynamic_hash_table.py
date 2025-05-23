from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        new_size = get_next_size()
        self.size = new_size
        old_table = self.table
        self.table = [None] * self.size
        self.num_elements = 0
        
        for i in old_table:
            if i:
                if self.collision_type == 'Chain':
                    for j in i: self.insert(j)
                else: self.insert(i)
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()
            

    
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        print(f'startsize = {self.size}')
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        # print('rehashing....')
        # print(f'old_size = {self.size}, num_elemtns = {self.num_elements}')
        new_size = get_next_size()
        # print(f'old = {self.size}, new = {new_size}')
        self.size = new_size
        old_table = self.table
        self.table = [None] * self.size
        self.num_elements = 0

        for i in old_table:
            if i:
                if self.collision_type == 'Chain':
                    for j in i: self.insert(j)
                else: self.insert(i)
                
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        # print('inserting',key)
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()