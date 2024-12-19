from collections import deque
import sys

type GardenPlot = str
type GardenPlots = list[GardenPlot]

type Position = tuple[int, int]
type Positions = list[Position]

type Price = int
type Corners = int
type Area = int
type Perimeter = int

type Region = tuple[Area, Perimeter, Positions]
type Regions = list[Region]

type Visited = set[Position]

def load_map() -> GardenPlots:
    if len(sys.argv) != 2:
        raise ValueError("Usage: python ../get_input.py <day>")
    input = sys.argv[1]

    with open(input) as f:
        return [plot.strip() for plot in f.read().strip().split('\n')]

def in_bound(x: int, y: int, H: int, W: int) -> bool:
    return (0 <= x < H and 0 <= y < W)

def calculate_region(row: int, col: int, map: GardenPlots, vis: Visited, H: int, W: int) -> Region:
    directions: Positions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    queue: deque = deque([(row, col)])
    vis.add((row, col))

    area: Area = 0
    perimeter: Perimeter = 0
    pos: Positions = list()

    while queue:
        x, y = queue.pop()
        sides: int = 4

        for (dx, dy) in directions:
            nx, ny = x + dx, y + dy
            if (in_bound(nx, ny, H, W) and map[nx][ny] == map[x][y]):
                sides -= 1
                if not (nx, ny) in vis:
                    queue.append((nx, ny))
                    vis.add((nx, ny))

        area += 1
        perimeter += sides
        pos.append((x, y))

    return area, perimeter, pos

def fence_price(map: GardenPlots, H: int, W: int) -> tuple[Price, Regions]:
    regions: Regions = list()
    vis: Visited = set()

    for row in range(H):
        for col in range(W):
            if not ((row, col) in vis):
                region = calculate_region(row, col, map, vis, H, W)
                regions.append(region)

    return sum(area * perimeter for area, perimeter, _ in regions), regions

# TODO: change Positions as a set instead, for O(1) retrieve/inspect
def get_corners(shape: Positions) -> Corners:
    vertical: Positions = [(-1, 0), (1, 0)]
    horizontal: Positions = [(0, -1), (0, 1)]
    corners: Corners = 0

    for x, y in shape:
        for vx, vy in vertical:
            for hx, hy in horizontal:
                dvx, dvy, dhx, dhy = x + vx, y + vy, x + hx, y + hy
                # Concave
                if not (((dvx, dvy) in shape) or ((dhx, dhy) in shape)):
                    corners += 1
                # Convex
                elif (((dvx, dvy) in shape) and ((dhx, dhy) in shape) and ((dvx, dhy) not in shape)):
                    corners += 1

    return corners

def bulk_fence_price(regions: Regions) -> Price:
    return sum(area * get_corners(pos) for area, _, pos in regions)

def main() -> None:
    map: GardenPlots = load_map()
    H, W = len(map), len(map[0])

    price, regions = fence_price(map, H, W)
    bulk_price: Price = bulk_fence_price(regions)

    print(f"Part 1: {price}")
    print(f"Part 2: {bulk_price}")

if __name__ == "__main__":
    main()
