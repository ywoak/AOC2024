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

def dijkstra(graph: Map, distances: Distances, start: Position, end: Position) -> int:
    distances[start] = 0
    print(f"Distance after setting start is {distances}")
    pq: list[tuple[int, Position]] = [(0, start)] # (distance, node)
    score: int = 0
    cur_dir: int = 1 # Starting west
    directions: Positions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # Keep 90 degre rotation close to each other, to always have dir +1/-1

    # For each position, determine distance
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        x, y = current_node


        if current_distance > distances[current_node]:
            continue

        # Get neighbor and weight,
        # either do it with x, y destructur to reach all 4 neighbor
        # And then grab the weight depending on the direction we're looking
        # Or keep graph(current_node).items() but then modify graph, to have an adjacency list
        # Instead of the current map with only str without weight to destructur

        # for the 4 directions, have them 90 degre rotation
        # Keep a current direction, one starting west

        # for neighbor, weight in graph[x][y]:
        # 
        for dx, dy in (directions[cur_dir+1], directions[cur_dir-1]):
            nx, ny = x + dx, y + dy
            # if we're looking 90 degree, so current direction +1 or -1
            # weight is 1000
            # Else weight is 1

            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

        # Perhaps duplicate with only one other direction, because we have a direction im not sure if we need to check the 4 directions
        # We can never do a 180 degree
        dx, dy = (directions[cur_dir])
        nx, ny = x + dx, y + dy
        # if we're looking 90 degree, so current direction +1 or -1
        # weight is 1000
        # Else weight is 1

        distance = current_distance + weight

        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(pq, (distance, neighbor))

    return score

# Expected result => 7036 & 11048
# Test 4 expected result, 4 different path, got 3 -> Solved
def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])
    for r in map: print(r)

    start, end, distances = find_start_and_end(map, H, W)
    print(f"Start is {start}, end is {end}\n distance is {distances}")

    dijkstra(map, distances, start, end)

if __name__ == "__main__":
    main()
