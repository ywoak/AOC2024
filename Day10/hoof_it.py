from collections import defaultdict

type Map = list[list[str]]
type Pos = tuple[int, int]

type Score = defaultdict[Pos, int]

def load_map() -> Map:
    with open('test.txt') as f:
        input = f.read()
    map = [list(line) for line in input.strip().split('\n')]
    return map

def print_map(map: Map) -> None:
    print(f"\n Current map is ->")
    for r in map: print(r)

def dfs(map: Map, pos: Pos, visited: set[Pos], H: int, W: int, score: int) -> None:
    directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    if (pos not in visited):
        x, y = pos
        print(f"Current coord -> {x, y}")
        visited.add((x, y))
        print(f"Visited {visited}")

        if (int(map[x][y]) == 0):
            score += 1

        print_map(map)
        for direction in directions:
            dx, dy = x + direction[0], y + direction[1]
            if ((0 <= dx < H) and (0 <= dy < W) and ((dx, dy) not in visited) and (int(map[dx][dy]) == int(map[x][y]) + 1)):
                return dfs(map, (dx, dy), visited, H, W, score)

def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])

    dfs(map, (0, 0), set(), H, W, 0)

if __name__ == '__main__':
    main()
