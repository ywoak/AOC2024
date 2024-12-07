# Get input
with open('input.txt') as f:
    input = (f.read())

type Map = list[list[str]] #list[list[char]]
type Coord = tuple[int, int]

# Find our guard
def find_guard() -> Coord :
    for i, r in enumerate(map):
        for j, c in enumerate(r):
            if c == '^':
                return(i, j)
    return (0,0) # Just to comply, there is always a lab guard

# Mark his shift and count his steps
def get_count(map: Map, start: Coord) -> int:
    steps = 1
    x, y = start
    while (x > 0):
        # The guard is at a new step
        # Dont include it if its a position he already marked
        if (map[x][y] != 'X'):
            steps += 1
            map[x][y] = 'X'

        # We dont need to check for safety :
        # - y is never OOB, the map is rectangular and always rotate in bound
        # - x never wrap as -1 because we stop the loop before
        if (map[x-1][y] == '#'):
            map, pos = rotate(map, x, y)
            x, y = pos
        else:
            x -= 1;
    return steps

# Rotate map 90 to the left
def rotate(map: Map, x: int, y: int):
    new_y = x
    new_x = len(map[x]) - 1 - y
    rotated = [list(e) for e in list(reversed(list(zip(*map))))]
    return list(rotated), (new_x, new_y)

# Make map out of input
map :Map = [list(c) for c in input.strip().split('\n')]
player_pos: Coord = find_guard()
print(get_count(map, player_pos))
