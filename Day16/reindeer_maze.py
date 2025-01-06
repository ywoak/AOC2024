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
    """
    Keep 4 directions next to each other clockwise, to be able to always look at possible directions with +1/-1
    Always checking only 3 directions, since we have where we came from, no need to check behind us
    Starting position is East

    Standard Dijkstra for the rest, getting the weight depending on where we looking, and the next direction to put in the heap
    The heap is pq, with (distance, node, direction)

    If we are somewhere we've already been but distance was lower, no need to continue this path
    If we reach the end, end it (not sure if its needed, but it's supposed to be faster)

    Checking for out of bound only done with obstacle #, because it surrounds the map, so we never get out

    This function "can" return float, but it will always return int on a correct maze, inf should never be the answer, I will even assert it
    """
    distances[start] = 0
    cur_dir: int = 1
    pq: list[tuple[int, Position, int]] = [(0, start, cur_dir)]

    directions: Positions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while pq:
        current_distance, current_node, cur_dir = heapq.heappop(pq)
        x, y = current_node

        if current_distance > distances[current_node]: continue
        if (x, y) == end: break

        for dx, dy in (directions[cur_dir], directions[(cur_dir + 1) % 4], directions[(cur_dir - 1) % 4]):
            nx, ny = x + dx, y + dy
            if graph[nx][ny] == '#': continue

            weight = 1001 if (dx, dy) != directions[cur_dir] else 1

            if (dx, dy) == directions[(cur_dir + 1) % 4]:
                next_dir = (cur_dir + 1) % 4
            elif (dx, dy) == directions[(cur_dir - 1) % 4]:
                next_dir = (cur_dir - 1) % 4
            else:
                next_dir = cur_dir

            distance = current_distance + weight

            if distance < distances[(nx, ny)]:
                distances[(nx, ny)] = distance
                heapq.heappush(pq, (distance, (nx, ny), next_dir))

    return distances[end]

# Expected tests results => 7036 & 11048
def main():
    map: Map = load_map()
    H, W = len(map), len(map[0])

    start, end, distances = find_start_and_end(map, H, W)

    score: int | float = dijkstra(map, distances, start, end)
    assert type(score) == int
    print(f"Score is {score}")

if __name__ == "__main__":
    main()
