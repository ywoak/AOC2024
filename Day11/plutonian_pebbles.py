from tqdm import tqdm

type Map = list[str]

def load_map():
    with open('input.txt') as f:
        input = f.read()
    return [c for c in input.strip().split(' ')]

def blink(map: Map) -> Map:
    cpy: Map = []

    for stone in map:
        length = len(stone)
        if (stone == '0'):
            cpy.append(str(1))
        elif (length % 2 == 0):
            cpy.append(stone[:length//2])
            #correct_half: str = remove_trailing_zero(stone[length//2:])
            cpy.append(str(int(stone[length//2:])))
        else:
            cpy.append(str(int(stone) * 2024))
    return cpy

def main():
    map: Map = load_map()
    #print(f"Initial map -> {map}")
    for _ in range(75):
        tqdm()
        map = blink(map)
        #print(f"\nmap After blink-> {map}")
    print(f"Part 1: {len(map)}")

if __name__ == "__main__":
    main()
