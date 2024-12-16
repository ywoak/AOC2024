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
    with open('test3.txt') as f:
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

def get_last_switch_window(map: Map) -> tuple[int, int]:
    # Find something from the end
    b = map.__len__()
    while ((b > 0) and (map[b].state is State.EMPTY)):
        b -= 1

    a: int = b
    tmp = map[b].id

    # While there is a window of similar id, find it
    while ((a - 1 > 0) and (map[a - 1].state is State.FILL) and (map[a - 1].id == tmp)):
        a -= 1

    # Verify it there is a window but its already finished or not
    cpy = a
    while ((cpy > 0) and (map[cpy].state is State.FILL)):
        cpy -= 1
    if (cpy == 0):
        a = cpy

    return a, b

def get_first_empty_window(map: Map) -> tuple[int, int]:
    i = j = -1
    for i, point in enumerate(map):
        if (point.state is State.EMPTY):
            for j in range(i, len(map)):
                if ((j + 1 >= len(map)) or (map[j + 1].state is State.FILL)):
                    break

    return i, j

# Perhaps representing it is annoying, because '.' is one place, while 10 is 2
# So without map representation to construct the final
# 1. Un Point c'est un id, un state (taken, empty)
# 2. On peut dire que on a une map de Point
# 3. On garde l'approche des sliding windows

def fill_backward(map: Map) -> Map:
    j = i = 0
    b: int = len(map) - 1

    while (True):
        if not (i and (i <= j)): # Only recalculate the next in line if needed
            i, j = get_first_empty_window(map)
            print(f'i, j -> {i, j}')
            if i < 0: # If there is no more empty_space
                break

        a, b = get_last_switch_window(map)
        if a <= 0: # If there is only one block
            break

        while ((a < b) and (i <= j)):
            #print(f"\nMap before swap -> {"".join(map)}\nFirst window is {i, j}\nSecond window is {a, b}")
            map[i], map[b] = map[b], map[i]
            #print(f"Map after the swap -> {"".join(map)}")

            # Update empty_space
            #print(f"Empty space -> {[item for item in empty_space.items()]}")

            # Update windows
            i += 1
            b -= 1
 

    return map

def main():
    input = load_map()
    print(f"Input is {input}")

    map = construct_map(input)
    print_map(map, string=True)

    map = fill_backward(map)
    print_map(map)

    checksum = get_checksum(map)
    print(f"Part 1: {checksum}")

if __name__ == '__main__':
    main()
