class Node:
    def __init__(self, val=None, left=None, right=None, height=1):
        self.val = val
        self.left = left
        self.right = right
        self.height = height

    def __repr__(self, level=0, prefix="Root: "):
        ret = "|\t" * (level) + prefix + repr(self.val) + f" (H: {self.height})\n"
        if self.left:
            ret += self.left.__repr__(level + 1, prefix="L--- ")
        if self.right:
            ret += self.right.__repr__(level + 1, prefix="R--- ")
        return ret
    
    
    
