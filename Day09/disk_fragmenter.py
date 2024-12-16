from collections import OrderedDict
from tqdm import tqdm

def load_map() -> str:
    with open('input.txt') as f:
        input = f.read()
    return input.strip()

def represent_map(input: str) -> tuple[list[str], OrderedDict]:
    empty_space = OrderedDict()
    map: list[str] = list('')
    actual_index = 0
    for i, c in enumerate(input):
        if (i % 2 == 0):
            map += str(i) * int(c)
            #print(f"actual index is {actual_index}")
        else:
            map += '.' * int(c)
            empty_space[actual_index] = int(c)
        actual_index += int(c)
    return map, empty_space

def get_checksum(map: list[str]) -> int:
    s_map = "".join(map)
    checksum: int = 0
    for i, c in enumerate(s_map):
        if (c.isalnum()):
            checksum += int(i) * int(c)
    return checksum

def find_first(empty_space: OrderedDict) -> tuple[int, int] | tuple[None, None]:
    for i, space in empty_space.items():
        if space != 0:
            return i, space
    return None, None

def is_finished(map: list[str]) -> bool:
    '''
    Mark a state when we see a dot
    If we ever meet something else its not done
    '''
    flag = False

    for c in map:
        if c == '.':
            flag = True
        elif c.isalnum() and flag == True:
            return False
    return flag

def fill_backward(map: list[str], empty_space: OrderedDict) -> list[str]:
    rev = [c for c in map[::-1]]
    for j, c in enumerate(tqdm(rev, desc="Processing Map")):
        # From the tail, every character to shift
        if (c.isalnum()):
            # Get the first index of empty space available
            i, _ = find_first(empty_space)
            if i is not None:
                # Put the last char in the correct place
                map[i] = c

                # Reverse indexing to remove from the actual map while using the reverse index
                map[-(j+1)] = '.'

                # Update empty space
                val = empty_space.pop(i)
                empty_space[i + 1] = val - 1
        # If we finish a block, check if there is more to do or not, even if there is still empty space available
        elif (is_finished(map)):
            break

    return map


def main():
    input = load_map()
    #print(f"Input is {input}")

    map, empty_space = represent_map(input)
    #print(f"Map is {map}\nEmpty space is {empty_space}")

    map = fill_backward(map, empty_space)
    #print(f"Filled map is {map}")

    checksum = get_checksum(map)
    print(f"Part 1: {checksum}")

if __name__ == '__main__':
    main()
