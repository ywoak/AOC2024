from collections import defaultdict

type Pos = tuple[int, int]
type Frequency = str
type Antennas = defaultdict[Frequency, list[Pos]]

type Map = list[list[str]]

def load_map() -> Map:
    map: Map = []

    with open('test.txt') as f:
        input = f.read()
    for line in input.split('\n'):
        if bool(line):
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

    return antennas

def find_antinodes(map: Map, antennas: Antennas) -> int:
    antinode_number: int = 0

    return antinode_number

def main() -> None:
    map: Map = load_map()
    antennas: Antennas = save_frequency_positions(map)
    for key, value in antennas.items():
        print(f"Frequency : {key}, Positions : {value}")
    antinode_number = find_antinodes(map, antennas)
    print(f"Part 1: {antinode_number}")

if __name__ == '__main__':
    main()
