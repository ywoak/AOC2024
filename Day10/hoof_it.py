from collections import defaultdict, deque

type Map = list[list[str]]
type Pos = tuple[int, int]

type Score = defaultdict[Pos, int]
type Path = dict[Pos, Pos]

def load_map() -> Map:
    with open('input.txt') as f:
        input = f.read()
    map = [list(line) for line in input.strip().split('\n')]
    return map

def bfs(map, H, W, pos):
    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    top = 0
    q = deque()
    q.append((pos[0], pos[1]))

    while q:
        x, y = q.popleft()
        for direction in directions:
            dx, dy = x + direction[0], y + direction[1]
            #if (0 > dx >= H) or (0 > dy >= W): continue
            if 0 > dx or 0 > dy or dx >= H or dy >= W: continue
            if int(map[dx][dy]) != int(map[x][y]) + 1: continue
            if (int(map[dx][dy]) == 9):
                print("FIND A 9")
                top += 1
            else:
                print("Nothing")
                q.append((dx, dy))
    return top

def dfs(map: Map, H: int, W: int, pos: Pos = (0, 0), visited: set[Pos] = set(), prev: Path = dict(), top: int = 0) -> int:
    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    if (pos not in visited):
        x, y = pos
        visited.add((x, y))
        if (int(map[x][y]) == 9):
            if (x, y in visited):
                top += 1
        else:
            for direction in directions:
                dx, dy = x + direction[0], y + direction[1]
                if ((0 <= dx < H) and (0 <= dy < W) and ((dx, dy) not in visited) and (int(map[dx][dy]) == int(map[x][y]) + 1)):
                    prev[(dx, dy)] = (x, y)
                    return dfs(map, H, W, (dx, dy), visited, prev, top)
    return top

def find_trailhead(map: Map) -> list[Pos]:
    trailheads = []
    for row, R in enumerate(map):
        for col, char in enumerate(R):
            if (char == '0'):
                trailheads.append((row, col))
    return trailheads

def reconstruct_path(map: Map, prev: Path, trailhead: Pos) -> list[list[Pos]]:
    paths = []

    final = [e for e in (set(prev.keys()) - set(prev.values())) if map[e[0]][e[1]] == '9']

    for pos_final in final:
        path = []
        curr = pos_final

        while (curr in prev) and (curr is not trailhead):
            path.append(curr)
            curr = prev[curr]

        path.append(trailhead)

        paths.append(path[::-1])
    return paths

def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])

    trailheads: list[Pos] = find_trailhead(map)
    print(f"trailheads {trailheads}")
    score = sum(bfs(map, H, W, trailhead) for trailhead in trailheads)
    print(f"Part 1: {score}")

if __name__ == '__main__':
    main()
