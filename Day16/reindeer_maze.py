from collections import deque

type Position = tuple[int, int]
type Positions = list[Position]

type Path = list[Position]
type Paths = list[Path]

type Map = list[list[str]]

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
            if not (map[nx][ny] == '#' or (nx, ny) in path):
                queue.append(((nx, ny), path + [(nx, ny)]))

    return paths

def color_map_with_path(map: Map, path: Positions):
    for position in path:
        x, y = position
        if map[x][y] not in 'SE':
            map[x][y] = '|'

def find_lowest_score(paths) -> int:
    lowest_score: int = 0
    #dir = 
    #for path in paths:

    return lowest_score

# Expected result => 7036 & 11048
# Test 4 expected result, 4 different path, got 3
def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])
    for r in map: print(r)

    start, end = find_start_and_end(map, H, W)
    print(f"Start is {start}, end is {end}")

    paths = solve_maze(map, start, end)
    for i, path in enumerate(paths, 1):
        print(f"Chemin {i}: {path}")
        cpy_map = [[char for char in line] for line in map]
        color_map_with_path(cpy_map, path)
        for r in cpy_map: print(r)

    score: int = find_lowest_score(paths)
    print(f"Part 1: {score}")

if __name__ == "__main__":
    main()
