from enum import Enum

with open('input.txt') as f:
    input = (f.read())

type Coord = tuple[int, int]
type Pos = tuple[Coord, Coord, Coord, Coord]
type ExactPos = tuple[int, int, Direction]

type Map = list[list[str]] #list[list[char]]
type Path = dict[ExactPos, None]

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Player:
    def __init__(self, position, direction) -> None:
        self.position: Coord = position
        self.direction: Direction = direction
        self._relative_pos: Pos = ((-1,0), (0, 1), (1, 0), (0, -1))

    def move_forward(self, map) -> bool:
        x, y = self.position
        rel_x, rel_y = self._relative_pos[self.direction.value]
        new_x, new_y = x + rel_x, y + rel_y
        if map[new_x][new_y] == '#':
            return False
        self.position = (new_x, new_y)
        return True

    def turn_right(self) -> None:
        self.direction = Direction((self.direction.value + 1) % 4)

    def in_bound(self, map: Map, position: Coord) -> bool:
        x, y = position
        return (0 < x < len(map) - 1 and 0 < y < len(map[x]) - 1)

def find_guard() -> Coord :
    for i, r in enumerate(map):
        for j, c in enumerate(r):
            if c == '^':
                return(i, j)
    return (0,0)

def trace_path(map: Map, player: Player) -> int:
    visited: Path = {}
    correct_obstacle = 1
    while player.in_bound(map, player.position):
        x, y = player.position
        x_cpy = x
        y_cpy = y
        map[x][y] = 'X'

        to_right = Direction((player.direction.value + 1) % 4)

        while(map[x_cpy][y_cpy] != '#' and (0 < x_cpy < len(map) - 1 and 0 < y_cpy < len(map[x]) - 1)):
            rel_x, rel_y = player._relative_pos[to_right.value]
            new_x, new_y = x_cpy + rel_x, y_cpy + rel_y
            if ((new_x, new_y, to_right) in visited):
                correct_obstacle += 1
                break
            x_cpy = new_x
            y_cpy = new_y

        visited[(x, y, player.direction)] = None

        if not (player.move_forward(map)):
            player.turn_right()
    return correct_obstacle;

#test = "....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."
#map :Map = [list(c) for c in test.strip().split('\n')]
map :Map = [list(c) for c in input.strip().split('\n')]
player: Player = Player(find_guard(), Direction.UP)
print(trace_path(map, player))
