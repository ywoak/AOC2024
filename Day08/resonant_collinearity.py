from collections import defaultdict

type Pos = tuple[int, int]
type Frequency = str
type Antennas = defaultdict[Frequency, list[Pos]]
type Antinodes = set[Pos]

type Map = list[list[str]]

def load_map() -> Map:
    map: Map = []

    with open('input.txt') as f:
        input = f.read()
    for line in input.split('\n'):
        if line:
            map.append(list(line))
    return map

def is_alpha(char: str) -> bool:
    return (('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'))

def save_frequency_positions(map: Map) -> Antennas:
    antennas: Antennas = defaultdict(list)
    for row, R in enumerate(map):
        for col, elem in enumerate(R):
            if (is_alpha(elem)):
                antennas[elem].append((row, col))
    print(f"Antennas {antennas}")
    return antennas

def calculate_antinodes(pos1: Pos, pos2: Pos) -> set[Pos]:
    x1, y1 = pos1
    x2, y2 = pos2
    a1_x = x2 + (x2 - x1)
    a1_y = y2 + (y2 - y1)
    a2_x = x1 + (x1 - x2)
    a2_y = y1 + (y1 - y2)
    print(f"For positions {pos1} and {pos2}\nThe first antinode is ({a1_x, a1_y})\nThe second is ({a2_x, a2_y})\n")
    return ({(a1_x, a1_y), (a2_x, a2_y)})

def find_antinodes(antennas: Antennas) -> Antinodes:
    antinodes: Antinodes = set()

    for positions in antennas.values():
        print(f"\n{positions}")
        length = len(positions)
        for i in range(length):
            j = i + 1
            while (j < length):
                antinodes |= calculate_antinodes(positions[i], positions[j])
                j += 1

    print(f"antinodes -> {antinodes}")
    return antinodes

def is_out_of_bound(height: int, width: int, row: int, col: int):
    return ((0 <= row < height) and (0 <= col < width))

def remove_out_of_bound_antinodes(height: int, width: int, antinodes: Antinodes) -> Antinodes:
    print(antinodes)
    antinode_cpy = set(antinodes)
    print(f"antinode_cpy -> {antinode_cpy}")
    for position in antinodes:
        if not (is_out_of_bound(height, width, position[0], position[1])):
            print(f"the out of bound position is {position}")
            antinode_cpy.remove(position)
    print(f"antinode_cpy -> {antinode_cpy}")
    return antinode_cpy

def main() -> None:
    map: Map = load_map()
    antennas: Antennas = save_frequency_positions(map)
    antinodes: Antinodes = find_antinodes(antennas)
    antinodes = remove_out_of_bound_antinodes(len(map), len(map[0]), antinodes)
    print(f"Part 1: {len(antinodes)}")

if __name__ == '__main__':
    main()
