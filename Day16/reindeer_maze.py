from collections import deque
import heapq

type Position = tuple[int, int]
type Positions = list[Position]

type Path = list[Position]
type Paths = list[Positions]
#type Paths = list[tuple[Position, ...]]

type Map = list[list[str]]

type ScoreDict = dict[int, int]

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
    assert start != (0, 0) and end != (0, 0), "The map is incorrect"
    return start, end

def dijkstra(graph: Map, start: Position, end: Position) -> int:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # (distance, node)
    score = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Expected result => 7036 & 11048
# Test 4 expected result, 4 different path, got 3 -> Solved
def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])
    for r in map: print(r)

    start, end = find_start_and_end(map, H, W)
    print(f"Start is {start}, end is {end}")

    dijkstra(map, start, end)

if __name__ == "__main__":
    main()
