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

def solve_maze(map: Map, start: tuple) -> PathPositions:
    # BFS
    x, y = start
    q: deque[Position] = deque([(x, y)])

    vis: PathPositions = defaultdict(list)
    vis[(x, y)].append(None)

    dirs: list = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        print(f"\nCurrent iteration, position: ({x, y})")

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            print(f"Looking at next direction for ({x, y}) in : ({nx, ny})")

            if map[nx][ny] == '#':
                print(f"It was a wall, ignore")
                continue

            if (nx, ny) not in vis:
                q.append((nx, ny))
                vis[(nx, ny)].append((x, y))
                print(f"It wasnt in visited yet, we add it to the queue, and to visited with parent being the current")
                print(f"q is {q}\nVis is {vis}")

            elif (nx, ny) not in vis[(x, y)]:
                # the next isn't our parent, aka we're not coming back on our map
                vis[(nx, ny)].append((x, y))
                # Add the current as a parent for the next

            ## Even if a path is visited, it can be visited through another path
            ## We can just remove vis or we would step backward on our own path
            ## ?????????????

            # We dont actually need to append a visited path to the queue again, because its bfs in all directions
            # We do need a way to track the chain of children-parent ?

            """
            start = 0, 0
            path 1, 0 -> 2, 0 -> 2, 1 -> 2,2

            child = 2, 2, parents = 2, 1

            alternate path same start same target at 2, 2
            path 0, 1 -> 0, 2 -> 1, 2 -> 2, 2

            Diff between 2, 2 and 0, 2 for alternate path is that 1, 2 is the parent of 0, 2
            So we are coming from here
            Lemma : We are always a parent to someone, since start is None
            """

#            elif (x, y) not in vis[(nx, ny)]:
#                print(f"The current ({x, y}) wasn't in the parent of the next ({nx, ny})")
#                vis[(nx, ny)].append((x, y))

    return vis

def reconstruct_paths(vis: PathPositions, end: Position) -> list[Positions]:
    paths: list[Positions] = []

    def backtrack(current: Position | None, path: Positions):
        if not current:
            paths.append(list(reversed(path)))
            return

        path.append(current)
        for prev in vis[current]:
            backtrack(prev, path)
        path.pop()

    backtrack(end, [])

    return paths

def color_map_with_path(map: Map, path: Positions):
    for position in path:
        x, y = position
        if map[x][y] not in 'SE':
            map[x][y] = '|'

# Expected result => 7036 & 11048
def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])
    for r in map: print(r)

    start, end = find_start_and_end(map, H, W)
    print(f"Start is {start}, end is {end}")

    vis = solve_maze(map, start)

    for key, neighbors in vis.items():
        formatted_neighbors = [str(neighbor) for neighbor in neighbors]
        print(f"Parent of {key} : {', '.join(formatted_neighbors)}")

    #paths = reconstruct_paths(vis, end)
    #print(f"paths {paths}")
    #for i, path in enumerate(paths):
    #    print(f"\nFor path number {i}")
    #    cpy_map = [[char for char in line] for line in map]
    #    color_map_with_path(cpy_map, path)


if __name__ == "__main__":
    main()
