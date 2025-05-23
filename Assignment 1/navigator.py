from maze import *
from exception import *
from stack import *

class PacMan:
    navigator_maze = []
    def __init__(self, grid):
        self.navigator_maze = grid.grid_representation
        
    def find_path(self, start, end):
        # IMPLEMENT FUNCTION HERE
        
        if (self.navigator_maze[start[0]][start[1]] == 1 or self.navigator_maze[end[0]][end[1]] == 1):
            raise PathNotFoundException
            
        cols = len(self.navigator_maze)
        rows = len(self.navigator_maze[0])
        path = Stack()
        stk = Stack()
        
        visited = [[False] * rows for _ in range(cols)]
        parent = [[(0,0)] * rows for _ in range(cols)]
        
        def check(x: int, y: int) :
            return(x >= 0 and y >= 0 
                   and x < cols and y < rows 
                   and not visited[x][y] 
                   and self.navigator_maze[x][y] != 1)
                   
        stk.push(start)
        directions = {(1,0),(0,1),(-1,0),(0,-1)}
        
        found = False
        while not stk.is_empty():
            x,y = stk.pop()
            visited[x][y] = True
            
            if (x,y) == end:
                found = True
                break
                
            for dx,dy in directions:
                
                if check(x+dx, y+dy):
                    
                    stk.push((x+dx , y+dy))
                    parent[x+dx][y+dy] = (x,y)
            
        if found:
            path.push(end)
            
            while path.peek() != start:
                px,py = path.peek()
                path.push(parent[px][py])
                
            length = path.size()
            return [path.pop() for _ in range(length)]
            
        raise PathNotFoundException