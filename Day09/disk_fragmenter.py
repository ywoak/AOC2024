from collections import OrderedDict

def load_map() -> str:
    with open('test.txt') as f:
        input = f.read()
    return input.strip()

def represent_map(input: str) -> list[str]:
    empty_space = OrderedDict()
    map: list[str] = list('')
    for i, c in enumerate(input):
        if (i % 2 == 0):
            map += str(i) * int(c)
        else:
            map += '.' * int(c)
            empty_space[i] = int(c)
    return map

def get_checksum(map: list[str]) -> int:
    s_map = "".join(map)
    checksum: int = 0
    for i, c in enumerate(s_map):
        if (c.isalnum()):
            checksum += int(i) * int(c)
    return checksum

def main():
    input = load_map()
    print(input)

    map = represent_map(input)
    print(map)

    checksum = get_checksum(map)
    print(checksum)

if __name__ == '__main__':
    main()
