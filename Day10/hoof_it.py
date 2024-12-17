from collections import deque

type Map = list[list[str]]
type Pos = tuple[int, int]

def load_map() -> Map:
    with open('input.txt') as f:
        input = f.read()
    map = [list(line) for line in input.strip().split('\n')]
    return map

def bfs(map: Map, H: int, W: int, pos: Pos) -> int:
    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    top = 0 # Make it a set and return its length for part 1
    q = deque([(pos[0], pos[1])])

    while q:
        x, y = q.popleft()
        for nx, ny in directions:
            dx, dy = x + nx, y + ny
            if not ((0 <= dx < H) and (0 <= dy < W) and int(map[dx][dy]) == int(map[x][y]) + 1): continue
            if (int(map[dx][dy]) == 9):
                top += 1
            else:
                q.append((dx, dy))
    return top

def find_trailhead(map: Map) -> list[Pos]:
    trailheads = []
    for row, R in enumerate(map):
        for col, char in enumerate(R):
            if (char == '0'):
                trailheads.append((row, col))
    return trailheads

def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])

    trailheads: list[Pos] = find_trailhead(map)
    print(f"trailheads {trailheads}")
    score = sum(bfs(map, H, W, trailhead) for trailhead in trailheads)
    print(f"Part 1: {score}")

if __name__ == '__main__':
    main()
