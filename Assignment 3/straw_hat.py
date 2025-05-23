'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
from heap import Heap
import treasure

def comp_crewmates(c1, c2):
    return c1.load + c1.idle_time < c2.load + c2.idle_time

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        crewmates = []
        for i in range(m):
            member = crewmate.CrewMate()
            member.id = i+1
            crewmates.append(member)

        self.team = Heap(comp_crewmates, crewmates)
        self.working_crewmates = set()
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        time = treasure.arrival_time
        least_load_cm = self.team.top()

        if least_load_cm.load + least_load_cm.idle_time < time:
            least_load_cm.idle_time += time - (least_load_cm.load + least_load_cm.idle_time)

        least_load_cm.assign_treasure(treasure)
        self.working_crewmates.add(least_load_cm)
        self.team.downheap(0)
        
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        processed_treasures = []
        for crewmate in self.working_crewmates:
            
            crewmate.process_treasures()
            # print(crewmate.completed_treasures)
            processed_treasures.extend(crewmate.completed_treasures)
        
        processed_treasures.sort(key = lambda x: x.id)
        return processed_treasures

        
    # You can add more methods if required

    def print_team_state(self):

        print("Current state of the team:")
        for i, crewmate in enumerate(self.team.heap):
            print(f"Crewmate {crewmate.id}: Load = {crewmate.load}")
            print("Assigned Treasures:")
            print(crewmate.treasures)
            print("-" * 30)