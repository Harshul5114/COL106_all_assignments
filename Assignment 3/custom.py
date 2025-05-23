# Assuming the necessary imports and the other classes are defined properly
# Test case for StrawHatTreasury
from treasure import *
from crewmate import *
from straw_hat import *
# Initialize a treasury with 3 crew members
treasury = StrawHatTreasury(3)

# Create some Treasure objects
treasure1 = Treasure(id=1, size=10, arrival_time=0)
treasure2 = Treasure(id=2, size=20, arrival_time=1)
treasure3 = Treasure(id=3, size=15, arrival_time=2)
treasure4 = Treasure(id=4, size=25, arrival_time=3)
print(treasury.team)

# Add the treasures to the treasury
treasury.add_treasure(treasure1)
print(treasury.team)

treasury.add_treasure(treasure2)
print(treasury.team)

treasury.add_treasure(treasure3)
print(treasury.team)

treasury.add_treasure(treasure4)



# (Optional) Print out the state of the team after adding treasures
# Assuming CrewMate and Heap classes have a proper __repr__ or similar method
print(treasury.team)
treasury.print_team_state()
print(treasury.get_completion_time())
