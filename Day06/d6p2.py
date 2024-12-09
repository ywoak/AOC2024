from enum import Enum
import ipdb

with open('input.txt') as f:
    input = (f.read())

type Coord = tuple[int, int]
type Pos = tuple[Coord, Coord, Coord, Coord]

type Map = list[list[str]] #list[list[char]]
type Path = dict[Coord, None]

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
        return (x > 0 and x < len(map) - 1 and y > 0 and y < len(map[x]) - 1)

def find_guard() -> Coord :
    for i, r in enumerate(map):
        for j, c in enumerate(r):
            if c == '^':
                return(i, j)
    return (0,0) # Just to comply, there is always a lab guard

# Mark his shift
# Store the place he visited in order
def trace_path(map: Map, player: Player) -> int:
    visited: Path = {}
    correct_obstacle = 0
    while player.in_bound(map, player.position):
#        ipdb.set_trace()
        x, y = player.position
        map[x][y] = 'X'
        print('\n')
        if (player.position in visited):
            os = list(visited)
            i = os.index(player.position)
            rel_x, rel_y = player._relative_pos[(player.direction.value + 1) % 4]
            new_x, new_y = x + rel_x, y + rel_y
            if (i+1 < len(os) and new_x == os[i+1][0] and new_y == os[i+1][1]):
                correct_obstacle += 1
        for r in map: print(r)
        visited[player.position] = None

        if not (player.move_forward(map)):
            player.turn_right()
            print(player.direction)
    return correct_obstacle;

#map :Map = [list(c) for c in input.strip().split('\n')]
test = "....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."
map :Map = [list(c) for c in test.strip().split('\n')]
player: Player = Player(find_guard(), Direction.UP)
print(trace_path(map, player))
