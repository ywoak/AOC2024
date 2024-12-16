from enum import IntEnum

class State(IntEnum):
    EMPTY = 0
    FILL = 1

class Point:
    def __init__(self, state: State = State.EMPTY, id: int | None = None) -> None:
        self.state = state
        self.id = id

    def __str__(self) -> str:
        return f"State -> {self.state.name} | id -> {self.id}"

type Map = list[Point]

def load_map() -> str:
    with open('input.txt') as f:
        input = f.read()

    return input.strip()

def construct_map(input: str) -> Map:
    map: Map = list()
    for i, c in enumerate(input):
        if (i % 2 == 0):
            for _ in range(int(c)):
                map.append(Point(State.FILL, int(i) // 2))
        else:
            for _ in range(int(c)):
                map.append(Point(State.EMPTY, None))

    return map

def print_map(map: Map, string=False) -> None:
    if string:
        s = ""
        for point in map:
            if (point.state == State.EMPTY and point.id is None):
                s += '.'
            else:
                s += str(point.id)
        print(s)
    else:
        for point in map:
            print(point)

def get_checksum(map: Map) -> int:
    checksum: int = 0
    for i, c in enumerate(map):
        if (c.id is not None):
            checksum += i * c.id

    return checksum

def get_last_switch_window(map: Map, done: set | None = None) -> tuple[int, int]:
    b = map.__len__() - 1
    if done is not None:
        while ((b > 0) and ((map[b].state is State.EMPTY) or (map[b].id in done))):
            b -= 1
    else:
        while ((b > 0) and (map[b].state is State.EMPTY)):
            b -= 1

    if (b <= 0):
        return 0, 0

    a: int = b
    tmp = map[b].id
    if (map[b].id == 0):
        return 0, 0

    while ((a - 1 > 0) and (map[a - 1].state is State.FILL) and (map[a - 1].id == tmp)):
        a -= 1

    if (done is not None):
        cpy = a
        while ((cpy > 0) and (map[cpy].state is State.FILL)):
            cpy -= 1
        if (cpy == 0):
            a = cpy

    return a, b

def get_first_empty_window(map: Map, switch_window: int | None = None, size: int | None = None) -> tuple[int, int]:
    if (switch_window is not None and switch_window <= 0):
        return 0, 0
    for i, point in enumerate(map):
        if (point.state is State.EMPTY):
            j = i
            while ((j + 1 < len(map)) and (map[j + 1].state is State.EMPTY)):
                j += 1
            if (switch_window is None or size is None):
                return i, j
            else:
                if (i >= switch_window):
                    return 0, 0
                if (size <= j - i + 1):
                    return i, j

    return 0, 0

def fill_backward(map: Map) -> Map:
    j = i = 0
    b: int = len(map) - 1

    loop = 0
    while (True):
        loop += 1
        if (loop > 100000):
            break
        if not (i and (i <= j)):
            i, j = get_first_empty_window(map)
            if i < 0:
                break

        a, b = get_last_switch_window(map)
        if a <= 0:
            break

        while ((a <= b) and (i <= j)):
            map[i], map[b] = map[b], map[i]

            i += 1
            b -= 1

    return map

def shift_no_fragmentation(map: Map) -> Map:
    i = 0
    b: int = len(map) - 1

    done = set()
    loop = 0
    while (True and loop < 100000):
        loop += 1
        a, b = get_last_switch_window(map, done=done)
        if a <= 0:
            break
        fill_size = b - a + 1

        i, _ = get_first_empty_window(map, switch_window=a, size=fill_size)
        if i <= 0:
            done.add(map[b].id)
            continue

        while ((a <= b)):
            map[i], map[b] = map[b], map[i]
            print("\nMap after the swap -> ")
            print_map(map, string=True)

            i += 1
            b -= 1

        if (i > 0):
            done.add(map[i - 1].id)

    return map

def main():
    input = load_map()
    #p1map: Map = construct_map(input)
    p2map: Map = construct_map(input)

    #p1map: Map = fill_backward(p1map)
    p2map: Map = shift_no_fragmentation(p2map)

    #part1 = get_checksum(p1map)
    part2 = get_checksum(p2map)
    print_map(p2map, string=True)

    #print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

if __name__ == '__main__':
    main()
