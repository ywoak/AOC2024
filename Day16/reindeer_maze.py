import heapq

type Position = tuple[int, int]
type Positions = list[Position]

type Distances = dict[Position, float | int]

type Path = list[Position]
type Paths = list[Positions]

type Map = list[list[str]]

type ScoreDict = dict[int, int]

def load_map() -> Map:
    return [
        [char for char in line]
        for line in open(0).read().strip().split('\n')
    ]

def find_start_and_end(map: Map, H: int, W: int) -> tuple[Position, Position, Distances]:
    start: Position = (0, 0)
    end: Position = (0, 0)
    distances: Distances = dict()

    for x in range(H):
        for y in range(W):
            if map[x][y] == 'S':
                start = (x, y)
            elif map[x][y] == 'E':
                end = (x, y)
            distances[(x, y)] = float('inf')
    assert start != (0, 0) and end != (0, 0), "The map is incorrect"
    return start, end, distances

def dijkstra(graph: Map, distances: Distances, start: Position, end: Position) -> int | float:
    distances[start] = 0
    cur_dir: int = 1 # Starting position is East
    pq: list[tuple[int, Position, int]] = [(0, start, cur_dir)] # (distance, node, direction)

    # Keep 90 degre rotation close to each other for 4 rotations, to always have dir +1/-1
    directions: Positions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # South, East, North, West

    # For each position, determine distance
    while pq:
        current_distance, current_node, cur_dir = heapq.heappop(pq)
        x, y = current_node

        print(f"\nIm at position {x, y}")
        if current_distance > distances[current_node]: continue
        if (x, y) == end: continue

        # Get neighbor and weight,

        # either do it with x, y destructor to reach all 4 neighbor
        # And then grab the weight depending on the direction we're looking

        # Or keep graph(current_node).items() but then modify graph, to have an adjacency list
        # Instead of the current map with only str without weight to destructur

        # for neighbor, weight in graph[x][y]:
        for dx, dy in (directions[cur_dir], directions[(cur_dir + 1) % 4], directions[(cur_dir - 1) % 4]):
            nx, ny = x + dx, y + dy
            # Check for out of bound
            if graph[nx][ny] == '#': continue

            # if we're looking 90 degree, so current direction +1 or -1
            # weight is 1000
            weight = 1000
            # Else weight is 1
            print(f"\nIm looking at direction {nx, ny}")
            print(f"cur_dir is {cur_dir}")
            if ((dx, dy) == directions[cur_dir]):
                weight = 1

            if (dx, dy) == directions[(cur_dir + 1) % 4]:
                cur_dir = (cur_dir + 1) % 4
            elif (dx, dy) == directions[(cur_dir - 1) % 4]:
                cur_dir = (cur_dir - 1) % 4

            distance = current_distance + weight
            print(f"weight is {weight}, so new distance is {distance}")
            print(f"Old distance is {distances[(nx, ny)]}")

            if distance < distances[(nx, ny)]:
                distances[(nx, ny)] = distance
                heapq.heappush(pq, (distance, (nx, ny), cur_dir))

    print(f"Distances after dijkstra is:\n")
    for key, val in distances.items():
        x, y = key
        if graph[x][y] != '#':
            print(f"{key}: {val}")

    return distances[end]

# Expected result => 7036 & 11048
# Test 4 expected result, 4 different path, got 3 -> Solved
def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])
    for r in map: print(r)

    start, end, distances = find_start_and_end(map, H, W)
    print(f"Start is {start}, end is {end}\n")
    print(f"Distances before dijkstra is:\n {distances}\n")

    score: int | float = dijkstra(map, distances, start, end)
    print(f"Score is {score}")

if __name__ == "__main__":
    main()
