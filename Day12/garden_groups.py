import sys
from collections import deque, defaultdict

# Garden plot -> Une case
# Map -> garden plots
# Region -> Garden plot qui se touche (horizontal/vertical) avec les memes plantes
# area -> number of garden plot in a region
# perimeter -> number of sides of garden plots in the region that do not touch another garden plot in the same region.
# price -> sum of all regions area * perimeter
#
# Find price for garden

type GardenPlot = str
type GardenPlots = list[GardenPlot]

type Pos = tuple[int, int]

type Area = int
type Perimeter = int

type Region = tuple[Area, Perimeter]
type Regions = list[Region]

type D = defaultdict[GardenPlot, Regions]
type Visited = set[Pos]

def load_map() -> GardenPlots:
    if len(sys.argv) != 2:
        raise ValueError("Usage: python ../get_input.py <day>")
    input = sys.argv[1]
    with open(input) as f:
        map: GardenPlots = [plot for plot in f.read().strip().split('\n')]
    return map

def print_map(map):
    print('\n')
    for r in map: print(r)

def main() -> None:
    map: GardenPlots = load_map()
    print_map(map)

if __name__ == "__main__":
    main()
