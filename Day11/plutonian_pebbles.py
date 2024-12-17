from tqdm import tqdm

type Stone = str
type Stones = list[Stone]

type MulCache = dict[Stone, int]
type Cache = dict[Stone, list[Stone]]

def load_map():
    with open('input.txt') as f:
        input = f.read()
    return [c for c in input.strip().split(' ')]

def blink(map: Stones, mul_cache: MulCache) -> Stones:
    cpy: Stones = []
    cache: Cache = dict()

    def f(stone: Stone) -> Stones:
        tmp: Stones = []
        length = len(stone)

        if (stone == '0'):
            tmp.append(str(1))
        elif (length % 2 == 0):
            tmp.append(stone[:length//2])
            tmp.append(str(int(stone[length//2:])))
        else:
            if (stone in mul_cache):
                tmp.append(str(mul_cache[stone]))
            else:
                res = int(stone) * 2024
                mul_cache[stone] = res
                tmp.append(str(res))
        cache[stone] = tmp
        return tmp

    for stone in map:
        if (stone in cache):
            cpy.extend(cache[stone])
        else:
            cpy.extend(f(stone))

    return cpy

#def blink(map: Map) -> Map:
#    cpy: Map = []
#
#    for stone in map:
#        length = len(stone)
#        if (stone == '0'):
#            cpy.append(str(1))
#        elif (length % 2 == 0):
#            cpy.append(stone[:length//2])
#            #correct_half: str = remove_trailing_zero(stone[length//2:])
#            cpy.append(str(int(stone[length//2:])))
#        else:
#            cpy.append(str(int(stone) * 2024))
#    return cpy

def main():
    mul_cache :MulCache = dict()
    map: Stones = load_map()
    #print(f"Initial map -> {map}")
    for _ in range(25):
        tqdm()
        map = blink(map, mul_cache)
        #print(f"\nmap After blink-> {map}")
    print(f"Part 1: {len(map)}")

if __name__ == "__main__":
    main()
