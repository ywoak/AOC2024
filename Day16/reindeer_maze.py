from collections import defaultdict, deque

type Position = tuple[int, int]
type Positions = list[Position]
type PrevPosition = Position
type PrevPositions = list[PrevPosition | None]

type SetPositions = set[Position]
type PathPositions = defaultdict[Position, PrevPositions]

type Map = list[list[str]]

def load_map() -> Map:
    return [
        [char for char in line]
        for line in open(0).read().strip().split('\n')
    ]

def find_start(map: Map, H: int, W: int) -> Position:
    for x in range(H):
        for y in range(W):
            if map[x][y] == 'S':
                return x, y
    return 0, 0

def solve_maze(map: Map, start: Position) -> tuple[PathPositions, Position]:
    # BFS
    x, y = start
    q: deque[Position] = deque([(x, y)])
    vis: PathPositions = defaultdict(list)
    vis[(x, y)].append(None)
    dirs: Positions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    end: Position = (0, 0)

    while q:
        x, y = q.pop()
        if map[x][y] == 'E':
            end = (x, y)
            print(f'Reached end at {x, y}')
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if (map[nx][ny] == '#' or (nx, ny) in vis): continue
            vis[(nx, ny)].append((x, y))
            q.append((nx, ny))
    return vis, end

def reconstruct_path(vis: PathPositions, end: Position) -> Positions:
    path: Positions = []
    current: Position | None = end

    while current is not None:
        x, y = current
        path.append((x, y))
        current = vis[(x, y)][0]

    assert len(path) == len(set(path))

    return list(reversed(path))

def color_map_with_path(map: Map, path: Positions):
    for position in path:
        x, y = position
        if map[x][y] not in 'SE':
            map[x][y] = '|'

def main():
    map = load_map()
    H, W = len(map), len(map[0])
    x, y = find_start(map, H, W)
    vis, end = solve_maze(map, (x, y))
    path = reconstruct_path(vis, end)
    color_map_with_path(map, path)

    for r in map: print(r)
    #print(f"{x, y}")
    #print(f"visited is {vis}")
    #print(f"visited is {path}")

if __name__ == "__main__":
    main()
