from collections import OrderedDict
from enum import IntEnum
from tqdm import tqdm

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

def get_checksum(map: list[str]) -> int:
    s_map = "".join(map)
    checksum: int = 0
    for i, c in enumerate(s_map):
        if (c.isalnum()):
            checksum += int(i) * int(c)

    return checksum

def find_first(empty_space: OrderedDict) -> tuple[int, int] | tuple[None, None]:
    for i, space in empty_space.items():
        if space > 0:
            return i, space

    return None, None

def get_last_switch_window(map: list[str], b: int):
    # Find a digit
    while not (map[b].isalnum()):
        b -= 1
    a: int = b

    tmp = map[b]

    # While there is a window, find it
    while (map[a] == tmp):
        a -= 1

    # Verify it there is a window but its already over or not
    cpy = a
    while (cpy > 0 and map[cpy].isalnum()):
        cpy -= 1
    if (cpy == 0):
        a = cpy

    return a, b

def get_first_empty_window(empty_space: OrderedDict):
    i = j = -1
    pos, space = find_first(empty_space)
    if pos and space:
        i = pos
        j = i + space - 1

    return i, j

# Perhaps representing it is annoying, because '.' is one place, while 10 is 2
# So without map representation to construct the final
# 1. un Point c'est un id, un state (taken, empty)
# 2. on peut dire que on a une map de Point

def fill_backward(map: list[str], empty_space: OrderedDict) -> list[str]:
    j = i = 0
    b: int = len(map) - 1

    progress_bar = tqdm(total=len(map))
    while (True):
        # Get first empty window (i, j inclusive)
        if not (i and (i <= j)): # Only recalculate the next in line if needed
            i, j = get_first_empty_window(empty_space)
            if i > 0:
                empty_space.pop(i) # We clean it instantly to avoid bugs, we dont need it anymore
            else: # If there is no more empty_space
                break
        #print(f'i, j -> {i, j}')

        # Get last to switch window (a exclusive)
        a, b = get_last_switch_window(map, b)
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
 
            progress_bar.update(1)

    progress_bar.close()
    return map

def main():
    input = load_map()
    print(f"Input is {input}")

    map = construct_map(input)
    print_map(map, string=True)

    #map = fill_backward(map, empty_space)
    #print(f"Filled map is {print_map(map)}")

    #checksum = get_checksum(map)
    #print(f"Part 1: {checksum}")

if __name__ == '__main__':
    main()
