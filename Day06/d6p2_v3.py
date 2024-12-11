from enum import Enum

type Map = list[str]

type Coord = tuple[int, int]
type Visited = set[Coord]

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
    return (0 <= guard.x < hMap and 0 <= guard.y < wMap)

def load_map() -> Map:
    try:
        with open("input.txt") as f:
            input = f.read()
        map: Map = input.strip().split('\n')
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

def get_guard_path(map: Map, guard: Guard, H: int, W: int) -> int:
    visited: Visited = set()
    while True:
        visited.add((guard.x, guard.y))
        forward = guard.look_forward()
        if not (is_in_bound(H, W, forward)):
            break
        if map[forward.x][forward.y] == '.':
            guard.move_forward()
        else:
            guard.turn_right()
    return len(visited)

def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])
    guard: Guard = find_guard(map)

    print(f"part 1 : {get_guard_path(map, guard, H, W)}")

if __name__ == '__main__':
    main()
