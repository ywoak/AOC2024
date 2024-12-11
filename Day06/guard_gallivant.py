from enum import Enum

type Map = list[list[str]]

type Coord = tuple[int, int]
type CoordAndDirection = tuple[int, int, Direction]

# We keep the direction for the second part
type Visited = set[Coord]
type VisitedWithDirection = set[CoordAndDirection]

# As an enum allow easy manipulation of relative dir for next step with guard._dirs
class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Guard:
    _dirs = ((-1,0), (0,1), (1,0), (0,-1))

    def __init__(self, x: int, y: int, direction: Direction = Direction.UP) -> None:
        self.x = x
        self.y = y
        self.direction = direction

    def __repr__(self) -> str:
        return f"Guard(x={self.x}, y={self.y}, direction={self.direction.name})"

    def turn_right(self):
        self.direction = Direction((self.direction.value + 1) % 4)

    def look_forward(self) -> "Guard":
        return Guard(self.x + self._dirs[self.direction.value][0], self.y + self._dirs[self.direction.value][1], self.direction)

    def move_forward(self) -> None:
        self.x = self.x + self._dirs[self.direction.value][0]
        self.y = self.y + self._dirs[self.direction.value][1]

def is_in_bound(hMap: int, wMap: int, guard: Guard):
    '''
    Checking if the guard position is in the map
    This function is not a Guard method because :
    - It relies on the map
    - We can more explicitely use it with another guard (when `guard.look_forward()`)
    '''
    return (0 <= guard.x < hMap and 0 <= guard.y < wMap)

def load_map() -> Map:
    '''
    Load input.txt
    map every line as a list in a list of every line and return it
    '''
    try:
        with open("input.txt") as f:
            input = f.read()
        map: Map = [list(line) for line in input.strip().split('\n')]
        return map
    except FileNotFoundError:
        raise FileNotFoundError("Input file is not found")
    except Exception as e:
        raise RuntimeError("Issue with loading and reading the input file") from e

def find_guard(map) -> Guard:
    guard = Guard(0, 0)
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if col == '^':
                return Guard(i, j, Direction.UP)
    return guard

def get_guard_path(map: Map, guard: Guard, H: int, W: int) -> tuple[int, Visited]:
    '''
    O(N), keep a set of visited area for O(1) insertion while mapping the guard path
    '''
    visited: Visited = set()
    while True:
        visited.add((guard.x, guard.y))
        forward = guard.look_forward()
        if not (is_in_bound(H, W, forward)):
            break;
        if map[forward.x][forward.y] == '.':
            guard.move_forward()
        else:
            guard.turn_right()
    return len(visited), visited

def is_loop(map: Map, guard: Guard, H: int, W: int):
    '''
    We define a loop if before being out of bound, by mapping the guard path, we meet a place he already visited, while facing the same direction
    '''
    visited: VisitedWithDirection = set()
    while True:
        if ((guard.x, guard.y, guard.direction) in visited):
            return True
        visited.add((guard.x, guard.y, guard.direction))
        forward = guard.look_forward()
        if not (is_in_bound(H, W, forward)):
            return False
        if map[forward.x][forward.y] == '#':
            guard.turn_right()
        else:
            guard.move_forward()

def get_correct_obstacle(map, guard, H, W, visited) -> int:
    '''
    We use the part 1 `visited` set to try to put an obstacle at each position, and see if there will be a loop
    We could also remove the positions before #, but the gain would be marginal, and we would have to modify the part 1 result
    '''
    obstacle = 0
    for row, col in visited:
        if map[row][col] == '.' and not (row == guard.x and col == guard.y):
            map[row][col] = '#'
            if is_loop(map, Guard(guard.x, guard.y, guard.direction), H, W):
                obstacle += 1
            map[row][col] = '.'
    return obstacle

def main():
    '''
    21 seconds without Pypy
    '''
    map: Map = load_map()
    guard: Guard = find_guard(map)
    H, W = len(map), len(map[0])

    visited_num, visited = get_guard_path(map, Guard(guard.x, guard.y, guard.direction), H, W)
    obstacle_num = get_correct_obstacle(map, guard, H, W, visited)

    print(f"Part 1 : {visited_num}")
    print(f"Part 2 : {obstacle_num}")

if __name__ == '__main__':
    main()
