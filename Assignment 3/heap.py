'''
Python Code to implement a heap with general comparison function
'''

class Heap:

    def __init__(self, comparison_function , init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        self.comparator = comparison_function
        self.heap = init_array[:]
        self.size = len(init_array)
        self._heapify()

    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        self.heap.append(value)
        size = len(self.heap)
        self.upheap(size - 1)
        self.size += 1

    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        if self.heap:
            self._swap(0, self.size - 1)
            ele = self.heap.pop()
            self.size -= 1
            self.downheap(0)
            return ele

    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        if self.heap:
            return self.heap[0]

    def _leftchild(self, pos):
        return (2 * pos) + 1

    def _rightchild(self, pos):
        return (2 * pos) + 2

    def _parent(self, pos):
        return (pos - 1) // 2

    def _swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def _is_leaf(self, pos):
        return self._leftchild(pos) >= self.size

    def downheap(self, pos):
        if not self._is_leaf(pos):
            left = self._leftchild(pos)
            right = self._rightchild(pos)
            swap_child = None

            if left < self.size and self.comparator(self.heap[left], self.heap[pos]):
                swap_child = left

            if right < self.size and self.comparator(self.heap[right], self.heap[pos]):
                if swap_child is None or self.comparator(self.heap[right], self.heap[swap_child]):
                    swap_child = right

            if swap_child is not None:
                self._swap(pos, swap_child)
                self.downheap(swap_child)

    def upheap(self, pos):
        if pos != 0:
            parent = self._parent(pos)
            if self.comparator(self.heap[pos], self.heap[parent]):
                self._swap(pos, parent)
                self.upheap(parent)

    def _heapify(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.downheap(i)

    def is_empty(self):
        return len(self.heap) == 0

    def __repr__(self, index=0, level=0, prefix="Root: "):
        if index >= len(self.heap):
            return ""

        ret = "|\t" * level + prefix + repr(self.heap[index]) + "\n"
        left_index = self._leftchild(index)
        right_index = self._rightchild(index)

        if left_index < self.size:
            ret += self.__repr__(left_index, level + 1, prefix="L--- ")
        if right_index < self.size:
            ret += self.__repr__(right_index, level + 1, prefix="R--- ")

        return ret

    def __iter__(self):
        return iter(self.heap)
