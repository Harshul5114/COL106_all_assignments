from node import Node

def comp_bins_y_r(node_1, node_2):
    if (node_1.capacity == node_2.capacity):
        return node_1.id < node_2.id
    
    return node_1.capacity > node_2.capacity

def comp_bins_b_g(node_1, node_2):
    if (node_1.capacity == node_2.capacity):
        return node_1.id > node_2.id
    
    return node_1.capacity > node_2.capacity

def comp_ids(node_1, node_2):
    return node_1.id > node_2.id


class AVLTree:
    def __init__(self, compare_function = comp_ids):
        self.root = None
        self.size = 0
        self.comparator = compare_function
    
    def insert(self, ele):
        self.root = self._insert_rec(ele, self.root)
        self.size += 1

    def _insert_rec(self, ele, node):
        if node is None:
            return Node(ele)

        if self.comparator(node.val, ele):
            node.left = self._insert_rec(ele, node.left)
        else:
            node.right = self._insert_rec(ele, node.right)

        node = self._restructure(node)

        return node

    def _restructure(self, node):
        if node is None:
            return
        
        balance = self._get_balance(node)
        r_bal = self._get_balance(node.right)
        l_bal = self._get_balance(node.left)

        #LL imbalance
        if balance > 1 and l_bal >= 0:
            temp = node.left  
            T1 = temp.right   

            temp.right = node  
            temp.right.left = T1     

            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
            temp.height = 1 + max(self._get_height(temp.left), self._get_height(temp.right))

            return temp  

        #LR imbal
        elif balance > 1 and l_bal < 0:
            temp = node.left.right  
            T1 = temp.right          
            T2 = temp.left          

            temp.left = node.left    
            temp.right = node        

            temp.left.right = T2     
            temp.right.left = T1     

            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
            temp.left.height = 1 + max(self._get_height(temp.left.left), self._get_height(temp.left.right))
            temp.height = 1 + max(self._get_height(temp.left), self._get_height(temp.right))


            return temp
        
        #RR
        elif balance < -1 and r_bal <= 0:
            temp = node.right  
            T1 = temp.left   

            temp.left = node  
            temp.left.right = T1     

            node.height = 1 + max(self._get_height(node.right), self._get_height(node.left))
            temp.height = 1 + max(self._get_height(temp.right), self._get_height(temp.left))

            return temp  
        
        #RL
        elif balance < -1 and r_bal > 0:
            temp = node.right.left
            T1 = temp.left
            T2 = temp.right
            
            temp.right = node.right
            temp.left = node
            temp.right.left = T2
            temp.left.right = T1
            
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
            temp.right.height = 1 + max(self._get_height(temp.right.left), self._get_height(temp.right.right))
            temp.height = 1 + max(self._get_height(temp.left), self._get_height(temp.right))
            
            return temp

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        return node
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def search(self,ele):
        if (self.root):
            if (self.root.val.id == ele):
                return self.root
            else:
                return self._search_rec(ele,self.root)
        else:
            return False

    def _search_rec(self, ele, node):

        if not node:
            return False
        
        if node.val.id == ele:
            return node
        
        if node.val.id > ele:
            return self._search_rec(ele, node.left)
        else:
            return self._search_rec(ele, node.right)
        
    def delete(self, ele):
        if self.root:
            self.root = self._delete_rec(ele, self.root)
            self.size -= 1

        else:
            return False
        return True

    def _delete_rec(self, ele, node):
        if node is None:
            return node

        if self.comparator(node.val, ele):
            node.left = self._delete_rec(ele, node.left)
        elif self.comparator(ele, node.val):
            node.right = self._delete_rec(ele, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            successor = self._inorder_successor(node)
            node.val = successor.val
            node.right = self._delete_rec(successor.val, node.right)

        return self._restructure(node)

    def _inorder_successor(self, node):
        current = node.right
        while current.left is not None:
            current = current.left
        return current
    
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def inorder(self):
        lst = []
        def dfs(node):
            if node:
                dfs(node.left)
                lst.append(node.val.id)
                dfs(node.right)
        dfs(self.root)
        return lst
    
    def __repr__(self):
        if not self.root:
            return "Empty AVL Tree"
        return repr(self.root)