from pprint import pprint
import random


class Cell:
    def __init__(self, x, y):
        self.walls = {
            'n': True,
            'e': True,
            's': True,
            'w': True,
        }
        self.visited = False
        self.x = x
        self.y = y
    
    def remove_wall(self, dir):
        self.walls[dir] = False
    
    def visit(self):
        self.visited = True

    def get_neighbors(self, board):
        a = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        neighbors = []
        for x, y in a:
            if self.x+x in [len(board), -1] or self.y+y in [-1, len(board)]:
                continue
            
            child = board[self.y+y][self.x+x]
            if child.visited:
                continue
            neighbors.append(child)
        return neighbors
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

def remove_walls(curr, target):
    if target.x > curr.x:
        curr.remove_wall('e')
        target.remove_wall('w')
    elif target.x < curr.x:
        curr.remove_wall('w')
        target.remove_wall('e')
    elif target.y > curr.y:
        curr.remove_wall('s')
        target.remove_wall('n')
    elif target.y < curr.y:
        curr.remove_wall('n')
        target.remove_wall('s')


def drawWalls(grid: list, binGrid: list) -> list:
    """Draw existing walls around Cells"""
    for yindex, y in enumerate(grid):
        for xindex, x in enumerate(y):
            for i, w in enumerate(x.walls.values()):
                if i == 3 and w:
                    binGrid[yindex*2+1][xindex*2] = '⬛'
                if i == 1 and w:
                    binGrid[yindex*2+1][xindex*2+2] = '⬛'
                if i == 0 and w:
                    binGrid[yindex*2][xindex*2+1] = '⬛'
                if i == 2 and w:
                    binGrid[yindex*2+2][xindex*2+1] = '⬛'
    return binGrid


def drawBorder(grid: list) -> list:
    """Draw a border around the maze"""
    length = len(grid)
    for row in grid:
        row[0] = row[length-1] = '⬛'
        
    grid[0] = grid[length-1] = ['⬛'] * length
    return grid


def displayMaze(grid: list):
    """Draw the maze using ASCII characters and display the maze"""
    binGrid = []
    length = len(grid)*2+1
    for x in range(length):
        if x % 2 == 0:
            binGrid.append(['⬜' if x % 2 != 0 else '⬛' for x in range(length)])
        else:
            binGrid.append(['⬜'] * length)
    
    binGrid = drawWalls(grid, binGrid)
            
    binGrid = drawBorder(binGrid)

    print('\n'.join([''.join(x) for x in binGrid]))


size = int(input('Enter a maze size: '))
board = [[Cell(x, y) for x in range(size)] for y in range(size)]
current = board[0][0]
stack = []

# Main loop to generate the maze
while True:
    current.visited = True
    children = current.get_neighbors(board)

    if children:
        choice = random.choice(children)
        choice.visited = True
        stack.append(current)
        remove_walls(current, choice)
        current = choice
    elif stack:
        current = stack.pop()
    else:
        break

displayMaze(board)