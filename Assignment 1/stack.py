class Stack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self) -> bool:
        if self.items:
            return False
        else:
            return True

    def push(self,ele) -> None:
        self.items.append(ele)

    def pop(self):
        if not self.is_empty():
            a = self.items.pop()
            return a
        else:
            return None
        
    def peek(self):
        return self.items[-1]


    def show(self):
        if not self.is_empty():
            print("Stack =",*self.items)
        else:
            print("Stack is empty...")
    
    def size(self) -> int:
        return len(self.items)


    

    
    
    # You can implement this class however you like