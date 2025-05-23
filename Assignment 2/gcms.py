from bin import Bin
from avl import * #changed
from object import Object, Color
from exceptions import NoBinFoundException


class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self.storage_blue_green = AVLTree(compare_function = comp_bins_b_g)
        self.storage_yellow_red = AVLTree(compare_function = comp_bins_y_r)
        self.bins = AVLTree()
        self.objects = AVLTree()

    def add_bin(self, bin_id, capacity):
        new_bin = Bin(bin_id, capacity)
        self.storage_blue_green.insert(new_bin)
        self.storage_yellow_red.insert(new_bin)
        self.bins.insert(new_bin)
    
    def add_object(self, object_id, size, color):
        # print(f"adding {object_id}, {size}, {color}")
        new_obj = Object(object_id, size, color)
        self.objects.insert(new_obj)
        best_node = self._find_bin_for_obj(new_obj)
        # print("best_node = ",best_node)
        # print(best_node.val)
  
        if best_node:
            best_bin = best_node.val

            # deleting old bin
            for tree in [self.storage_blue_green,self.storage_yellow_red,self.bins]:
                tree.delete(best_bin)

            best_bin.add_object(new_obj)
            new_obj.bin = best_bin.id

            for tree in [self.storage_blue_green,self.storage_yellow_red,self.bins]:
                tree.insert(best_bin)

        else:
            self.objects.delete(new_obj)
            raise NoBinFoundException
    
        # print(self.storage_yellow_red)

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        obj_node = self.objects.search(object_id)
        if obj_node:
            obj = obj_node.val
            obj_bin = self.bins.search(obj.bin).val
            self.objects.delete(obj)

            for tree in [self.storage_blue_green,self.storage_yellow_red,self.bins]:
                tree.delete(obj_bin)

            obj_bin.remove_object(obj.id)
            

            for tree in [self.storage_blue_green,self.storage_yellow_red,self.bins]:
                tree.insert(obj_bin)





    def bin_info(self, bin_id):
        # Returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        node = self.bins.search(bin_id)

        if node:
            binn = node.val
            cap = binn.capacity
            
            return (cap, binn.objects.inorder())
        else:
            raise NoBinFoundException

    def object_info(self, object_id):
        obj_node = self.objects.search(object_id)
        if obj_node:
            obj = obj_node.val
            return obj.bin

        # returns the bin_id in which the object is stored

    def _find_bin_for_obj(self, object):

        def compact_fit(node):
            mini = None
            curr_node = node
            while curr_node:
                if curr_node.val.capacity >= object.size:
                    mini = curr_node
                    curr_node = curr_node.left
                
                else:
                    curr_node = curr_node.right
            return mini

        def largest_fit(node):

            while node.right:
                node = node.right
            if node.val.capacity >= object.size:
                return node
            
        best_node = None
        if object.color.value == 1:  # BLUE
            best_node = compact_fit(self.storage_blue_green.root)
        elif object.color.value == 2:  # YELLOW
            best_node = compact_fit(self.storage_yellow_red.root)
        elif object.color.value == 3:  # RED
            best_node = largest_fit(self.storage_yellow_red.root)
        elif object.color.value == 4:  # GREEN
            best_node = largest_fit(self.storage_blue_green.root)

        return best_node

            