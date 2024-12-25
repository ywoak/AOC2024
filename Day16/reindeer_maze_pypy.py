from collections import deque

Position = tuple[int, int]
Positions = list[Position]

Path = list[Position]
Paths = list[Path]

Map = list[list[str]]

ScoreDict = dict[int, int]

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
    queue: deque[tuple[Position, Path]] = deque([(start, [start])])
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

def color_map_with_path(map: Map, path: Path):
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
        score: int = 0
        for i in range(len(path) - 1):
            x, y = path[i]
            nx, ny = path[i + 1]

            dx, dy = directions[orientation]

            if not ((nx == x + dx) and (ny == y + dy)):
                score += 1000
                orientation = directions.index((nx - x, ny - y))

            score += 1

        scores[P] = score

    return scores

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
# Test 4 expected result, 4 different path, got 3
def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])

    start, end = find_start_and_end(map, H, W)

    # Fast enough for actual input but reconstruct_paths is too slow then
    parents = bfs_all_paths(map, start, end)

    # Fast path reconstruction and path finding
    paths = []
    stack = [(end, [end])]

    while stack:
        (x, y), path = stack.pop()

        if (x, y) == start:
            paths.append(path)
            continue

        for px, py in parents[x][y]:
            if (px, py) not in path:
                stack.append(((px, py), path + [(px, py)]))

    scores = find_lowest_score(paths)
    min_key = min(scores, key=lambda k: scores[k])

    print(f"\nPart 1: {scores[min_key]}")

if __name__ == "__main__":
    main()
