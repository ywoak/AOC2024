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
        map = [list(line) for line in input.strip().split('\n')]
    return map

def save_frequency_positions(map: Map) -> Antennas:
    antennas: Antennas = defaultdict(list)
    for row, R in enumerate(map):
        for col, elem in enumerate(R):
            if (elem.isalnum()):
                antennas[elem].append((row, col))
    return antennas

def calculate_antinodes(pos1: Pos, pos2: Pos, H: int, W: int) -> set[Pos]:
    tmp = set()

    x1, y1 = pos1
    x2, y2 = pos2
    a1_x = x2 + (x2 - x1)
    a1_y = y2 + (y2 - y1)
    a2_x = x1 + (x1 - x2)
    a2_y = y1 + (y1 - y2)

    if not (is_out_of_bound(H, W, a1_x, a1_y)):
        tmp.add((a1_x, a1_y))
    if not (is_out_of_bound(H, W, a2_x, a2_y)):
        tmp.add((a2_x, a2_y))

    return tmp

def calculate_antinodes_recursive(pos1: Pos, pos2: Pos, H: int, W: int, antinodes: Antinodes, direction: int = 1) -> set[Pos]:
    x1, y1 = pos1
    x2, y2 = pos2
    if direction == 1:
        ax = x2 + (x2 - x1)
        ay = y2 + (y2 - y1)
    else:
        ax = x1 + (x1 - x2)
        ay = y1 + (y1 - y2)

    if is_out_of_bound(H, W, ax, ay):
        if direction == 0:
            return antinodes
        return calculate_antinodes_recursive(pos1, pos2, H, W, antinodes, direction=0)

    antinodes.add((ax, ay))
    if direction == 1:
        return calculate_antinodes_recursive(pos2, (ax, ay), H, W, antinodes, direction)
    else:
        return calculate_antinodes_recursive((ax, ay), pos1, H, W, antinodes, direction)

def find_antinodes(antennas: Antennas, H: int, W: int) -> tuple[Antinodes, Antinodes]:
    antinodes: Antinodes = set()
    rec_antinodes: Antinodes = set()

    for positions in antennas.values():
        rec_antinodes |= set(positions)
        length = len(positions)
        for i in range(length):
            for j in range(i + 1, length):
                antinodes |= calculate_antinodes(positions[i], positions[j], H, W)
                rec_antinodes |= calculate_antinodes_recursive(positions[i], positions[j], H, W, rec_antinodes)

    return antinodes, rec_antinodes

def is_out_of_bound(height: int, width: int, row: int, col: int) -> bool:
    return (not ((0 <= row < height) and (0 <= col < width)))

def remove_out_of_bound_antinodes(height: int, width: int, antinodes: Antinodes) -> Antinodes:
    antinode_cpy = set(antinodes)
    for position in antinodes:
        if (is_out_of_bound(height, width, position[0], position[1])):
            antinode_cpy.remove(position)
    return antinode_cpy

def main() -> None:
    map: Map = load_map()
    H: int = len(map)
    W: int = len(map[0])
    antennas: Antennas = save_frequency_positions(map)
    antinodes, rec_antinodes = find_antinodes(antennas, H, W)
    antinodes = remove_out_of_bound_antinodes(H, W, antinodes)
    print(f"Part 1: {len(antinodes)}")
    print(f"Part 2: {len(rec_antinodes)}")

if __name__ == '__main__':
    main()
