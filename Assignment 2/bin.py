from avl import AVLTree

class Bin:
    def __init__(self, bin_id, capacity):
        self.id = bin_id
        self.capacity = capacity
        self.objects = AVLTree()
        
    def add_object(self, object):
        self.objects.insert(object)
        self.capacity -= object.size

    def remove_object(self, object_id):
        obj_node = self.objects.search(object_id)
        if obj_node:
            obj = obj_node.val
            self.objects.delete(obj)
            self.capacity += obj.size
        
    def __repr__(self):
        return f"(cap: {self.capacity}, id: {self.id})"

