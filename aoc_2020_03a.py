# aoc_2020_03a
import sys
from aoc_io import get_input

inp = get_input(__file__, test=False if len(sys.argv) == 1 else True)
grid = [[0 if ch == '.' else 1 if ch == '#' else -1 for ch in [*line]] for line in inp.splitlines()]
orig_grid = grid
x, y, total = 0, 0, 0

def step(x, y):
    global grid
    if x + 3 >= len(grid[y]):
        grid = [grid[y] + orig_grid[y] for y in range(0, len(grid))]    
    tree = grid[y + 1][x + 3]
    return tree

while y < len(grid) - 2:
    total += step(x, y)
    x += 3; y += 1
print(f'Total trees: {total}')
