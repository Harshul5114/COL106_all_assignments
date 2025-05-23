class Maze:
    def __init__(self, m: int, n : int) -> None:
        ## DO NOT MODIFY THIS
        ## We initialise the list with all 0s, as initially all cells are vacant
        self.grid_representation = []
        for row in range(m):
            grid_row = []
            for column in range(n):
                grid_row.append(0)
            self.grid_representation.append(grid_row)
    
    def add_ghost(self, x : int, y: int) -> None:
        if self._is_in_grid(x,y):
            self.grid_representation[x][y] = 1
        
    def remove_ghost(self, x : int, y: int) -> None:
        if self._is_in_grid(x,y):
            self.grid_representation[x][y] = 0

    def is_ghost(self, x : int, y: int) -> bool:
        if (self.grid_representation[x][y] == 1):
            return True
        else:
            return False
    def print_grid(self) -> None:
        for row in self.grid_representation:
            print(*row)

    def _is_in_grid(self, x: int, y: int) -> bool:
        cols = len(self.grid_representation)
        rows = len(self.grid_representation[0])
        return(x >= 0 and y >= 0 and x < cols and y < rows)








