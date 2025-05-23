import hash_table as ht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    def __init__(self, book_titles, texts):
        self.book_titles = book_titles[:]
        self.texts = texts[:]
        
        for i in range(len(self.texts)):
            self.texts[i] = self._merge_sort(self.texts[i])
            distinct_words = [self.texts[i][0]]
            for j in range(1, len(self.texts[i])):
                if self.texts[i][j-1] != self.texts[i][j]:
                    distinct_words.append(self.texts[i][j])
            self.texts[i] = distinct_words

        self.books = list(zip(self.book_titles, self.texts))
        self.books = self._merge_sort(self.books)

    def distinct_words(self, book_title):
        index = self._binary_search(list(map(lambda x: x[0], self.books)), book_title)
        return self.books[index][1]
    
    def count_distinct_words(self, book_title):
        index = self._binary_search(list(map(lambda x: x[0], self.books)), book_title)
        return len(self.books[index][1])
    
    def search_keyword(self, keyword):
        book_titles = []
        for book in self.books:
            if self._binary_search(book[1], keyword) != -1:
                book_titles.append(book[0])
        return book_titles

    def print_books(self):
        for book in self.books:
            print(book[0], end=': ')
            print(*book[1], sep=' | ')

    def _merge(self, left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        return self._merge(left, right)

    def _binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


        
class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        self.name = name
        self.params = params
        if self.name == 'Jobs':
            self.collision_type = 'Chain'
        elif self.name == 'Gates':
            self.collision_type = 'Linear'
        else:
            self.collision_type = 'Double'

        self.bookmap = ht.HashMap(self.collision_type, self.params)
 

    def add_book(self, book_title, text):
        text_set = ht.HashSet(self.collision_type, self.params)
        for i in text:
            text_set.insert(i)
       
        self.bookmap.insert((book_title,text_set))
    
    def distinct_words(self, book_title):
        text_set = self.bookmap.find(book_title)
        words_list = text_set.contents()
        return words_list

    
    def count_distinct_words(self, book_title):
        return self.bookmap.find(book_title).num_elements
    
    def search_keyword(self, keyword):
        keybooks = []
        for i in self.bookmap.contents():   
            text = self.bookmap.find(i)   
            if text.find(keyword):
                keybooks.append(i)
    
        return keybooks
    
    def print_books(self):
 
        for book_title in self.bookmap.contents():
            text_set = self.bookmap.find(book_title)
            print(f"{book_title}: {text_set}")
            



