class Direction:
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3

    @staticmethod
    def turn_90(direction):
        return {
            Direction.UP: Direction.RIGHT,
            Direction.RIGHT: Direction.DOWN,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP
        }[direction]

class Point:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

def turn_90(current):
    return Point(current.x, current.y, Direction.turn_90(current.direction))

def find_guard(grid):
    direction = Direction.UP
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "^":
                return Point(j, i, direction)
    return None

def get_next_step_with_direction_preserved(grid, current):
    next_point = Point(current.x, current.y, current.direction)
    if current.direction == Direction.UP:
        next_point.y -= 1
    elif current.direction == Direction.DOWN:
        next_point.y += 1
    elif current.direction == Direction.RIGHT:
        next_point.x += 1
    elif current.direction == Direction.LEFT:
        next_point.x -= 1

    if 0 <= next_point.x < len(grid[0]) and 0 <= next_point.y < len(grid):
        return True, next_point
    return False, next_point

def find_next_step(grid, current):
    valid, possible_next = get_next_step_with_direction_preserved(grid, current)
    if not valid:
        return False, possible_next

    cell = grid[possible_next.y][possible_next.x]
    if cell == "#":
        return find_next_step(grid, turn_90(current))
    elif cell in ".^":
        return True, possible_next
    return False, possible_next

def find_path(grid, start):
    path = {}
    count = 0
    current = start

    while True:
        coord = (current.x, current.y)
        if coord not in path:
            count += 1
            path[coord] = current.direction

        valid, new_current = find_next_step(grid, current)
        if not valid:
            return count, path
        current = new_current

def is_loop(grid, start):
    path = {}
    coord_path = set()
    current = start

    while True:
        if (current.x, current.y, current.direction) in path:
            return True
        path[(current.x, current.y, current.direction)] = True
        coord_path.add((current.x, current.y))

        valid, new_current = find_next_step(grid, current)
        if not valid:
            return False
        current = new_current

def find_new_obstacle_count(grid, start, path):
    count = 0
    obstacle_map = set()

    for step in path:
        if step == (start.x, start.y):
            continue

        if grid[step[1]][step[0]] == ".":
            grid[step[1]][step[0]] = "#"
            if is_loop(grid, start):
                if step not in obstacle_map:
                    count += 1
                    obstacle_map.add(step)
            grid[step[1]][step[0]] = "."

    return count

# Lecture de la grille depuis un fichier
def load_map(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f]

if __name__ == "__main__":
    grid = load_map("input.txt")
    start = find_guard(grid)
    path_count, path = find_path(grid, start)
    obstacle_count = find_new_obstacle_count(grid, start, path)

    print("Part 1:", path_count)
    print("Part 2:", obstacle_count)
