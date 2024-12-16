from collections import deque

type Map = list[list[str]]
type Pos = tuple[int, int]

def load_map() -> Map:
    with open('test2.txt') as f:
        input = f.read()
    map = [list(line) for line in input.strip().split('\n')]
    return map

def print_map(map: Map) -> None:
    print(f"\n Current map is ->")
    for r in map: print(r)

def bfs(map: Map, queue: deque, visited: set[Pos], H: int, W: int) -> None:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while (queue):
        x, y = queue.popleft()
        print(f"Current coord -> {x, y}")
        visited.add((x, y))
        print(f"Visited {visited}")
        map[x][y] = '~'
        print_map(map)
        for direction in directions:
            dx, dy = x + direction[0], y + direction[1]
            if ((0 <= dx < H) and (0 <= dy < W) and ((dx, dy) not in queue) and ((dx, dy) not in visited)):
                queue.append((dx, dy))

def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])
    for r in map: print(r)

    queue = deque()
    queue.append((0, 0))
    bfs(map, queue, set(), H, W)

if __name__ == '__main__':
    main()
