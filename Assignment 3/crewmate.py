'''
    Python file to implement the class CrewMate
'''
from heap import Heap

def comp_treasures(t1, t2):
    if t1.get_priority() != t2.get_priority():
        return t1.get_priority() < t2.get_priority()
    return t1.id < t2.id

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        self.id = None
        self.load = 0
        self.treasures = []
        # self.completed_treasures = []
        self.idle_time = 0
    
    def assign_treasure(self, treasure):
        self.treasures.append(treasure)
        self.load += treasure.size

    def process_treasures(self):
        self.completed_treasures = []

        treas_heap = Heap(comp_treasures, [])  
        treas_heap.insert(self.treasures[0])   
        time = self.treasures[0].arrival_time  
        self.treasures[0].processed_time = 0   

        for tres in self.treasures[1:]:
            tres.processed_time = 0  

            while time < tres.arrival_time:
                if not treas_heap.is_empty():
                    top_treas = treas_heap.top()  
                    
                    time_left = tres.arrival_time - time
                    pros_time = min(top_treas.size - top_treas.processed_time, time_left)
                    top_treas.processed_time += pros_time
                    time += pros_time

                    if top_treas.processed_time == top_treas.size:
                        top_treas.completion_time = time
                        self.completed_treasures.append(treas_heap.extract())
                else:
                    time = tres.arrival_time
                    break
            treas_heap.insert(tres)

        while not treas_heap.is_empty():
            tres = treas_heap.extract()
            remaining_time = tres.size - tres.processed_time
            time += remaining_time
            tres.processed_time = tres.size
            tres.completion_time = time
            self.completed_treasures.append(tres)

        
    # def __repr__(self):
    #     return f'id:{self.id},load:{self.load + self.idle_time}'