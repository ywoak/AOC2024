from collections import deque

type Position = tuple[int, int]
type Positions = list[Position]

type Path = list[Position]
type Paths = list[Positions]
#type Paths = list[tuple[Position, ...]]

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
    queue: deque[tuple[Position, Positions]] = deque([(start, [start])])
    paths: Paths = []

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            paths.append(path)
            continue

        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if map[nx][ny] != '#':
                if (nx, ny) not in path:
                    queue.append(((nx, ny), path + [(nx, ny)]))

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

def reconstruct_paths(parents, start, end):
    all_paths = []
    stack = [(end, [end])]

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == start:
            all_paths.append(path)
            continue

        for px, py in parents[x][y]:
            if (px, py) not in path:
                stack.append(((px, py), path + [(px, py)]))

    return all_paths

def reconstruct_paths_optimized(parents, start, end):
    all_paths = []
    stack = [(end, [end], set([end]))]

    while stack:
        (x, y), path, visited = stack.pop()

        if (x, y) == start:
            all_paths.append(path[:])
            #all_paths.append(path)
            print(f"Reconstructed {len(all_paths)} paths")
            continue

        print(f"For current {x, y}, there is {len(parents[x][y])} parent")
        for px, py in parents[x][y]:
            if (px, py) not in visited:
                stack.append(((px, py), path + [(px, py)], visited | {(px, py)}))

    return all_paths

def bfs_all_paths(map, start, end):
    """
    global visited doesn't allow to search all path
    No visited makes O(N) `in` __contains__ in every loop
    a local visited or a manual OrderedSet makes an O(N) copy in every loop
    Mutation fucks with for in iterable while doing it

    Going back to my previous idea of parent and then reconstruct paths, but this time instead of knowing if something is a parent because we visited it, which doesn't allow for a point to have multiple parents
    We use an array of parent for each position, with a bool array for global visited (prob faster than set)
    """
    H, W = len(map), len(map[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = [[False] * W for _ in range(H)]
    parents = [[[] for _ in range(W)] for _ in range(H)]

    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if map[nx][ny] != '#' and (nx, ny) != start:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    parents[nx][ny].append((x, y))
                    queue.append((nx, ny))
                elif (x, y) not in parents[nx][ny]:
                    parents[nx][ny].append((x, y))

    return parents

# Expected result => 7036 & 11048
# Test 4 expected result, 4 different path, got 3 -> Solved
def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])
    for r in map: print(r)

    start, end = find_start_and_end(map, H, W)
    print(f"Start is {start}, end is {end}")

    # To slow for actual input
    #paths: Paths = solve_maze(map, start, end)
    # Fast enough for actual input but reconstruct_paths is too slow then
    parents = bfs_all_paths(map, start, end)
    print("Parents of end:", parents[end[0]][end[1]])
    for r in parents: print(r)

    #paths = reconstruct_paths(parents, start, end)
    #paths = reconstruct_paths_optimized(parents, start, end)

    #print(f"Found {len(paths)} paths:")
    #for path in paths:
    #    print(path)

    #scores: ScoreDict = find_lowest_score(paths)
    #min_key = min(scores, key=lambda k: scores[k])
    #print(f"\nPart 1: {scores[min_key]}")

    #cpy_map = [[char for char in line] for line in map]
    #color_map_with_path(cpy_map, paths[min_key])
    #for r in cpy_map: print(r)

if __name__ == "__main__":
    main()
