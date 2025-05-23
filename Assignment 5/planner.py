from flight import Flight

class Planner:
    def __init__(self, flights):
        """The Planner
        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        self.num_flights = len(flights) + 1
        self.flights = flights
        self.flight_graph = []
        for flight in flights:
            start_city = flight.start_city
            n = max(flight.start_city, flight.end_city)
            if len(self.flight_graph) <= n:
                self.flight_graph.extend([[] for _ in range(n - len(self.flight_graph) + 1)])
            self.flight_graph[start_city].append(flight)

    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        if start_city == end_city:
            return []  

        num_flights = self.num_flights
        parent_flight = [None] * num_flights 
        min_time = [float('inf')] * num_flights 
        min_flights = [float('inf')] * num_flights  
        vis = [False] * num_flights  
        
        q = Queue()
        q.enqueue((0, None))  # (num_flights, previous_flight)
        best_steps = float('inf')
        while not q.is_empty():
            num_flights, prev_flight = q.dequeue()
        
            if prev_flight:
                city = prev_flight.end_city
                vis[prev_flight.flight_no] = True  
            else:
                city = start_city

            if city == end_city:
                best_steps = num_flights
            
            if num_flights > best_steps:
                break

            for flight in self.flight_graph[city]:

                if vis[flight.flight_no]:
                    continue

                if prev_flight is None:
                    if flight.departure_time < t1:
                        continue
                else:
                    if flight.departure_time < prev_flight.arrival_time + 20:
                        continue

                new_time = flight.arrival_time
                new_flights = num_flights + 1

                if (new_flights,new_time) < (min_flights[flight.flight_no],min_time[flight.flight_no]):
                    min_time[flight.flight_no] = new_time
                    min_flights[flight.flight_no] = new_flights
                    q.enqueue((new_flights, flight))
                    parent_flight[flight.flight_no] = prev_flight

        best_flight = None
        for flight in self.flights:
            if flight.end_city == end_city and min_time[flight.flight_no] <= t2:
                if best_flight is None or (min_flights[flight.flight_no], min_time[flight.flight_no]) < (min_flights[best_flight.flight_no], min_time[best_flight.flight_no]):
                    best_flight = flight

        if best_flight:
            path = self.construct_path(best_flight, parent_flight,start_city)
        else:
            path = []

        return path

    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        num_flights = self.num_flights
        parent_flight = [None] * num_flights 
        min_cost = [float('inf')] * num_flights 
        vis = [False] * num_flights  

        h = Heap(lambda a, b: a[0] < b[0])
        h.insert((0, None))  # (current cost, previous flight)

        last_flight = None  

        while not h.is_empty():
            cost, prev_flight = h.extract()

            if prev_flight:
                city = prev_flight.end_city
                vis[prev_flight.flight_no] = True 
            else:
                city = start_city

            if city == end_city and (prev_flight is None or prev_flight.arrival_time <= t2):
                last_flight = prev_flight
                break

            for flight in self.flight_graph[city]:
                if prev_flight is None:
                    if flight.departure_time < t1:
                        continue
                else:
                    if flight.departure_time < prev_flight.arrival_time + 20:
                        continue

                new_cost = cost + flight.fare

                if new_cost < min_cost[flight.flight_no] and not vis[flight.flight_no]:
                    min_cost[flight.flight_no] = new_cost
                    h.insert((new_cost, flight))
                    parent_flight[flight.flight_no] = prev_flight

        if last_flight and min_cost[last_flight.flight_no] != float('inf') and last_flight.arrival_time <= t2:
            path = self.construct_path(last_flight, parent_flight,start_city)
        else:
            path = []
        return path


    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """

        num_flights = self.num_flights
        parent_flight = [None] * num_flights  
        min_flights = [float('inf')] * num_flights
        min_cost = [float('inf')] * num_flights  
        vis = [False] * num_flights 

        h = Heap(lambda a, b: (a[0],a[1]) < (b[0],b[1]))
        h.insert((0, 0, None))  # (number of flights ,current cost, previous flight)

        last_flight = None  

        while not h.is_empty():
            num_flights, cost, prev_flight = h.extract()

            if prev_flight:
                city = prev_flight.end_city
                vis[prev_flight.flight_no] = True  
            else:
                city = start_city

            if city == end_city and (prev_flight is None or prev_flight.arrival_time <= t2):
                last_flight = prev_flight
                break

            for flight in self.flight_graph[city]:
                if prev_flight is None:
                    if flight.departure_time < t1:
                        continue
                else:
                    if flight.departure_time < prev_flight.arrival_time + 20:
                        continue

                
                new_cost = cost + flight.fare
                new_flights = num_flights + 1

                if (new_flights,new_cost) < (min_flights[flight.flight_no],min_cost[flight.flight_no]) and not vis[flight.flight_no]:
                    min_cost[flight.flight_no] = new_cost
                    min_flights[flight.flight_no] = new_flights
                    h.insert((new_flights,new_cost, flight))
                    parent_flight[flight.flight_no] = prev_flight
        
        if last_flight and min_cost[last_flight.flight_no] != float('inf') and last_flight.arrival_time <= t2:
            path = self.construct_path(last_flight, parent_flight,start_city)
        else:
            path = []
        return path
    
    def construct_path(self, last_flight, parent_flight, start_city):
        path = []
        flight = last_flight
        while flight:
            path.append(flight)
            if flight.start_city == start_city:  
                break
            flight = parent_flight[flight.flight_no]
        if not path or path[-1].start_city != start_city:
            return []  

        path.reverse()
        return path

class Queue:
    def __init__(self, initial_capacity=4):
        self.queue = [None] * initial_capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        self.capacity = initial_capacity

    def enqueue(self, item):
        if self.size == self.capacity:
            self._resize()

        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None 

        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def _resize(self):
        new_capacity = self.capacity * 2
        new_queue = [None] * new_capacity

        for i in range(self.size):
            new_queue[i] = self.queue[(self.front + i) % self.capacity]

        self.queue = new_queue
        self.front = 0
        self.rear = self.size
        self.capacity = new_capacity

    def __repr__(self):
        if self.is_empty():
            return "Queue([])"
        elements = []
        for i in range(self.size):
            elements.append(repr(self.queue[(self.front + i) % self.capacity]))
        return f"Queue[{', '.join(elements)}]"
class Heap:

    def __init__(self, comparison_function):
        self.comparator = comparison_function
        self.heap = []
        self.size = 0

    def insert(self, value):
        self.heap.append(value)
        size = len(self.heap)
        self.upheap(size - 1)
        self.size += 1

    def extract(self):
        if self.heap:
            self._swap(0, self.size - 1)
            ele = self.heap.pop()
            self.size -= 1
            self.downheap(0)
            return ele

    def top(self):
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

    def __iter__(self):
        return iter(self.heap)