from collections import deque

type Position = tuple[int, int]
type Positions = list[Position]

type Path = list[Position]
type Paths = list[Path]

type Map = list[list[str]]

type ScoreDict = dict[int, int]

class OrderedSet:
    def __init__(self):
        self.items = []
        self.set = set()

    def add(self, item):
        if item not in self.set:
            self.items.append(item)
            self.set.add(item)

    def __contains__(self, item):
        return item in self.set

    def __iter__(self):
        return iter(self.items)

    def __len__(self):
        return len(self.items)


def load_map() -> Map:
    return [
        [char for char in line]
        for line in open(0).read().strip().split('\n')
    ]

def find_start_and_end(map: Map, H: int, W: int) -> tuple[Position, Position]:
    start: Position = (0, 0)
    end: Position = (0, 0)

    for x in range(H):
        for y in range(W):
            if map[x][y] == 'S':
                start = (x, y)
            elif map[x][y] == 'E':
                end = (x, y)
    return start, end

def solve_maze(map: Map, start: Position, end: Position) -> Paths:
    queue: deque[tuple[Position, OrderedSet]] = deque()
    initial_path = OrderedSet()
    initial_path.add(start)
    queue.append((start, initial_path))

    paths: Paths = []

    print(f"We're solving the maze")
    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            paths.append(list(path.items))
            print(f"We reached an end")
            continue

        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if not (map[nx][ny] == '#' or (nx, ny) in path):
                cpy_path = OrderedSet()
                cpy_path.items = path.items[:]
                cpy_path.set = path.set.copy()
                cpy_path.add((nx, ny))

                queue.append(((nx, ny), cpy_path))

    print(f"We solved the maze")
    return paths

def color_map_with_path(map: Map, path: Positions):
    for position in path:
        x, y = position
        if map[x][y] not in 'SE':
            map[x][y] = '|'

def find_lowest_score(paths: Paths) -> ScoreDict:
    """
    Iterate each path to verify which cost the lowest score
    Turning cost 1000, Moving forward once cost 1
    We start by looking east
    We never do a 180 turn
    """
    directions: Positions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    scores: ScoreDict = dict()

    for P, path in enumerate(paths):
        orientation = 1 # Start East
        #print(f"\nFor path {j} ->")
        score: int = 0
        for i in range(len(path) - 1):
            x, y = path[i]
            nx, ny = path[i + 1]
            #print(f"We are on {x, y}, we are taking into account {nx, ny}")
            dx, dy = directions[orientation]

            if not ((nx == x + dx) and (ny == y + dy)):
                score += 1000
                orientation = directions.index((nx - x, ny - y))
                #print(f"For path {path}\nNew orientation is {orientation} from node ({x, y}) to node ({nx, ny})")
            #print(f"We move forward")
            score += 1

        #print(f"Final score for path is {score}")
        scores[P] = score

    return scores

# Expected result => 7036 & 11048
# Test 4 expected result, 4 different path, got 3
def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])
    #for r in map: print(r)

    start, end = find_start_and_end(map, H, W)
    #print(f"Start is {start}, end is {end}")

    paths = solve_maze(map, start, end)
    #for i, path in enumerate(paths, 1):
        #print(f"Chemin {i}: {path}")

    scores: ScoreDict = find_lowest_score(paths)


#    directions: Positions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#    orientation = 1 # Start East

    min_key = min(scores, key=lambda k: scores[k])

#    cpy_map = [[char for char in line] for line in map]
#    color_map_with_path(cpy_map, paths[min_key])
#    for r in cpy_map: print(r)
#
#    score: int = 0
#    for i in range(len(paths[min_key]) - 1):
#        x, y = paths[min_key][i]
#        nx, ny = paths[min_key][i + 1]
#        #print(f"\nWe are on {x, y}, we are looking at {nx, ny}")
#        dx, dy = directions[orientation]
#
#        if not ((nx == x + dx) and (ny == y + dy)):
#            score += 1000
#            orientation = directions.index((nx - x, ny - y))
#            print(f"TURN AT {x, y} -> {orientation}")
#
#        #print(f"We move forward")
#        score += 1
#
#    print(f"SCOORUUUUU is {score}")

    print(f"\nPart 1: {scores[min_key]}")

if __name__ == "__main__":
    main()
